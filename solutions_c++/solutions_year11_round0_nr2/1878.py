#include <iostream>
#include<sstream>

#include <cmath>
using namespace std;
char str[110]={'0'};
int main ()
{

	int t,c,d,n;
	char com1[40] ,com2[40],cre[40];
	char op1[30],op2[30];


		freopen("C:\\Users\\NAZI\\Desktop\\B-large.in", "rt", stdin);
		freopen("C:\\Users\\NAZI\\Desktop\\B-large.out", "wt", stdout);
	cin>>t;
	for(int i=0;i<t;i++)
	{//��������

		cin>>c;

		for(int j=0;j<c;j++)
		{
			cin>>com1[j]>>com2[j]>>cre[j];
		}
		cin>>d;
		for(int j=0;j<d;j++)
		{
			cin>>op1[j]>>op2[j];
		}
		cin>>n;
		if(n!=0)
			cin>>str[0];
		for(int j=1;j<n;j++)
		{//ѭ���ַ���
			cin>>str[j];

			for(int q=0;q<c;q++)
			{//�����Ƿ�����
				if(str[j-1]==com1[q] && str[j]==com2[q])
				{
					str[j]='0';
					str[j-1]=cre[q];
					j--;
					n--;
					break;
				}
				if(str[j-1]==com2[q] && str[j]==com1[q])
				{
					str[j]='0';
					str[j-1]=cre[q];
					j--;
					n--;
					break;
				}
			}//�����Ƿ�����

			for(int p=j-1;p>=0;p--)
			{//��ǰ���뵽��ʼ
				for(int q=0;q<d;q++)
				{//����������
					if(str[p]==op1[q] && str[j]==op2[q])
					{
						while(j>=p)
						{
							str[j]='0';
							j--;
							n--;
						}
						break;
					}
					if(str[p]==op2[q] && str[j]==op1[q])
					{
						while(j>=p)
						{
							str[j]='0';
							j--;
							n--;
						}
						break;
					}
				}//����������
			}//��ǰ���뵽��ʼ
		}//ѭ���ַ���

		cout<<"Case #"<<i+1<<": [";
		if(n>0)
		{
			for(int j=0;j<n-1;j++)
			{
				cout<<str[j]<<", ";
			}
			cout<<str[n-1]<<"]"<<endl;
		}
		else
			cout<<"]"<<endl;

	}//��������
	return 0;
}

