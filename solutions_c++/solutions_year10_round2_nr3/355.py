#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

int dp[600][600];

const int MOD = 100003;
int C(int m, int n) { 
	return n ? (C(m - 1, n - 1) * m / n) % MOD : 1; 
}

void solve() {
	int n;
	cin >> n;

	memset(dp, 0, sizeof dp);

	for (int i = 2; i <= n; i++) {
		dp[i][1] = 1;
		for (int j = 1; j <= i - 1; j++) {
			for (int ni = i + i - j; ni <= n; ni++) {
				int nj = i;
				
				if (ni - i- 1 > 0 && i - j - 1 > 0) {
					dp[ni][nj] += ((long long)C(ni - i - 1, i - j - 1) * dp[i][j]) % MOD;
					dp[ni][nj] %= MOD;
				} else {
					dp[ni][nj] += dp[i][j];
					dp[ni][nj] %= MOD;
				}
			}
		}
	}
	int ans = 0;
	for (int i = 1; i <= n; i++) {
		ans += dp[n][i];
		ans %= MOD;
	}

	printf("%d\n", ans);
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}