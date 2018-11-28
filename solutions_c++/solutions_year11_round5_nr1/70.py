#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 128;

struct Area {
	int n;
	double x[MAXN], y[MAXN], z[MAXN];

	void init(int n) {
		this->n = n;
		for (int i = 0; i < n; ++i) {
			scanf("%lf%lf", &x[i], &y[i]);
			if (i > 0) {
				z[i] = (y[i] - y[i - 1]) / (x[i] - x[i - 1]);
			}
		}
	}

	double gao(double xx) {
		double ret = 0.0;
		for (int i = 1; i < n; ++i) {
			if (xx <= x[i]) {
				double yy = y[i - 1] + z[i] * (xx - x[i - 1]);
				ret += (xx - x[i - 1]) * (yy + y[i - 1]);
				break;
			} else {
				ret += (x[i] - x[i - 1]) * (y[i] + y[i - 1]);
			}
		}
		return ret;
	}
} lo, up;

int main() {
	int re, w, n, m, g;
	double s, t;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d%d%d%d", &w, &n, &m, &g);
		lo.init(n);
		up.init(m);
		s = up.gao(w) - lo.gao(w);

		printf("Case #%d:\n", ri);
		fflush(stdout);
		for (int i = 1; i < g; ++i) {
			t = s / g * i;
			double l = 0, r = w;
			for (int j = 0; j < 100; ++j) {
				double mid = (l + r) / 2;
			//	printf("%lf | %lf ?  %lf\n", mid, up.gao(mid) - lo.gao(mid), t);
				if (up.gao(mid) - lo.gao(mid) < t) {
					l = mid;
				} else {
					r = mid;
				}
			}
			printf("%.10lf\n", (l + r) / 2);
		}
	}

	return 0;
}

