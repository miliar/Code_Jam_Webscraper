#include <cstdio>

using namespace std;

int W, L, U;
int x[200], y[200];
int G;
double area;

double findY(double y1, double y2, double x1, double x2, double x) {
	return y1 / (x2 - x1) * (x2 - x) +
		y2 / (x2 - x1) * (x - x1);
}

double findX(double y1, double y2, double x1, double x2, double A) {
	double l = x1, u = x2;

	while ((u - l) > 1e-8) {
		double mid = (l + u) / 2;
		
		double yx = findY(y1, y2, x1, x2, mid);

		double amid = (yx + y1) * (mid - x1) / 2;
		if (amid < A) l = mid;
		else u = mid;
	}

	return l;
}

void solve() {
	int curU = 0, curL = 0;
	double curx = 0; double curarea = area;
	double cury = y[L] - y[0];

	for (int i = 0; i < G - 1; ) {
		double b, y2;
		if (x[curL + 1] < x[L + curU + 1]) {
			b = x[curL + 1];
			y2 = findY(y[L + curU], y[L + curU + 1], x[L + curU], x[L + curU + 1], b) - y[curL + 1];
		} else {
			b = x[L + curU + 1];
			y2 = y[L + curU + 1] - findY(y[curL], y[curL + 1], x[curL], x[curL + 1], b);
		}

		if ((y2 + cury) * (b - curx) / 2 > curarea) {
			double curx2 = findX(cury, y2, curx, b, curarea);
			printf("%.9lf\n", curx2); i++;

			cury = findY(cury, y2, curx, b, curx2);
			curx = curx2;
			curarea = area;
		} else {
			curarea -= (y2 + cury) * (b - curx) / 2;

			curx = b;
			cury = y2;
			if (x[curL + 1] < x[L + curU + 1]) curL++;
			else curU++;
		}
	}
}

void init() {
	scanf("%d%d%d%d", &W, &L, &U, &G);
	for (int i = 0; i < L + U; i++) {
		scanf("%d%d", &x[i], &y[i]);
	}

	area = 0;
	for (int i = 1; i < L; i++) {
		area -= (y[i - 1] + y[i]) * (x[i] - x[i - 1]) / 2.;
	}

	for (int i = L + 1; i < L + U; i++) {
		area += (y[i - 1] + y[i]) * (x[i] - x[i - 1]) / 2.;
	}

	area /= G;
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		init();
		printf("Case #%d:\n", i);
		solve();
	}
	
	return 0;
}
