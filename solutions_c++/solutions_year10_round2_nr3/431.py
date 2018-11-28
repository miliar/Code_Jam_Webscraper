#include<iostream>
#include<algorithm>
int dp[501][501],c[501][501];
int main()
{
	int T,cs,i,j,n,k,b,t,ct,ans;
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	dp[2][1]=0;
	for(i=0;i<=500;i++)
		c[i][0]=c[i][i]=1;
	for(i=1;i<=500;i++)
		for(j=1;j<=i;j++)
			c[i][j]=(c[i-1][j]+c[i-1][j-1])%100003;
	for(i=2;i<=500;i++)
		dp[i][1]=1;
	for(i=3;i<=500;i++)
		for(j=1;j<i;j++)
		{
			for(k=1;k<j ;k++)
				dp[i][j]+=(dp[j][k]*c[i-j-1][j-k-1])%100003;
			dp[i][j]%=100003;
		}
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		scanf("%d",&n);
		for(ans=i=0;i<=n;i++)
			ans=(ans+dp[n][i])%100003;
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}
