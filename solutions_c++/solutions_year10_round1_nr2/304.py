#include<cstdio>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
const int BIG=0x3f3f3f3f;
#define cc(x) cout<<#x<<':'<<x<<endl;
#define MAX 101
int dp[MAX][257],a[MAX];
int main()
{
	int D,I,M,cs,i,j,k,dd,n,ans;
	scanf("%d",&cs);
	for(dd=1;dd<=cs;dd++)
	{
		scanf("%d%d%d%d",&D,&I,&M,&n);
		memset(dp,0x3f,sizeof(dp));
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=0;i<256;i++)
			dp[0][i]=abs(i-a[0]);
		dp[0][256]=D;
		for(i=0;i<n;i++)
			for(j=0;j<256;j++)
			{
				dp[i+1][j]=min(dp[i+1][j],dp[i][256]+abs(j-a[i+1]));
				dp[i+1][j]=min(dp[i+1][j],dp[i][j]+D);
				for(k=0;k<256;k++)
				{
					dp[i+1][k]=min(dp[i+1][k],dp[i][j]+(M?(max(0,abs(j-k)-1)/M*I):(j==k?0:10000000))+abs(k-a[i+1]));
					dp[i+1][k]=min(dp[i+1][k],dp[i][j]+(M?(max(0,abs(j-k)-1)/M*I):(j==k?0:10000000))+D);
				}
			}
		for(ans=BIG,i=0;i<=256;i++)
			ans=min(ans,dp[n-1][i]);
		printf("Case #%d: %d\n",dd,ans);
	}
}