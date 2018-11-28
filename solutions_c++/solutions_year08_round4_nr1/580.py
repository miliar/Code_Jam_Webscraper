#include<cstdio>
int dp[50000][2];
int g[50000];
int c[50000];
int f[50000];
const int INF=0x7fffffff;
void dfs(int u,int m)
{
	int tmp;
	/*if(2*u+2>=(m-1)/2)
	{
		if(g[u]==1)
		tmp=(f[2*u+1]&f[2*u+2]);
		else tmp=(f[2*u+1]|f[2*u+2]);
		dp[u][tmp]=0;
		if(c[u]==1)
		{
			if(g[u]==1)
			tmp=(f[2*u+1]|f[2*u+2]);
			else tmp=(f[2*u+1]&f[2*u+2]);
			dp[u][tmp]<?=1;
		}
		return;
	}*/
	if(2*u+1<(m-1)/2)
	dfs(2*u+1,m);
	if(2*u+2<(m-1)/2)
	dfs(2*u+2,m);
	if(g[u]==1)
	{
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][1]<?=dp[2*u+1][1]+dp[2*u+2][1];
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][0]<?=dp[2*u+1][0]+dp[2*u+2][0];
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][0]<?=dp[2*u+1][0]+dp[2*u+2][1];
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][0]<?=dp[2*u+1][1]+dp[2*u+2][0];
	}
	else 
	{
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][1]<?=dp[2*u+1][1]+dp[2*u+2][1];
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][0]<?=dp[2*u+1][0]+dp[2*u+2][0];
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][1]<?=dp[2*u+1][0]+dp[2*u+2][1];
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][1]<?=dp[2*u+1][1]+dp[2*u+2][0];
	}
	if(c[u]==1)
	{
		if(g[u]==0)
	{
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][1]<?=dp[2*u+1][1]+dp[2*u+2][1]+1;
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][0]<?=dp[2*u+1][0]+dp[2*u+2][0]+1;
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][0]<?=dp[2*u+1][0]+dp[2*u+2][1]+1;
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][0]<?=dp[2*u+1][1]+dp[2*u+2][0]+1;
	}
	else 
	{
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][1]<?=dp[2*u+1][1]+dp[2*u+2][1]+1;
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][0]<?=dp[2*u+1][0]+dp[2*u+2][0]+1;
		if(dp[2*u+1][0]!=INF&&dp[2*u+2][1]!=INF)
		dp[u][1]<?=dp[2*u+1][0]+dp[2*u+2][1]+1;
		if(dp[2*u+1][1]!=INF&&dp[2*u+2][0]!=INF)
		dp[u][1]<?=dp[2*u+1][1]+dp[2*u+2][0]+1;
	}
		
	}
}
		
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int t,cc,v,m,i;
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		scanf("%d%d",&m,&v);
		for(i=0;i<(m-1)/2;i++)
		{
			scanf("%d%d",&g[i],&c[i]);
			dp[i][0]=dp[i][1]=INF;
		}
		for(i=(m-1)/2;i<m;i++)
		{
			scanf("%d",&f[i]);
			dp[i][f[i]]=0;
			dp[i][1-f[i]]=INF;
		}
		dfs(0,m);
		printf("Case #%d: ",cc);
		if(dp[0][v]==INF)printf("IMPOSSIBLE\n");
		else printf("%d\n",dp[0][v]);
	}
	return 0;
}

		
