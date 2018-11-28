#include <stdio.h>
#include <memory.h>
#include <stdlib.h>

#define MOD 100003

int solve_small(int n) {
	int ans = 0;
	for (int i = 1 << n - 2, _n = (1 << n - 1); i < _n; ++i) {
		int z = n;
		while (i & (1 << z-2)) {
			int nz = 0;
			for (int j = 0; j < z-2; ++j) if (i & (1<<j))
				++nz;
			z = nz + 1;
		}
		if (z == 1) ans++;
	}
	return ans % MOD;
}

long long C[550][550];
int dp[550][500];

int solve(int n) {
	memset(dp, 0, sizeof dp);
	for (int x = 2; x <= n; ++x)
		dp[1][x] = 1;
	for (int len = 2; len < n; ++len) {
		for (int last = 2; last <= n; ++last) {
			for (int x = 1; x < len; ++x)
				dp[len][last] += dp[x][len] * C[len - x - 1][last - len - 1] % MOD;
		}
	}
	int ret = 0;
	for (int x = 1; x <= n; ++x)
		ret = (ret + dp[x][n]) % MOD;
	//if (ret != solve_small(n))
	//	abort();
	return ret;
}

int t;

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("C-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	//t = 100;

	C[0][0] = 1;
	for (int i = 1; i < 550; ++i) {
		C[i][0] = 1;
		for (int j = 1; j < 550; ++j)
			C[i][j] = (C[i-1][j] + C[i-1][j-1]) % MOD;
	}

	for (int i = 0; i < t; ++i) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", i+1, solve(n));
	}


		
	
}