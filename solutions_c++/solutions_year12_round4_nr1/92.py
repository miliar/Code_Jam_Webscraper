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

#define N 10005
int d[N], l[N], dp[N];

int i, j, k, n, m, x, y, z, t, tt, T;
int ab(int x) {
	return x >= 0 ? x : -x;
}


int main() {
	freopen("large.in", "r", stdin);	freopen("large.out", "w", stdout);

	scanf("%d", &T);
	for (tt= 1; tt <= T; tt ++) {
		scanf("%d", &n);
		for (i = 0; i < n; i ++) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &d[i]);
		l[i] = 1;
		n ++;
		memset(dp, 0, sizeof(dp));
		dp[0] = d[0];
		for (i = 0; i < n; i ++) {
			for (j = i + 1; j < n; j ++) {
				if (d[j] - d[i] > dp[i]) {
					break;
				}
				dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
			}
		}
		printf("Case #%d: ", tt);
		if (dp[n-1] > 0) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}



