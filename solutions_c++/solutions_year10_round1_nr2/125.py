#include <iostream>
#include <cmath>
using namespace std;
int i,j,k,n,m,testcase,curcase = 1,D,I,ans,num;
int dp[101][300],s[101];
bool used[300];
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d",&testcase) ; curcase <= testcase ; curcase++ )
	{
		scanf("%d %d %d %d\n",&D,&I,&m,&n);
		for ( i = 1 ; i <= n ; i++ )
			if (i==n) scanf("%d\n",&s[i]); else scanf("%d ",&s[i]); 
		printf("Case #%d: ",curcase);
		memset(dp,63,sizeof(dp));
		for ( i = 0 ; i < 256 ; i++ ) dp[0][i] = 0;
		for ( i = 0 ; i <= n ; i++ )
		{
			memset(used,false,sizeof(used));
			for ( j = 0 ;j < 256 ; j++ )
			{
				num = 290;
				for ( k = 0 ; k < 256 ; k++ )
					if ((!used[k])&&((num==290)||(dp[i][num]>dp[i][k]))) num = k;
				used[num] = true;
				for ( k = 0 ; k < 256 ; k++ )
				{	
					if (abs(num-k)<=m) dp[i][k] = min(dp[i][k],dp[i][num]+I);
					dp[i][k] = min(dp[i][k],dp[i][num]+abs(num-k));
				}
			}
			if (i==n) break;
			for ( j = 0 ; j < 256 ; j++ )
			{
				dp[i+1][j] = min(dp[i+1][j],dp[i][j]+D);
				for ( k = 0 ; k < 256 ; k++ )
					if (abs(j-k)<=m) dp[i+1][k] = min(dp[i+1][k],dp[i][j]+abs(k-s[i+1]));
			}
		}
		ans = 2000000000;
		for ( i = 0 ; i < 256 ; i++ )
			ans = min(ans,dp[n][i]);
		printf("%d\n",ans);
	}
}
