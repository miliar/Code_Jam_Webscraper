#include <string.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define maxn 1009
char str[maxn][maxn];
int n;
int K;
int rr[4]={0,1,1,1};
int cc[4]={1,1,0,-1};
void init()
{
	/*
	for(int i=1;i<=n;i++)
		printf("%s\n",str[i]+1);
	*/
	for(int i=1;i<=n;i++)
	{
		int ans=n;
		for(int j=n;j>=1;j--)
		{
			if(str[i][j]!='.')
			{
				str[i][ans]=str[i][j];
				ans--;
			}
		}
		while(ans)
		{
			str[i][ans]='.';
			ans--;
		}
	}	
	/*
	for(int i=1;i<=n;i++)
	{	
		for(int j=1;j<=n;j++)
			printf("%c",str[i][j]);
		printf("\n");
	}
	*/
}
bool check(char ch)
{
	int i,j;
	for(int r=1;r<=n;r++)
		for(int c=1;c<=n;c++)
		{
			for(int k=0;k<4;k++)
			{
				int ans=0;
				for(int z=0;z<K;z++)
				{	
					i=r+z*rr[k];
					j=c+z*cc[k];
					if(i>=1&&i<=n&&j>=1&&j<=n)
					{
						if(str[i][j]==ch)
							ans++;
					}
				}
				if(ans==K)
					return true;
			}
		}
	return false;
}
int main()
{
	int Q;
	scanf("%d",&Q);
	for(int t=1;t<=Q;t++)
	{
		scanf("%d%d",&n,&K);
		for(int i=1;i<=n;i++)
			scanf("%s",str[i]+1);
		init();
		bool flag1=check('R');
		bool flag2=check('B');
		printf("Case #%d: ",t);
		if(flag1)
		{
			if(flag2)
				printf("Both\n");
			else
				printf("Red\n");
		}
		else
		{
			if(flag2)
				printf("Blue\n");
			else
				printf("Neither\n");
		}
	}
	return 0;
}
