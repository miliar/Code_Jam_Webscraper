#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<string>
#include<stdlib.h>
#include<vector>
#include<math.h>
using namespace std;
int a[30];
int dp[21][4000000];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("ans.out","w",stdout);
	int t,k=0;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		bool sb=0;
		k++;
		scanf("%d",&n);
		memset(dp,0,sizeof(dp));
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		dp[0][2000000]=1;
		stack<int> a1;
		stack<int> a2;
		int flag=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<=4000000;j++)
			{
				if(dp[i][j])
				{
					dp[i+1][j+a[i]]=1;
					dp[i+1][j-a[i]]=1;
					if(i!=0)
						dp[i+1][j]=1;
				}
				if(dp[i+1][2000000])
				{
					flag=i+1;
					goto loop;
				}
			}
		}
loop:
		printf("Case #%d:\n",k);
		if(!flag)
			puts("impossible");
		else
		{
			int x=2000000;
			for(int i=flag;i>0;i--)
			{
				if(dp[i-1][x+a[i-1]])
				{
					a2.push(a[i-1]);
					x+=a[i-1];
				}
				else if(dp[i-1][x-a[i-1]])
				{
					a1.push(a[i-1]);
					x-=a[i-1];
				}
			}
			while(!a1.empty())
			{
				printf("%d",a1.top());
				a1.pop();
				if(a1.empty())
					printf("\n");
				else
					printf(" ");
			}
			while(!a2.empty())
			{
				printf("%d",a2.top());
				a2.pop();
				if(a2.empty())
					printf("\n");
				else
					printf(" ");
			}
		}
	}
}