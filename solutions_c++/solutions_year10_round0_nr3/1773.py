#include <stdio.h>
#include <string.h>
typedef __int64 ll;
const int MAXN = 1009;

ll ans;
int R, K, N;
int g[MAXN];
int sum[MAXN];
int next[MAXN];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	int i, j, k;
	int cur;
	int cas = 0;

	scanf("%d", &T);
	while (T--) {
		scanf("%d%d%d", &R, &K, &N);
		for (i = 0; i < N; ++i) {
			scanf("%d", &g[i]);
		}
		for (i = 0; i < N; ++i) {
			sum[i] = 0;
			for (j = i, k = 0; k < N; ++k, j = (j + 1) % N) {
				if (sum[i] + g[j] > K) {
					break;
				}
				sum[i] += g[j];
				next[i] = (j + 1) % N;
			}
		}
		ans = 0;
		cur = 0;
		for (i = 0; i < R; ++i) {
			ans += sum[cur];
			cur = next[cur];
		}
		printf("Case #%d: %I64d\n", ++cas, ans);
	}
	return 0;
}


