#include <cstdio>
#include <vector>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)

int main()
{
	char s[510], w[] = "welcome to code jam";
	gets(s);
	int T, M = 10000;
	sscanf(s, "%d", &T);
	FOR(cas,1,T+1)
	{
		gets(s);
		int n = strlen(s);
		int m = strlen(w);
		vector< vector<int> > dp(n+1, vector<int>(m+1, 0) );
		FOR(i,0,n+1)
			dp[i][m] = 1;
		for(int i=n-1; i>=0; --i)
			for(int j=m-1; j>=0; --j)
			{
				dp[i][j] = dp[i+1][j];
				if (s[i] == w[j])
					dp[i][j] = (dp[i][j] + dp[i+1][j+1]) % M;
			}
		printf("Case #%d: %04d\n", cas, dp[0][0]);
		fprintf(stderr, "Case #%d: %04d\n", cas, dp[0][0]);
	}
	return 0;
}
