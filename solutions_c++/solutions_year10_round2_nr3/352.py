#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int MOD = 100003;
int dp[501][501];
int choose[501][501];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-output0.out", "w", stdout);

	for(int i = 0; i <= 500; ++i) choose[i][0] = 1;
	for(int i = 1; i <= 500; ++i)
		for(int j = 1; j <= 500; ++j)
			choose[i][j] = choose[i - 1][j - 1] + choose[i - 1][j];
	for(int i = 2; i <= 500; ++i) dp[i][1] = 1;
	for(int i = 2; i < 500; ++i)
		for(int j = 2; j < i; ++j)
		{
			int& cnt = dp[i][j];
			for(int k = 1; k < j; ++k)
			{
				cnt = (cnt + (choose[i - j - 1][j - k - 1] * dp[j][k]) % MOD) % MOD;
			}
		}
	int T;
	scanf("%d", &T);
	for(int test = 1; test <= T; ++test)
	{
		int n;
		scanf("%d", &n);
		int res = 0;
		for(int i = 0; i <= 500; ++i)
			res = (res + dp[n][i]) % MOD;
		printf("Case #%d: %d\n", test, res);
	}

	return 0;
}