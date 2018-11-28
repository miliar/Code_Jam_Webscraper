#include<cstdio>
int dp[105][105];
bool mark[105][105];
int walk[2][2]={{2,1},{1,2}};
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("d-small.out","w",stdout);
	int t,cc,h,w,m,i,j,k,a,b;
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		scanf("%d%d%d",&h,&w,&m);
		for(i=1;i<=h;i++)
			for(j=1;j<=w;j++)
			{
				mark[i][j]=0;
				dp[i][j]=0;
			}
		for(i=0;i<m;i++)
		{
			scanf("%d%d",&a,&b);
			mark[a][b]=1;
		}
		if(mark[1][1]==0)dp[1][1]=1;
		for(i=1;i<=h;i++)
			for(j=1;j<=w;j++)
			{
				for(k=0;k<2;k++)
				{
					a=i+walk[k][0];
					b=j+walk[k][1];
					if(a>h||b>w)continue;
					if(mark[a][b]==0)
					{
						dp[a][b]=(dp[a][b]+dp[i][j])%10007;
					}
				}
			}
		printf("Case #%d: %d\n",cc,dp[h][w]);
	}
	
	return 0;
}
