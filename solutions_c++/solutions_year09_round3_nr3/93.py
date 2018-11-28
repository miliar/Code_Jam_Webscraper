#include<stdio.h>
#define N 111
int v[N],dp[N][N],s[N][N];
int main()
{
	freopen("C-large.in.txt","r",stdin);
	freopen("ou.txt", "w", stdout);
	int i,j,k,p,n,t,tt=1,ca;
	scanf("%d",&ca);
	while(ca--)
	{
		scanf("%d%d",&t,&n);
		for(i=1;i<=n;i++)
			scanf("%d",&v[i]);
		v[++n]=t+1;

		for(i=1;i<=n;i++)
		{
			dp[i][i]=0;
			s[i][i]=i;
		}

		for(k=1;k<=n;k++)
		{
			for(i=1;i+k<=n;i++)
			{
				j=i+k;
				dp[i][j]=dp[i][i]+dp[i+1][j]+(v[j]-v[i-1]-2),s[i][j]=i;
				for(p=s[i][j-1];p<=s[i+1][j];p++)
					if(dp[i][j]>dp[i][p]+dp[p+1][j]+(v[j]-v[i-1]-2))
						dp[i][j]=dp[i][p]+dp[p+1][j]+(v[j]-v[i-1]-2),s[i][j]=p;
			}
		}
		printf("Case #%d: %d\n",tt++,dp[1][n]);
	}
	return 0;
}

