#include<iostream>
using namespace std;
int dp[2][10001];
int d[10001],p[10001];
int main()
{
	int v,n,i,cs,css,inf=99999999;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d%d",&n,&v);
		for(i=1;i<=n;i++)
			dp[0][i]=dp[1][i]=inf;
		for(i=1;i<=n/2;i++)
		{
			scanf("%d%d",&d[i],&p[i]);
		}
		for(;i<=n;i++)
		{
			scanf("%d",&d[i]);
			dp[d[i]][i]=0;
		}
		for(i=n/2;i>0;i--)
		{
			if(p[i]==0)//不能变
			{
				if(d[i]==1)//与
				{
					dp[1][i]<?=dp[1][i*2]+dp[1][i*2+1];
					dp[0][i]<?=dp[0][i*2]+dp[1][i*2+1];
					dp[0][i]<?=dp[0][i*2]+dp[0][i*2+1];
					dp[0][i]<?=dp[1][i*2]+dp[0][i*2+1];
				}
				else
				{
					dp[1][i]<?=dp[1][i*2]+dp[1][i*2+1];
					dp[1][i]<?=dp[0][i*2]+dp[1][i*2+1];
					dp[0][i]<?=dp[0][i*2]+dp[0][i*2+1];
					dp[1][i]<?=dp[1][i*2]+dp[0][i*2+1];
				}
			}
			else
			{
				if(d[i]==1)//与
				{
					dp[1][i]<?=dp[1][i*2]+dp[1][i*2+1];
					dp[0][i]<?=dp[0][i*2]+dp[1][i*2+1];
					dp[0][i]<?=dp[0][i*2]+dp[0][i*2+1];
					dp[0][i]<?=dp[1][i*2]+dp[0][i*2+1];
					dp[1][i]<?=dp[1][i*2]+dp[1][i*2+1]+1;
					dp[1][i]<?=dp[0][i*2]+dp[1][i*2+1]+1;
					dp[0][i]<?=dp[0][i*2]+dp[0][i*2+1]+1;
					dp[1][i]<?=dp[1][i*2]+dp[0][i*2+1]+1;
				}
				else
				{
					dp[1][i]<?=dp[1][i*2]+dp[1][i*2+1];
					dp[1][i]<?=dp[0][i*2]+dp[1][i*2+1];
					dp[0][i]<?=dp[0][i*2]+dp[0][i*2+1];
					dp[1][i]<?=dp[1][i*2]+dp[0][i*2+1];
					dp[1][i]<?=dp[1][i*2]+dp[1][i*2+1]+1;
					dp[0][i]<?=dp[0][i*2]+dp[1][i*2+1]+1;
					dp[0][i]<?=dp[0][i*2]+dp[0][i*2+1]+1;
					dp[0][i]<?=dp[1][i*2]+dp[0][i*2+1]+1;
				}
			}
		}
		printf("Case #%d: ",css);
		if(dp[v][1]!=inf)printf("%d\n",dp[v][1]);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
