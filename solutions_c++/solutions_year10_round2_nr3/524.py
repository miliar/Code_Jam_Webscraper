#include<stdio.h>
int dp[501][501];
int c[501][501];
int main()
{
	for(int i=0;i<=500;i++)
		for(int j=0;j<=500;j++)
			dp[i][j]=c[i][j]=0;
	for(int i=0;i<=500;i++)
	{
		c[i][0]=c[i][i]=1;
		for(int j=1;j<i;j++)
			c[i][j]=(c[i-1][j-1]+c[i-1][j])%100003;
	}
	dp[2][1]=1;
	for(int i=3;i<=500;i++)
	{
		dp[i][1]=1;
		for(int j=2;j<i;j++)
		{
			for(int k=2;k<i;k++)
			{
				if(k!=j) continue;
				for(int l=1;l<k && l<j;l++)
				{
					if(i-k-1>=0 && j-l-1>=0 && j-l-1<=i-k-1)
						dp[i][j]+=(((long long)dp[k][l])*(long long)c[i-k-1][j-l-1])%100003;
				}
			}
		}
	}
	int tt,t;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		int n;
		int ans=0;
		scanf("%d",&n);
		for(int i=0;i<=500;i++)
			ans=(ans+dp[n][i])%100003;
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}

