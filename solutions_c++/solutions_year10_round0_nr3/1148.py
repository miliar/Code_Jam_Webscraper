#include <stdio.h>

int i, j, t, tt, n, k, r;
int g[1001];
int z[1001], p[1001]; // kolko zarobim a o kolko sa posuniem, ked zacnem z toho miesta

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		scanf("%d%d%d", &r, &k, &n);
		for (i = 0; i < n; i++) scanf("%d", &g[i]);
		for (i = 0; i < n; i++) {
			int kk = k;
			z[i] = g[i];
			kk -= g[i]; 
			for (p[i] = 1; (j = (i + p[i]) % n) != i; p[i]++) {
				kk -= g[j];
				if (kk < 0) break;
				z[i] += g[j];
			}
		}
		i = 0;
		long long res = 0;
		while (r--) {
			res += z[i];
			i = (i + p[i]) % n;
		}
		printf("%lld\n", res);
	}
	return 0;
}
