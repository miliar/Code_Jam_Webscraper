#include<iostream>
#include<fstream>
#include<memory.h>

using namespace std;
char   buf[105];
char search[100][100];
bool flag[100];
char queries[1000][100];
int main()
{
	int jump = 1;
	int sum = 1;
	int zhuan = 0;
	int n = 0;
	int s = 0;
	int q = 0;
	int i = 0;
	int j = 0;
	int k = 0;
	int cha = -1;
	bool first;
	ifstream f("A-large.in");
	ofstream fout("AAAAAA-large.out");

	if(f == NULL)   
	{   
		cout<<"error"<<endl;
		return 0;   
	}   
	if(!f.eof())   
	{  
		f.getline(buf, sizeof(buf));
		n = ::atoi(buf);               //��ȡ����
	}
	for(i = 0;i < n;i++)               //n��ѭ��
	{
		//--------------------------------------------------
		sum = 1;						 //���ݳ�ʼ��
		first = true;
		int zhuan = 0;
		memset(flag,false,100);
		cha = -1;
		//--------------------------------------------------
		f.getline(buf, sizeof(buf));
		s = ::atoi(buf);                 //������
		for(j = 0;j < s;j++)			 //�������search����
		{
			f.getline(search[j], 100);
		}
		f.getline(buf, sizeof(buf));     //�ؼ�����
		q = ::atoi(buf);
		for(k = 0;k < q;k++)			 //�ؼ��ִ���queries����
		{
			f.getline(queries[k], 100);
		}
		//�ڴ˴�������������
		for(k = 0;k < q;k++)
		{
			jump = 1;
			for(j = 0;j < s && jump == 1;j++)
			{
				if(j != cha)
				{
					if(!strcmp(queries[k],search[j]) && flag[j] == false)  //��������ַ������ ��Ӧ�ı��λ��Ϊfalse
					{
						flag[j] = true;
						sum++;
						if(first)
						{
							if(sum == s+1)
							{
								zhuan++;
								cha = j;
								first = false;
								jump = 0;
								sum = 1;
								memset(flag,false,100);
								break;
							}
						}
						else
						{
							if(sum == s)
							{
								zhuan++;
								cha = j;
								first = false;
								jump = 0;
								sum = 1;
								memset(flag,false,100);
								break;
							}
						}
					}
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<zhuan<<endl;
	}
	return 0;
}