#include<stdio.h>
int m[1100];
long long dp[12][1100][12];
int main()
{
	freopen("b-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	int tt,t;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<(1<<n);i++)
		{
			scanf("%d",&m[i]);
			m[i]=n-m[i];
		}
		for(int i=0;i<(1<<n);i++)
		{
			for(int j=0;j<m[i];j++)
				dp[n][i][j]=10000000;
			for(int j=m[i];j<=n;j++)
				dp[n][i][j]=0;
		}
		for(int i=n-1;i>=0;i--)
		{
			for(int j=0;j<(1<<i);j++)
				for(int k=0;k<=n;k++)
					dp[i][j][k]=10000000;
			
			for(int j=0;j<(1<<i);j++)
			{
				int c;
				scanf("%d",&c);
				for(int k=0;k<=n;k++)
				{
					dp[i][j][k]=dp[i+1][j*2][k]+dp[i+1][j*2+1][k];
					if(dp[i][j][k]>dp[i+1][j*2][k+1]+dp[i+1][j*2+1][k+1]+c)
						dp[i][j][k]=dp[i+1][j*2][k+1]+dp[i+1][j*2+1][k+1]+c;
				}
			}
		}
		printf("Case #%d: ",t);
		printf("%I64d\n",dp[0][0][0]);
//		printf("!!!!!!!!!%d\n",dp[1][0][1]);
	}
	return 0;
}
