#include<iostream>
using namespace std;
int tree[12000];
int mark[12000];
int dp[12000][2];
int m,c;
int mmin(int a,int b){return a<b?a:b;}
void dfs(int k)
{
	int i,j;
	if(k<=(m-1)/2)
	{
		dfs(k*2);
		dfs(k*2+1);
		if(mark[k]==1)
		{
			if(tree[k]==1)
			{
				for(i=0;i<2;++i)
				{
					for(j=0;j<2;++j)
					{
						dp[k][i|j]=mmin(dp[k][i|j],dp[2*k][i]+dp[2*k+1][j]+1);
						dp[k][i&j]=mmin(dp[k][i&j],dp[2*k][i]+dp[2*k+1][j]);
					}
				}
			}
			else
			{
				for(i=0;i<2;++i)
				{
					for(j=0;j<2;++j)
					{
						dp[k][i&j]=mmin(dp[k][i&j],dp[2*k][i]+dp[2*k+1][j]+1);
						dp[k][i|j]=mmin(dp[k][i|j],dp[2*k][i]+dp[2*k+1][j]);
					}
				}
			}
			/*if(tree[k]==1)
			{
				dp[k][tree[k*2]|tree[k*2+1]]=mmin(dp[k][tree[k*2]|tree[k*2+1]],dp[k*2][tree[k*2]]+dp[k*2+1][tree[k*2+1]]+1);
				dp[k][tree[k*2]&tree[k*2+1]]=mmin(dp[k][tree[k*2]&tree[k*2+1]],dp[k*2][tree[k*2]]+dp[k*2+1][tree[k*2+1]]);
			}
			else
			{
				dp[k][tree[k*2]&tree[k*2+1]]=mmin(dp[k][tree[k*2]|tree[k*2+1]],dp[k*2][tree[k*2]]+dp[k*2+1][tree[k*2+1]]+1);
				dp[k][tree[k*2]|tree[k*2+1]]=mmin(dp[k][tree[k*2]&tree[k*2+1]],dp[k*2][tree[k*2]]+dp[k*2+1][tree[k*2+1]]);
			}*/
		}
		else
		{
			if(tree[k]==1)
			{
				for(i=0;i<2;++i)
				{	
					for(j=0;j<2;++j)
					{
						dp[k][i&j]=mmin(dp[k][i&j],dp[2*k][i]+dp[2*k+1][j]);
					}
				}
			}
			else
			{
				for(i=0;i<2;++i)
				{
					for(j=0;j<2;++j)
					{
						dp[k][i|j]=mmin(dp[k][i|j],dp[2*k][i]+dp[2*k+1][j]);
					}
				}
			}
		}
	}
	return;
}
int main()
{
	int i,v;
	int cases,t;
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	scanf("%d",&cases);
	for(t=1;t<=cases;++t)
	{
		scanf("%d%d",&m,&v);
		for(i=1;i<=m;++i)
			dp[i][0]=dp[i][1]=1e9;
		for(i=1;i<=(m-1)/2;++i)
			scanf("%d%d",tree+i,mark+i);
		for(;i<=m;++i)
		{
			scanf("%d",tree+i);
			dp[i][tree[i]]=0;
		}
		dfs(1);
		if(dp[1][v]<1e9)
		{
			printf("Case #%d: %d\n",t,dp[1][v]);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",t);
		}
	}
	return 0;
}