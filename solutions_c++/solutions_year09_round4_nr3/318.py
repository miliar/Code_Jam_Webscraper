#include <stdio.h>
#include <algorithm>

using namespace std;

int sign(int x) {
	if (x == 0) return 0;
	return x < 0 ? -1 : 1;
}

int p[16][25];
bool a[16][16];
int dp[1<<16];

int solve() {
	int n, k;
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < k; ++j)
			scanf("%d", &p[i][j]);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			a[i][j] = p[i][0] != p[j][0];
			if (a[i][j]) for (int t = 1; t < k; ++t)
				if (sign(p[i][0] - p[j][0]) != sign(p[i][t] - p[j][t])) {
					a[i][j] = false;
					break;
				}
		}
	memset(dp, -1, sizeof(dp));
	for (int m = 0; m < (1<<n); ++m) {
		bool ok = true;
		for (int i = 0; i < n; ++i) if (m & (1 << i))
			for (int j = i + 1; j < n; ++j) if (m & (1 << j))
				if (!a[i][j]) {
					ok = false;
					break;
				}
		if (ok) 
			dp[m] = 1;
	}
	dp[0] = 0;
	for (int m = 1; m < (1<<n); ++m) if(dp[m] == -1) {
		int &cur = dp[m];
		for (int sub = m; sub > 0; sub = (sub-1)&m) 
			if (dp[sub] != -1 && dp[m - sub] != -1)
				if (cur == -1 || cur > dp[sub] + dp[m - sub])
					cur = dp[sub] + dp[m - sub];
	}
	return dp[(1<<n)-1];
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: %d\n", i+1, solve());
	}
}