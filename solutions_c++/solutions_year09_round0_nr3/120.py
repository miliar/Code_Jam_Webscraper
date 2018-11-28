#include <iostream>
#include <cstring>
using namespace std;

const int N = 500;
const int M = 20;
const int MOD = 10000;
char s[N + 1];
char t[] = "welcome to code jam";
int dp[N][M];

int main()
{
	int num, cas;
	int n, m;
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	m = strlen(t);
	scanf("%d\n", &cas);
	for (num = 1; num <= cas; ++num)
	{
		int i, j, k;
		gets(s);
		n = strlen(s);
		memset(dp, 0, sizeof(dp));
		dp[0][0] = (s[0] == t[0]);
		int ret = 0;
		for (i = 1; i < n; ++i)
		{
			dp[i][0] = (s[i] == t[0]);
			for (j = 1; j < m; ++j)
			{
				if (t[j] != s[i]) continue;
				for (k = i - 1; k >= 0; --k)
					dp[i][j] = (dp[i][j] + dp[k][j - 1]) % MOD;
			}
			ret = (ret + dp[i][m - 1]) % MOD;
		}
		printf("Case #%d: %04d\n", num, ret);
	}
	return 0;
}
