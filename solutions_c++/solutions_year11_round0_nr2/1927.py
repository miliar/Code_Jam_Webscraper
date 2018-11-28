#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

char a[35][35],b[35][35];
char que[1000];
int main()
{
	int t,n,i,j,r,cas=1;
	char ch1,ch2,ch3,ch;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			cin>>ch1>>ch2>>ch3;
			a[ch1-64][ch2-64]=ch3-64;
			a[ch2-64][ch1-64]=ch3-64;
		}
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			cin>>ch1>>ch2;
			b[ch1-64][ch2-64]=1;
			b[ch2-64][ch1-64]=1;
		}
		scanf("%d",&n);
		r=0;
		for(i=0;i<n;i++)
		{
			cin>>ch;
			if(ch!='Q'&&ch!='W'&&ch!='E'&&ch!='R'&&ch!='A'&&ch!='S'&&ch!='D'&&ch!='F')
			{
				que[r++]=ch-64;
				continue;
			}
			if(r==0)
			{
				que[r++]=ch-64;
				continue;
			}
			if(a[que[r-1]][ch-64])
				que[r-1]=a[que[r-1]][ch-64];
			else
			{
				for(j=0;j<r;j++)
					if(b[que[j]][ch-64])
						break;
				if(j>=r)
					que[r++]=ch-64;
				else 
					r=0;
			}
		}
		printf("Case #%d: [",cas++);
		if(r>0)
		{
			printf("%c",que[0]+64);
			for(i=1;i<r;i++)
				printf(", %c",que[i]+64);
		}
		printf("]\n");
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
	}
	return 0;
}
