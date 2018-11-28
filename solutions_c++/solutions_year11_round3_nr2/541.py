#include <stdio.h>

#define MIN(x, y) ((x) < (y) ? (x) : (y))
const int MAXC = 1010, MAXL = 2;
int d[MAXC];
int l, n, c;
long long t;
long long f[MAXL + 1];
int main() {
	int cases;
	scanf("%d", &cases);
	for (int k = 0; k < cases; ++k) {
		printf("Case #%d: ", k + 1);
		scanf("%d%lld%d%d", &l, &t, &n, &c);
		for (int i = 0; i < c; ++i)
			scanf("%d", &d[i]);
		for (int i = 0; i <= l; ++i)
			f[i] = 0;
		for (int i = 0 ; i < n; ++i) {
			for (int j = l; j >= 0; --j) {
				f[j] += d[i % c] * 2;
				if ((j > 0) && (t < f[j])) {
					if (t < f[j - 1])
						f[j] = MIN(f[j], f[j - 1] + d[i % c]);
					else
						f[j] = MIN(f[j], f[j - 1] + d[i % c] + (t - f[j - 1]) / 2);
				}
			}
		}
		printf("%lld\n", f[l]);
	}
	return 0;
}
