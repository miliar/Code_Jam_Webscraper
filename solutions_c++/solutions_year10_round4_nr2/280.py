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

#define N 4205
#define K 12
#define inf 1000000000

int dp[N][K];
int a[N];
int i, j, k, n, m, x, y, z, t, T, tt, p;

inline int miin(int x, int y) {
	return x < y ? x : y;
}

int main() {
	freopen("large.in", "r", stdin);	freopen("large.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 1; tt <= T; tt ++) {
		scanf("%d", &p);
		n = (1 << p);
		for (i = n; i < n+ n; i ++) {
			scanf("%d", &a[i]);
			a[i] = p-a[i];
			for (j = 0; j < a[i]; j ++) {
				dp[i][j] = inf;
			}
			for (j = a[i]; j <= p; j ++) {
				dp[i][j] = 0;
			}
		}
		k = n / 2;
		while (k > 0) {
			for (i = k; i < k + k; i ++) {
				scanf("%d", &a[i]);
			}
			k /= 2;
		}
		for (i = n - 1; i > 0; i --) {
			for (j = 0; j <= p; j ++) {
				x = a[i] + dp[i+i][j+1] + dp[i+i+1][j+1];
				y = dp[i+i][j] + dp[i+i+1][j];
				dp[i][j] = miin(x, y);
				if (dp[i][j] > inf) {
					dp[i][j] = inf;
				}
			}
		}
		printf("Case #%d: %d\n", tt, dp[1][0]);
	}
	return 0;
}