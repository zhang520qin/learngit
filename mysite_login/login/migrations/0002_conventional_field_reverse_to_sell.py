# Generated by Django 2.2.5 on 2019-09-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='conventional_field',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name=32)),
                ('user_id', models.CharField(max_length=255)),
                ('use_name', models.CharField(max_length=128, unique=True)),
                ('create_data', models.DateField(auto_now_add=True)),
                ('updata', models.DateField(auto_now=True)),
                ('logic_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
            ],
        ),
        migrations.CreateModel(
            name='reverse_to_sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wechat_id', models.CharField(max_length=255)),
                ('content', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='login.conventional_field')),
            ],
        ),
    ]