#include <cstdio>
#include <memory.h>
#include <cmath>

#define MAXN 101
#define inf (int)1e6
#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) > (b) ? (a) : (b))

int T, N, D, I, M;
int arr[MAXN];

int d[2][257];

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	scanf("%d", &T);
	for (int q = 1; q <= T; q++) {
		scanf("%d %d %d %d", &D, &I, &M, &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
		}

		memset(d[1], 63, sizeof(d[1]));
		d[1][256] = 0;

		for (int i = 0; i < N; i++) {
			int ci = i % 2;
			int di = (i + 1) % 2;

			memset(d[ci], 63, sizeof(d[ci]));
			for (int k = 0; k < 256; k++) {
				d[ci][k] = d[di][256] + (int)(fabs(arr[i] - k) + 0.1);

				for (int j = 0; j < 256; j++) {
					if (d[di][j] < inf) {
						d[ci][j] = min(d[ci][j], d[di][j] + D);
	
						if (k == j) {
						d[ci][k] = min(d[ci][k], 
								d[di][j]
								+ (int)(fabs(arr[i] - k) + 0.1));
						} else
						if (M > 0) {
							d[ci][k] = min(d[ci][k], 
								d[di][j] + I * max(((int)(fabs(k - j) + 0.1) - 1) / M, 0)
								+ (int)(fabs(arr[i] - k) + 0.1));

						}
					}
				}
			}
			d[ci][256] = d[di][256] + D;
		}

		int ci = (N - 1) % 2;

		int ans = inf;
		for (int i = 0; i <= 256; i++) {
			ans = min(ans, d[ci][i]);
		}

		printf("Case #%d: %d\n", q, ans);
	}

	return 0;
}

