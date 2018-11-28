#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

double eps = 1e-6;

inline int sig(double k) {
	return k < -eps ? -1 : k > eps;
}

int ps[1001000];
int pn;

int d, c;

int check(double t) {
	double r = ps[0] - t;
	for (int i = 1; i < pn; i++) {
		double tmp = r + d;
		if (sig(ps[i] - tmp) < 0) {
			if (sig((double)ps[i] + t - tmp) < 0) 
				return 0;
			r = tmp;
		} else {
			double xt = t;
			if (sig(xt - ((double)ps[i] - tmp)) > 0) xt = (double)ps[i] - tmp;
			r = (double)ps[i] - xt;
		}
	}
	return 1;
}

double work() {
	int cnt = 0;
	double right = 1e20;
	double left = 0;
	double mid;
	while (sig(right - left) > 0) {
		cnt++;
		if (cnt > 100) break;
		mid = (right + left + eps) / 2.0;
		if (check(mid)) right = mid;
		else left = mid;
	}
	return right;
}

int main() {
	int T;
	scanf("%d", &T);
	int i, j, k;
	int p, v;
	int cas = 1;
	while (T--) {
		scanf("%d%d", &c, &d);
		pn = 0;
		for (i = 0; i < c; i++) {
			scanf("%d%d", &p, &v);
			for (j = 1; j <= v; j++)
				ps[pn++] = p;
		}
		sort(ps, ps + pn);
		printf("Case #%d: %.7f\n", cas++, work());
	}
	return 0;
}