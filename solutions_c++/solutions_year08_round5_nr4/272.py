#include "stdio.h"
int dp[1005][1005];
int main()
{
	int kase,tot,h,w,r,i,k,j;
	scanf("%d",&tot);
	for(kase=1;kase<=tot;kase++)
	{
		scanf("%d%d%d",&h,&w,&r);
		for(i=1;i<=h+2;i++)
			for(k=1;k<=w+2;k++)
				dp[i][k]=0;
		while(r--)
		{
			scanf("%d%d",&k,&j);
			dp[k][j]=-1;
		}
		dp[1][1]=1;
		for(i=1;i<h;i++)
			for(k=1;k<w;k++)
			{
				if(dp[i][k]==-1)
					continue;
				dp[i][k]%=10007;
				if(dp[i+1][k+2]!=-1)
					dp[i+1][k+2]+=dp[i][k];
				if(dp[i+2][k+1]!=-1)
					dp[i+2][k+1]+=dp[i][k];
			}
		dp[h][w]%=10007;
		printf("Case #%d: %d\n",kase,dp[h][w]);
	}
	return 0;
}