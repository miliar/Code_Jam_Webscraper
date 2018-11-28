#include <cstdio>
#include <cstring>

typedef long long LL;

const int MAXN = 500 + 1;
const int MOD = 100003;

int C[MAXN][MAXN], dp[MAXN][MAXN];

int main() {
	C[0][0] = 1;
	for (int i = 1; i < MAXN; i++) {
		C[i][0] = C[i][i] = 1;
		for (int j = 1; j < i; j++) {
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
		}
	}
	dp[2][0] = 1;
	for (int o = 3; o < MAXN; o++) {
		for (int i = 2; i < o; i++) {
			int sum = 0;
			for (int j = 0; j <= i - 2; j++) {
				sum = (sum + (LL)C[o - i - 1][i - j - 2] * dp[i][j]) % MOD;
			}
			dp[o][i - 1] = sum % MOD;
		}
		dp[o][0] = 1;
	}
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		int n;
		scanf("%d", &n);
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum = (sum + dp[n][i]) % MOD;
		}
		printf("Case #%d: %d\n", oo + 1, sum);
	}
	return 0;
}
