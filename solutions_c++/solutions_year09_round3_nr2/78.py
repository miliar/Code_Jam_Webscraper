#include <stdio.h>
#include <math.h>
#include <complex>

/*
#define re real()
#define im imag()
typedef complex<double> pt;
typedef complex<pt> ln;

double operator&(pt a, pt b) { return (conj(a) * b).im; }
double operator^(pt a, pt b) { return (conj(a) * b).re; }
bool operator <(pt a, pt b) { return a.re != b.re ? a.re < b.re : a.im < b.im; }
pt operator~(ln a) { return a.im - a.re; }
double abs(ln a) {return abs(~a); }

pt proj(ln l, pt p) { return l.re + (p - l.re ^ ~l) / norm(~l) * ~l; }
bool intsp(ln s, pt p)
 { return abs(s.re - p) + abs(s.im - p) - abs(~s) <= EPS; }
db distsp(ln s, pt p) { pt r = proj(s, p);
 return intsp(s, r) ? abs(r - p) : min(abs(s.re - p), abs(s.im - p)); }
 */

void solve() {
	int n; scanf("%d", &n);
	double a[6] = {0, 0, 0, 0, 0, 0};
	for (int i = 0; i < n; i++)
	 for (int j = 0; j < 6; j++) {
		int d; scanf("%d", &d);
		a[j] += d / (double)n;
	}
	a[0] = -a[0]; a[1] = -a[1]; a[2] = -a[2];
	double d1 = a[0] * a[0] + a[1] * a[1] + a[2] * a[2];
	double d2 = a[0] * a[3] + a[1] * a[4] + a[2] * a[5];
	double d3 = a[3] * a[3] + a[4] * a[4] + a[5] * a[5];
	if (fabs(d3) < 1e-9 || d2 < 1e-9) {
		printf("%.8lf %.8lf\n", sqrt(d1), 0.0);
		return;
	}
	d2 /= sqrt(d3);
	if (fabs(d1 - d2 * d2) < 1e-9) {
		printf("%.8lf %.8lf\n", 0.0, d2 / sqrt(d3));
		return;
	}
	printf("%.8lf %.8lf\n", sqrt(d1 - d2 * d2), d2 / sqrt(d3));
}

int main() {
	int n; scanf("%d", &n);
	for (int case_x = 1; case_x <= n; case_x++)
	 printf("Case #%d: ", case_x), solve();
	return 0;
}
