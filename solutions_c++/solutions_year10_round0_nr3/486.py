#include <iostream>
using namespace std;
int i,j,n,m,testcase,curcase = 1,tim,sum,curpos;
int s[2000],next[30][2000];
long long ans,dp[30][2000];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d",&testcase) ; curcase <= testcase; curcase++ )
	{
		scanf("%d%d%d",&tim,&m,&n);
		for ( i = 0 ; i < n ; i++ ) scanf("%d",&s[i]);
		for ( i = 0 ; i < n ; i++ )
		{
			sum = 0;
			for ( j = 0 ; j < n ; j++ )
			{
				sum += s[(i+j)%n];
				if (sum>m) break;
			}
			next[0][i] = (i+j)%n;
			if (sum>m) dp[0][i] = sum - s[(i+j)%n]; else dp[0][i] = sum;
		}
		ans = 0;
		curpos = 0;
		for ( i = 0 ; (1 << i)<=tim ; i++ )
		{
			if (tim&(1 << i))
			{
				ans += dp[i][curpos];
				curpos = next[i][curpos];
			}
			for ( j = 0 ; j < n ; j++ )
			{
				dp[i+1][j] = dp[i][j]+dp[i][next[i][j]];
				next[i+1][j] = next[i][next[i][j]];
			}
		}
		printf("Case #%d: %I64d\n",curcase,ans);
	}
}
