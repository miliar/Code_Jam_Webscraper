#include <cstdio>
#include <string>
#include <cstring>
#include <set>

using namespace std;

const int MOD = 100003;

int C[512][512];
int dp[512][512];

int dd()
{
	int ret = 0;
	int n;
	scanf("%d", &n);
	for (int rk = 1; rk < n; ++rk) {
		ret += dp[n][rk];
		if (ret >= MOD) ret -= MOD;
	}
	return ret;
}

int main()
{
	freopen("CC.in", "r", stdin);
	freopen("CC.txt", "w", stdout);
	C[0][0] = 1;
	for (int i = 1; i <= 500; ++i) {
		C[i][0] = C[i][i] = 1;
		for (int j = 1; j < i; ++j) {
			C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
			if (C[i][j] >= MOD) C[i][j] -= MOD;
		}
	}
	for (int n = 2; n <= 500; ++n) {
		for (int num = 1; num < n; ++num) {
			if (num == 1) {
				dp[n][num] = 1;
			}
			else {
				dp[n][num] = 0;
				for (int rk = num; rk <= num; ++rk) {
					for (int left = 1; left < rk; ++left) {
						int mid = num - left - 1;
						if (mid >= 0 && mid <= (n - rk - 1)) {
							dp[n][num] = ((long long)dp[rk][left] * C[n - rk - 1][mid] + dp[n][num]) % MOD;
						}
					}
				}
			}
		}
	}
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, dd());
	}
	return 0;
}