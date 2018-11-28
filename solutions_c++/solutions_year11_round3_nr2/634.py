#include <stdio.h>
#include <cstring>

#define MAX_STARS (1000001)

int dist[MAX_STARS];
long long tsf[MAX_STARS];

int main() {
	int ntc, tc;
	int i, j;
	long long k, m, n;
	int L, N, t, C;
	scanf("%d", &ntc);
	for (tc = 1; tc <= ntc; tc++) {
		scanf("%d %d %d %d", &L, &t, &N, &C);

		for (i = 0; i < C; i++) {
			scanf("%d", &dist[i]);
			dist[i] *= 2;
		}
		for (; i < N; i++) dist[i] = dist[i % C];

		memset(tsf, -1, sizeof(tsf));
		tsf[0] = 0;
		for (i = 0; i < N; i++) {
			for (j = L; j > 0; j--) {
				if (tsf[j-1] < 0) continue;
				if (tsf[j-1] < t) {
					n = tsf[j-1] + dist[i] - t;
					if (n < 0)
						m = tsf[j-1] + dist[i];
					else
						m = tsf[j-1] + dist[i] - n/2;
				} else
					m = tsf[j-1] + dist[i]/2;
				if (tsf[j] >= 0) {
					k = tsf[j] + dist[i];
					tsf[j] = (k < m) ? k : m;
				} else
					tsf[j] = m;
			}
			tsf[0] = tsf[0] + dist[i];
		}

		m = 1000000L * 1000000;
		for (i = 0; i <= L; i++)
			if (tsf[i] >= 0 && tsf[i] < m) m = tsf[i];
		printf("Case #%d: %lld\n", tc, m);
	}
	return 0;
}

