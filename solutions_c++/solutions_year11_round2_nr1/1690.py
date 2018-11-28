#include<iostream>
#include<cstdio>
#include<string.h>

using namespace std;

int main()
{
	int ch;
	cin>>ch;
	for(int k=1;k<=ch;k++)
	{
		int n;
		cin>>n;
		char arr[200][200];
		double brr[200][5]={0.0};
		for(int i=1;i<=n;i++)
		{
			scanf("%s",arr[i]);
		}
		for(int i=1;i<=n;i++)
		{
			int len = strlen(arr[i]);
			int win=0;
			int loose = 0;
			for(int j=0;j<len;j++)
			{
				if(arr[i][j]=='0')
					loose++;
				else if(arr[i][j]=='1')
					win++;
			}
			brr[i][0]=(win);
			brr[i][1]=(win+loose);
		}
		for(int i=1;i<=n;i++)
		{
			int len=strlen(arr[i]);
			double x=0.0;
			int count=0;
			for(int j=0;j<len;j++)
			{
				if(arr[i][j]=='1')
				{
					x+=((double)(brr[j+1][0])/(brr[j+1][1]-1));
					count++;
				}
				else if(arr[i][j]=='0')
				{
						x+=((double)(brr[j+1][0]-1)/(brr[j+1][1]-1));
						count++;
				}
			}
			brr[i][2]=x/count;
		}
		for(int i=1;i<=n;i++)
		{
			int len=strlen(arr[i]);
			double x=0.0;
			int count=0;
			for(int j=0;j<len;j++)
			{
				if(arr[i][j]=='1')
				{
					x+=brr[j+1][2];
					count++;
				}
				else if(arr[i][j]=='0')
				{
						x+=brr[j+1][2];
						count++;
				}
			}
			brr[i][3]=x/count;
		}
		cout<<"Case #"<<k<<":"<<endl;
		for(int i=1;i<=n;i++)
		{
			double x=0.25*((double)(brr[i][0])/(brr[i][1]))+0.50*brr[i][2]+0.25*brr[i][3];
			printf("%.9lf\n",x);
		}
	}
	return 0;
}