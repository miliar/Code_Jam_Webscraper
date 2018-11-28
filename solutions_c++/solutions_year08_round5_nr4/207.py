#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <string.h>
#include <string>
using namespace std;

int i, j;

int dp[105][105];
char u[105][105];
int r, k, n, t, T, m, x, y;

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n >> k >> m;
		memset(dp, 0, sizeof(dp));
		memset(u, 0, sizeof(u));
		r = 0;
		for (i = 0; i < m; i ++) {
			cin >> x >> y;
			u[x][y] = 1;
		}
		dp[1][1] = 1;
		for (i = 1; i <= n; i ++) {
			for (j = 1; j <= k; j ++) {
				if (i - 1 > 0 && j - 2 > 0) {
					if (u[i-1][j-2] == 0) {
						dp[i][j] = (dp[i][j] + dp[i-1][j-2]) % 10007;
					}
				}
				if (i - 2 > 0 && j - 1 > 0) {
					if (u[i-2][j-1] == 0) {
						dp[i][j] = (dp[i][j] + dp[i-2][j-1]) % 10007;
					}
				}
			}
		}
		cout << "Case #" << t << ": " << dp[n][k] << endl;
	}
	return 0;
}





