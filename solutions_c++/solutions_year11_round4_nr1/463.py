#include <algorithm>
#include <stdio.h>
#include <string.h>
using namespace std;

const double ZERO = 1E-8;

int f[111];
int x, s, r, n, m, w;

int i, j, k, l, p, q, _, __;
double ans, t, p1, p2, p3;

int main() {
	scanf("%d", &__);
for (_ = 1; _ <= __; ++_) {
	scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
	memset(f, 0, sizeof f);
	for (m = 0, l = 0; n; --n) {
		scanf("%d%d%d", &p, &q, &w);
		f[0] += p - l, l = q;
		f[w] += q - p;
	}
	f[0] += x - l;

	for (ans = 0, i = 0; i <= 100; ++i) {
		if (!f[i]) continue;
		p1 = f[i] * 1.0 / (r + i);
		if (t - p1 >= -ZERO) t -= p1, ans += p1;
		else ans += t + (f[i] - (r + i) * t) / (s + i), t = 0;
	}
	printf("Case #%d: %.9lf\n", _, ans);
}
	return 0;
}