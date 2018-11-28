#include<stdio.h>
#include<algorithm>

using namespace std;

int ntest;
char g[12][12];
int s[12];
int dp[12][1<<10];

int cnt(int x)
{
	int ret=0;
	while(x)
	{
		ret += x%2;
		x/=2;
	}
	return ret;
}

int n,m;

int main()
{
	freopen("output.txt","w",stdout);
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
		{
			scanf("%s",&g[i]);
			for(int j=0;j<m;j++) if(g[i][j]=='x') s[i] = s[i] * 2 + 1; else s[i] = s[i] * 2;
		}
		memset(dp,0,sizeof(dp));
		int ans = 0;
		for(int j=0;j<(1<<m);j++)
		{
			if(j&s[0]) continue;
			if(j&(j<<1)) dp[0][j]=-2147483647;
			else dp[0][j] = cnt(j);
			if(dp[0][j]>ans)
				ans = dp[0][j];	

		}
		for(int i=1;i<n;i++)
			for(int j=0;j<(1<<m);j++)
			{
				if(j&s[i]) continue;

				if(j&(j<<1)) dp[i][j]=-2147483647;
				else
				{
					for(int k=0;k<(1<<m);k++)
					{
						if(k&s[i-1]) continue;
						if(k&(k<<1)) continue;
						if(k&(k>>1)) continue;
						if(j&(k<<1)) continue;
						if(j&(k>>1)) continue;
						dp[i][j] = max(dp[i][j] ,dp[i-1][k] + cnt(j));
					}
				}
				if(dp[i][j]>ans) 
					ans = dp[i][j];				
			}
			printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}