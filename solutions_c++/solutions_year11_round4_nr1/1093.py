#include <cstdio>
#include <cstring>

#define ABS(a) ((a) > 0 ? (a) : -(a))

const int MAXN = 1000 + 1;

int q;
int n;
double t, s, r, x;

double b[MAXN], e[MAXN], w[MAXN];

void sort(int l, int r) {
	int i = l, j = r;
	double x = w[(l + r) >> 1];
	while (i <= j) {
		while (w[i] < x) i ++;
		while (w[j] > x) j --;
		if (i <= j) {
			double t = b[i];
			b[i] = b[j];
			b[j] = t;
			t = e[i];
			e[i] = e[j];
			e[j] = t;
			t = w[i];
			w[i] = w[j];
			w[j] = t;
			i ++;
			j --;
		}
	}
	if (i < r) sort(i, r);
	if (l < j) sort(l, j);
}


int main() {
	scanf("%d", &q);
	for (int z = 1; z <= q; z ++) {
		scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
		for (int i = 1; i <= n; i ++) scanf("%lf%lf%lf", &b[i], &e[i], &w[i]);
		double sum = 0;
		for (int i = 1; i <= n; i ++) sum += e[i] - b[i];
		double ans = 0;
		if (x - sum >= r * t) {
			ans += t;
			ans += (x - sum - r * t) / s;
			for (int i = 1; i <= n; i ++) ans += (e[i] - b[i]) / (s + w[i]);
			printf("Case #%d: %0.9lf\n", z, ans);
		} else {
			sort(1, n);
			double tmp = t;
			tmp -= (x - sum) / r;
			ans += (x - sum) / r;
			for (int i = 1; i <= n; i ++) {
				if ((r + w[i]) * tmp >= e[i] - b[i]) {
					ans += (e[i] - b[i]) / (r + w[i]);
					if (tmp > 0) tmp -= (e[i] - b[i]) / (r + w[i]);
				} else {
					ans += tmp;
					ans += (e[i] - b[i] - (r + w[i]) * tmp) / (s + w[i]);
					tmp = 0;
				}
			}
			printf("Case #%d: %0.9lf\n", z, ans);
		}
	}
	return 0;
}

