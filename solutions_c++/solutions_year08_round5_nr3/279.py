#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
char G[100][100];
int dp[100][1200]={0};

int n,m;

int solve(int i,int j)
{
	int result=0;
	for(int k=0;k<(1<<m);k++)
	{
		int flag=1;
		for(int t=0;t<m;t++)
		{
			if(k & (1<<t))
			{
				if(j & (1<<(t+1))) flag=0;
				if(t > 0 && (j & (1<<(t-1)))) flag=0;
			}
		}
		if(flag)
			result=max(result,dp[i-1][k]);
	}
	for(int t=0;t<m;t++)
		if(j & (1<<t)) result++;

	return result;
}
int main()
{
	int T,Ti=0;
	scanf("%d",&T);
	while(T--)
	{
		Ti++;
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++) scanf("%s",G[i]);

		vector<int> g[11];
		for(int i=1;i<=n;i++)
			for(int j=0;j<m;j++)
				if(G[i][j]=='x') g[i].push_back(j);

		memset(dp,0,sizeof(dp));
	//	dp[0][0]=1;

		for(int i=1;i<=n;i++)
		{
			for(int j=0;j<(1<<m);j++)
			{
				int flag=1;
				for(int k=0;k<g[i].size();k++)
					if(j & (1<<g[i][k])) flag=0;

				for(int k=0;k<=m-1;k++) 
					if((j & (3<<k)) == (3<<k)) flag=0;
				if(flag)
					dp[i][j]=solve(i,j);
			}
		}
	
		int result=0;
		for(int j=0;j<(1<<m);j++) result=max(result,dp[n][j]);

		printf("Case #%d: %d\n",Ti,result);
	}

}