#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

const int MOD = 100003;

int n;
LL dp[505][505];
LL C[505][505];

void Init() {
	C[0][0] = 1;
	C[1][0] = C[1][1] = 1;
	for (int i = 2; i <= 500; i++) {
		C[i][0] = C[i][i] = 1;
		for (int j = 1; j < i; j++) {
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
		}
	}
}

int calc(int n, int k) {
	if (dp[n][k] != -1) {
		return dp[n][k];
	}
	if (k == 1) {
		return dp[n][k] = 1;
	}
	LL ret = 0;
	for (int i = max(1, 2 * k - n); i < k; i++) {
		ret = (ret + calc(k, i) * C[n - k - 1][k - i - 1]) % MOD;
	}
	return dp[n][k] = ret;
}

int main() {
	Init();
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d", &n);
		LL res = 0;
		memset(dp, -1, sizeof(dp));
		for (int i = 1; i < n; i++) {
			res = (res + calc(n, i)) % MOD;
		}
		printf("Case #%d: %lld\n", cas, res);
	}
	return 0;
}
