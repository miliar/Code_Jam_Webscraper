#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 110;
const int MAXV = 256;
const int INFF = 1000000000;

int cas, D, I, M, N, newv, a[MAXN], dp[MAXN][MAXV];

void gao(int id, int i, int j, int ii, int jj) {
//	printf("%d : [%d][%d]  => [%d][%d]\n", id, i, j, ii, jj);
}

int main() {
	freopen("input.txt", "r", stdin);
  	freopen("output.txt", "w", stdout);

	scanf("%d", &cas);
	for (int c = 1; c <= cas; c ++) {
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for (int i = 1; i <= N; i ++)
			scanf("%d", &a[i]);

		for (int i = 0; i <= N; i ++)
			for (int j = 0; j < MAXV; j ++)
				dp[i][j] = INFF;
		for (int j = 0; j < MAXV; j ++)
			dp[0][j] = 0;
		for (int i = 0; i < N; i ++) {
			for (int j = 0; j < MAXV; j ++) {
				if (dp[i][j] < INFF) {
					// delete
					newv = dp[i][j] + D;
					if (newv < dp[i+1][j]) {
						dp[i+1][j] = newv;
					}

					for (int k = 0; k < MAXV; k ++) {
						int cost = abs(k - a[i+1]);
						int diff = abs(k - j);

						if (diff <= M) {
							newv = dp[i][j] + cost;
							if (newv < dp[i+1][k]) {
								dp[i+1][k] = newv;
							}
						} else if (M != 0) {
							int kk;
							if (diff % M == 0)
								kk = diff / M - 1;
							else
								kk = diff / M;
							newv = dp[i][j] + cost + I*kk;
							if (newv < dp[i+1][k]) {
								dp[i+1][k] = newv;
							}
						}
					}
				}
			}
		}

		int ans = INFF;
		for (int j = 0; j < MAXV; j ++) {
			if (dp[N][j] < ans) {
				ans = dp[N][j];
			}
		}
		printf("Case #%d: %d\n", c, ans);
	}

	return 0;
}