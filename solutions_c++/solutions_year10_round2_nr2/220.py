#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct chicken_t {
	long long x, v;
	bool arrive;
} chicken[1000];

long long cnt[1001], swap[1001];

int cmp(const void *a, const void *b)
{
	chicken_t *a0 = (chicken_t *) a, *b0 = (chicken_t *) b;
	return a0->x - b0->x;
}

int main()
{
	int c, cas, n, k, i;
	long long t, b;
	scanf("%d", &c);
	for (cas = 1; cas <= c; cas++) {
		scanf("%d%d%lld%lld", &n, &k, &b, &t);
		for (i = 0; i < n; i++) {
			scanf("%lld", &chicken[i].x);
		}
		for (i = 0; i < n; i++) {
			scanf("%lld", &chicken[i].v);
			chicken[i].arrive = (chicken[i].x + chicken[i].v * t >= b);
			//printf("%lld %lld\n", chicken[i].x + chicken[i].v * t, b);
			//printf("x = %lld, v = %lld, a = %d\n", chicken[i].x, chicken[i].v, chicken[i].arrive);
		}
		qsort(chicken, n, sizeof(chicken_t), cmp);
		memset(cnt, 0, sizeof(cnt));
		memset(swap, 0, sizeof(swap));
		for (i = n - 1; i >= 0; i--) {
			cnt[i] = cnt[i + 1] + chicken[i].arrive;
			swap[i] = swap[i + 1] + chicken[i].arrive * (n - i - 1 - cnt[i + 1]);
			//printf("i = %d: %d %d\n", i, cnt[i], swap[i]);
		}
		printf("Case #%d: ", cas);
		if (cnt[0] < k) printf("IMPOSSIBLE\n");
		else {
			for (i = 0; i < n; i++)
				if (cnt[i + 1] < k) break;
			printf("%lld\n", swap[i]);
		}
	}
	return 0;
}
