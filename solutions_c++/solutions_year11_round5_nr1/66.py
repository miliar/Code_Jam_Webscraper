#include <cstdio>

int T, l, u, g;
double w, lx[100], ly[100], ux[100], uy[100], ta, lo, md, hi;

double area(double *x, double *y, int n, double tx) {
	double r = 0;
	for (int i = 0; i + 1 < n; ++i)
		if (x[i + 1] < tx)
			r += .5*(x[i + 1] - x[i])*(y[i] + y[i + 1]);
		else {
			double ty = (tx - x[i])/(x[i + 1] - x[i])*(y[i + 1] - y[i]) + y[i];
			r += .5*(tx - x[i])*(y[i] + ty);
			break;
		}
	return r;
}

double area(double x) {
	return area(ux, uy, u, x) - area(lx, ly, l, x);
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d:", r);
		scanf("%lf%d%d%d", &w, &l, &u, &g);
		for (int i = 0; i < l; ++i)
			scanf("%lf%lf", lx + i, ly + i);
		for (int i = 0; i < u; ++i)
			scanf("%lf%lf", ux + i, uy + i);
		ta = area(w);
		for (int i = 1; i < g; ++i) {
			lo = 0, hi = w;
			while (lo + 1e-10 < hi) {
				md = .5*(lo + hi);
				if (area(md) < ta*i/g)
					lo = md;
				else
					hi = md;
			}
			printf("\n%.10lf", md);
		}
		puts("");
	}
	return 0;
}
