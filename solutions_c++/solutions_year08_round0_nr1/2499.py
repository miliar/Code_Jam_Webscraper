#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<process.h>

char engine[100][100];

void clearflag(int *);
int searchstr(char *,int);
void main()
{
	int n,flag[100];
	char query[100];
	clrscr();
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int m;
		cin>>m;
		cin.getline(engine[0],100);
		for(int j=0;j<m;j++)
		{
			cin.getline(engine[j],100);
		}

		int k;
		cin>>k;
		cin.getline(query,100);

		int sw=-1;
		clearflag(flag);
		int m1=m;
		for(j=1;j<=k;j++)
		{
			cin.getline(query,100);
			int l = searchstr(query,m);
			if(flag[l]==0)
			{
				flag[l]=1;
				m1--;
			}
			if(m1==0)
			{
				sw++;
				m1=m;
				clearflag(flag);
				flag[l]=1;
				m1--;
			}
		}
		sw++;
		cout<<"Case #"<<i<<": "<<sw<<"\n";
	}
}
void clearflag(int *a)
{
	for(int i=0;i<100;i++)
		a[i]=0;
}
int searchstr(char *str,int a)
{
	for(int i=0;i<a;i++)
		if(strcmp(engine[i],str)==0)
			return i;
	return -1;
}