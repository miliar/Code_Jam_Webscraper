#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int data[100],cd;

int ff[1<<10][10];

int fun(int s,int i)
{
	if(i==cd) return 0;
	int ret=10000;
	if(ff[s][i]!=-1) return ff[s][i];
	int j;
	for(j=data[i];j<cd;j++)
	{
		if(s&(1<<j))
		{
			int k;
			int sm=0;
			for(k=0;k<j;k++)
			{
				if(s&(1<<k))
				{
					sm++;
				}
			}
			int r=sm+fun(s^(1<<j),i+1);
			if(r<ret) ret=r;
		}
	}
	return ff[s][i]=ret;
}

int solve()
{
	memset(ff,0xff,sizeof(ff));
	return fun((1<<cd)-1,0);
}

int main()
{
	int t;
	scanf("%d",&t);
	char buf[1000];
	int cse=0;
	while(t--)
	{
		cse++;
		scanf("%d",&cd);
		int i,j;
		for(i=0;i<cd;i++)
		{
			scanf("%s",buf);
			int mj=-1;
			for(j=0;buf[j];j++)
			{
				if(buf[j]=='1') mj=j;
			}
			data[i]=mj;
		}
		int ret=solve();
		printf("Case #%d: %d\n",cse,ret);
	}
	return 0;
}
