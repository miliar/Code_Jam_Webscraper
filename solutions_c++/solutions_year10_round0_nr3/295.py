#include <stdio.h>
#include <stdlib.h>

int n;

void iterate(long long *count, long long *sum, int times, long long *&itc, long long *&its)
{
	itc = new long long[n];
	its = new long long[n];
	int i;
	if (times == 0) {
		for (i = 0; i < n; i++) {
			itc[i] = 0;
			its[i] = 0;
		}
	} else if (times % 2 == 0) {
		long long *tc, *ts;
		iterate(count, sum, times / 2, tc, ts);
		for (i = 0; i < n; i++) {
			itc[i] = tc[i] + tc[(i + tc[i]) % n];
			its[i] = ts[i] + ts[(i + tc[i]) % n];
		}
	} else {
		long long *tc, *ts;
		iterate(count, sum, times - 1, tc, ts);
		for (i = 0; i < n; i++) {
			itc[i] = count[i] + tc[(i + count[i]) % n];
			its[i] = sum[i] + ts[(i + count[i]) % n];
		}
	}
}

int main()
{
	long long count[1010], sum[1010];
	int c, t, k, i, r, g[1010];
	scanf("%d", &t);
	for (c = 1; c <= t; c++) {
		scanf("%d%d%d", &r, &k, &n);
		for (i = 0; i < n; i++) scanf("%d", &g[i]);
		count[0] = 0; sum[0] = 0;
		for (i = 0; i < n && sum[0] + g[i] <= k; i++) {
			sum[0] += g[i]; count[0]++;
		}
		for (i = 1; i < n; i++) {
			sum[i] = sum[i - 1] - g[i - 1];
			count[i] = count[i - 1] - 1;
			while (count[i] < n && sum[i] + g[(i + count[i]) % n] <= k) {
				sum[i] += g[(i + count[i]) % n];
				count[i]++;
			}
		}
		long long *itc, *its;
		iterate(count, sum, r, itc, its);
		printf("Case #%d: %lld\n", c, its[0]);
		delete [] its;
		delete [] itc;
	}
	return 0;
}
