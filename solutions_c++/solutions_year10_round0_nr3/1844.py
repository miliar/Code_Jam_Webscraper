#include <cstdio>

#define int long long unsigned int

int v[1010][2], p, t, r, k, n, s, it, peg;
int g[1010];

main() {
	scanf("%llu", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%llu %llu %llu", &r, &k, &n);
		for (int j = 0; j < n; j++)
			scanf("%llu", &g[j]);

		for (int j = 0; j < n; j++) {
			s = 0; it = j; peg = 0;
			while ((s+g[it] <= k) && (peg < n)) {
				s += g[it]; 
				it = (it+1) % n;
				peg++;
			}
			v[j][0] = it;
			v[j][1] = s;
		}

		s = 0; it = 0;
		while (r--) {
			s += v[it][1];
			it = v[it][0];
		}

		printf("Case #%llu: %llu\n", i, s);
	}
}
