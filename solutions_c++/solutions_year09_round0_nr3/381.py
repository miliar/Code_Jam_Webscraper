#include <cstdio>
#include <cstring>
using namespace std;

const int MOD = 10000;
const char welcome[]="welcome to code jam";
int dp[510][20];
char a[510];



int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int cas,N,L,i,j;
	scanf("%d%*c",&N);
	for (cas=0;cas<N;++cas)
	{
		gets(a);
		L = strlen(a);
		memset(dp,0,sizeof(dp));
		dp[0][0] = a[0]=='w' ? 1 : 0;
		for (i=1;i<L;++i)
		{
			dp[i][0] = (dp[i-1][0] + (a[i]=='w'?1:0)) % MOD;
			for (j=1;j<19;++j)
			{
				dp[i][j] = dp[i-1][j];
				if (a[i]==welcome[j]) dp[i][j] += dp[i-1][j-1];
				dp[i][j] %= MOD;
			}
		}
		printf("Case #%d: %04d\n",cas+1,dp[L-1][18]);
	}
	return 0;
}
