#include <cstdio>

int T, x, a, b, n, s, e, w, p;
double t, ans, len[1024];

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d:", r);
		p = 0;
		for (int i = 0; i < 1024; ++i)
			len[i] = 0;
		ans = 0;
		scanf("%d%d%d%lf%d", &x, &a, &b, &t, &n);
		b -= a;
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &s, &e, &w);
			len[a] += s - p;
			len[w + a] += e - s;
			p = e;
		}
		len[a] += x - p;
		for (int i = 1; i < 1024; ++i)
			if ((i + b)*t > len[i]) {
				t -= len[i]/(i + b);
				ans += len[i]/(i + b);
			} else {
				ans += t;
				len[i] -= t*(i + b);
				t = 0;
				ans += len[i]/i;
			}
		printf(" %.10lf\n", ans);
	}
	return 0;
}
