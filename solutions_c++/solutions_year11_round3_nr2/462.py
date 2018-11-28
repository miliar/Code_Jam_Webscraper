#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long i64;

i64 dp[1100][3];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t,n,i,j,c,l;
	i64 T,tt,res;
	int a[1100];
	scanf("%d",&t);
	for (int cnt=1;cnt<=t;cnt++)
	{
		printf("Case #%d: ",cnt);
		scanf("%d%lld%d%d",&l,&T,&n,&c);
		for (i=0;i<c;i++)
			scanf("%d",&a[i]);
		for (;i<n;i++)
			a[i]=a[i-c];
		memset(dp,-1,sizeof(dp));
		dp[0][0]=0;
		for (i=0;i<n;i++)
		{
			for (j=0;j<=l;j++)
			{
				tt=dp[i][j];
				if (tt==-1) continue;
				if (dp[i+1][j]==-1) dp[i+1][j]=tt+a[i]*2;
					else dp[i+1][j]=min(tt+a[i]*2,dp[i+1][j]);
				if (j<l)
				{
					if (tt>=T)
						tt+=a[i];
					else
						if (tt+a[i]*2>=T)
							tt=T+(a[i]-(T-tt)/2);
						else tt+=2*a[i];
					if (dp[i+1][j+1]==-1) dp[i+1][j+1]=tt;
					else dp[i+1][j+1]=min(tt,dp[i+1][j+1]);
				}
			}
		}
		res=dp[n][0];
		for (i=1;i<=l;i++)
			if (dp[n][i]<res) res=dp[n][i];
		printf("%lld\n",res);
	}
	return 0;
}