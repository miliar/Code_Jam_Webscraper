#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int dp[110][110];
int a[110],c[110][4];
int mabs(int x) 
{
	return x>0 ? x : (-x);
}
int sure(int x,int y,int z)
{
	return mabs(x-y) <= 2 && mabs(y-z) <= 2 && mabs(x-z) <= 2;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++) {
		int n,s,p;
		memset(c,0,sizeof(c));
		memset(dp,0,sizeof(dp));
		int i,j,k,r;
		scanf("%d%d%d",&n,&s,&p);
		for(i=1;i<=n;i++)
			scanf("%d",&a[i]);
		for(r=1;r<=n;r++) {
			for(i=0;i<=10;i++)
				for(j=0;j<=10 && i + j <=a[r];j++)
					for(k=0;k<=10&&i+j+k<=a[r];k++)
						if(i+j+k==a[r] && sure(i,j,k)) {
							int f = 0;
							if(mabs(i-j)==2||mabs(i-k)==2||mabs(j-k)==2) f++;
							if(i>=p||j>=p||k>=p) f+=2;
							c[r][f] = 1;
						}
		}
		for(i=1;i<=n;i++) {
			for(j=0;j<=i&&j<=s;j++) {
				if(c[i][0]) dp[i][j] = dp[i-1][j];
				if(c[i][1]&&j) dp[i][j] = max(dp[i][j],dp[i-1][j-1]);
				if(c[i][2]) dp[i][j] = max(dp[i][j],dp[i-1][j] + 1);
				if(c[i][3]&&j) dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1);
			}
		}
		printf("Case #%d: %d\n",tt,dp[n][s]);

	}
	return 0;
}


