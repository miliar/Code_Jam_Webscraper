#include <iostream>
#include <stdio.h>
using namespace std;

#define N 505

int i, j, k, n, m, x, y, z, t, T;
int dp[25][N];

char a[] = "#welcome to code jam";
char ccc;
char b[N];
int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	m = 10000;
	scanf("%d%c", &T, &ccc);
	for (t = 1; t <= T; t ++) {
		memset(dp, 0, sizeof(dp));
		memset(b, 0, sizeof(b));
		gets(b + 1);
		n = strlen(a);
		k = strlen(b+1);
		dp[0][0] = 1;
		for (i = 0; i < n; i ++) {
			for (j = 0; j <= k; j ++) {
				if (a[i] == b[j]) {
					if (i > 0 && j > 0) {
						dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % m;
					}
				}
				if (j > 0) {
					dp[i][j] = (dp[i][j] + dp[i][j-1]) % m;
				}
			}
		}
		printf("Case #%d: %04d\n", t, dp[n-1][k]);
	}
	return 0;
}


