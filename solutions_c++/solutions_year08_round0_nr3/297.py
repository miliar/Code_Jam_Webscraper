#include <iostream>
#include <cmath>

using namespace std;

const double EPS = 1e-12;
const double PI = acos(-1.0);

inline double square(double x) {
	return x * x;
}

inline bool inside(double x, double y, double r) {
	return square(x) + square(y) < square(r) - EPS;
}

inline double getX(double y, double r) {
	return sqrt(square(r) - square(y));
}

inline double arcArea(double x1, double y1, double x2, double y2, double r) {
	double cp = x1 * y2 - x2 * y1;
	return asin(cp / square(r)) / (PI + PI) * PI * square(r) - cp / 2;
}

double hitRatio(double f, double R, double t, double r, double g) {
	g -= f + f;
	r += f;
	t += f;
	if (g < EPS || R - t < EPS)
		return 1.0;
	double s = 0;
	double d = g + r + r;
	for (double x = r; inside(x, r, R - t); x += d) 
		for (double y = r; inside(x, y, R - t); y += d)  {
			if (inside(x + g, y + g, R - t))
				s += square(g);
			else {
				if (inside(x, y + g, R - t)) {
					if (inside(x + g, y, R - t)) {
						double x1 = getX(y + g, R - t);
						double y1 = getX(x + g, R - t);
						s += (y1 - y) * g + (x1 - x + g) * (y - y1 + g) / 2 + arcArea(x + g, y1, x1, y + g, R - t);
					} else {
						double x1 = getX(y, R - t);
						double x2 = getX(y + g, R - t);
						s += (x2 - x + x1 - x) * g / 2 + arcArea(x1, y, x2, y + g, R - t);
					}
				} else {
					if (inside(x + g, y, R - t)) {
						double y1 = getX(x, R - t);
						double y2 = getX(x + g, R - t);
						s += (y2 - y + y1 - y) * g / 2 + arcArea(y1, x, y2, x + g, R - t);
					} else {
						double x1 = getX(y, R - t);
						double y1 = getX(x, R - t);
						s += (x1 - x) * (y1 - y) / 2 + arcArea(x1, y, x, y1, R - t);
					}
				}
			}
		}
	return 1 - 4 * s / (PI * square(R));
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int N;
	cin >> N;
	for (int c = 1; c <= N; ++c) {
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;
		printf("Case #%d: %.6f\n", c, hitRatio(f, R, t, r, g));
	}
	return 0;
}