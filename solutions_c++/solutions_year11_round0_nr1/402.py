#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 105
#define inf 100000000

int a[N];
char c[N];
int dp[N];
int i, j, k, n, m, x, y, z, t, T, tt, px, py, dx, dy;
int ab(int x) {
	return x >= 0 ? x : -x;
}
int main() {
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		cin >> n;
		for (i = 1; i <= n; i ++) {
			cin >> c[i] >> a[i];
		}
		dp[0] = 0;
		for (i = 1; i <= n; i ++) {
			for (j = i - 1; j >= 1; j --) {
				if (c[j] == c[i]) {
					break;
				}
			}
			if (j == 0) {
				dp[i] = a[i];
			} else {
				dp[i] = ab(a[i] - a[j]) + 1 + dp[j];
			}
			if (dp[i-1] >= dp[i]) {
				dp[i] = dp[i-1] + 1;
			}
		}
		printf("Case #%d: %d\n", tt, dp[n]);
	}
	return 0;
}


