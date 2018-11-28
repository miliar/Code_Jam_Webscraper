#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
bool useok(int t,int p)
{
	if (t>28||t<2)return false;
	if (p>=2)
 	{
		t-=3*p;
		t+=4;
		return t>=0;
	}
	else return true;
}
bool nouseok(int t,int p)
{
	t-=3*p;
	t+=2;
	return t>=0;
}
int T,s,p,d[102];
int dp[102][102];
int gg,n;
int main()
{
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d%d%d",&n,&s,&p);
		for (int i=1;i<=n;i++)
			scanf("%d",&d[i]);
		memset(dp,-12,sizeof(dp));
		dp[0][0]=0;
		for (int i=0;i<n;i++)
		for (int j=0;j<=s;j++)
		{
			if (useok(d[i+1],p))
				dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+1);
			if (nouseok(d[i+1],p))
				dp[i+1][j]=max(dp[i+1][j],dp[i][j]+1);
			dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]);
			dp[i+1][j]=max(dp[i+1][j],dp[i][j]);
		}
		printf("Case #%d: %d\n",++gg,dp[n][s]);
	}
}
