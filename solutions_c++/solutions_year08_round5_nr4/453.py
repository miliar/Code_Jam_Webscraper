#include <stdio.h>

int main()
{
	int dp[205][205];
	int x,y;
	int r,i,j;
	int n,m;
	int cas,asd;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d %d %d",&n,&m,&r);

		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				dp[i][j]=0;
		for(i=0;i<r;i++)
		{
			scanf("%d %d",&x,&y);
			x--;y--;
			dp[x][y] = -1;
		}
		dp[0][0]=1;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(dp[i][j]==-1)
					continue;
				if(dp[i+2][j+1]!=-1)
					dp[i+2][j+1] = (dp[i+2][j+1]+dp[i][j])%10007;
				if(dp[i+1][j+2]!=-1)
					dp[i+1][j+2] = (dp[i+1][j+2]+dp[i][j])%10007;
			}
		}
		printf("Case #%d: ",asd+1);
		if(dp[n-1][m-1]!=-1)
		{
			printf("%d\n",dp[n-1][m-1]);
		}
		else
		{
			printf("0\n");
		}

	}
	return 0;
}