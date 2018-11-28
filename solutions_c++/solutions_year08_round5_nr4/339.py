#pragma comment(linker,"/STACK:256000000")

#ifdef __GNUC__
#define int64 long long
#else /* MSVC, say */
#define int64 __int64
#endif 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))

#define MAXN (1 << 7)
#define MOD 10007

int dp[MAXN][MAXN];
int a[MAXN][MAXN];

int main() {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		memset(dp, -1, sizeof(dp));
		for (int i = 0; i < MAXN; i++) {
			dp[0][i] = 0;
			dp[1][i] = 0;
			dp[i][0] = 0;
			dp[i][1] = 0;
		}
		dp[1][1] = 1;
		int h, w;
		int k;
		scanf("%d %d %d", &h, &w, &k);
		for (int i = 0; i < k; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			dp[x][y] = 0;
		}
		for (int i = 2; i <= h; i++) {
			for (int j = 2; j <= w; j++) {
				if (dp[i][j] == -1) {
					dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j - 2]) % MOD;
				}
			}
		}
		printf("Case #%d: ", test);
		printf("%d", dp[h][w]);
		printf("\n");
	}

	return 0;
}
