#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define Size(a) ((int)a.size())
#define Sqr(a) ((a) * (a))

struct SPoint {
	double x, y, r;
	void scan() {
		scanf("%lf %lf %lf", &x, &y, &r);
	}
	double Dist(double xx, double yy) {
		return sqrt(Sqr(x - xx) + Sqr(y - yy));
	}
} p[100];
bool Eq(SPoint &p1, SPoint &p2, int k, double r, double &x, double &y) {
	double l = sqrt(Sqr(p1.x - p2.x) + Sqr(p1.y - p2.y));
	if (l < 1e-9) {
		x = p1.x;
		y = p1.y;
		return !k;
	}
	if (l > r + r - p1.r - p2.r) return false;
	double r1 = r - p1.r, r2 = r - p2.r;
	double h = sqrt(Sqr(r2) - Sqr(Sqr(r1) - Sqr(l) - Sqr(r2)) / Sqr(2 * l));
	double kl = sqrt(Sqr(r1) - Sqr(h));
	double a = p1.y - p2.y, b = p2.x - p1.x, d = sqrt(Sqr(a) + Sqr(b));
	a /= d;
	b /= d;
	x = p1.x + (p2.x - p1.x) * kl / l;
	y = p1.y + (p2.y - p1.y) * kl / l;
	if (k) {
		x += a * h;
		y += b * h;
	} else {
		x -= a * h;
		y -= b * h;
	}
	return true;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);
		int n;
		scanf("%d", &n);
		double d = 1, u = 10000;
		for (int i = 0; i < n; i++) {
			p[i].scan();
			d = max(d, p[i].r);
		}
		for (int __i = 0; __i < 50; __i++) {
			double r = (d + u) / 2.0;
			for (int i1 = 0; i1 < n; i1++) {
				for (int j1 = i1; j1 < n; j1++) {
					for (int k1 = 0; k1 < 2; k1++) {
						double x1 = 0, y1 = 0;
						if (!Eq(p[i1], p[j1], k1, r, x1, y1)) continue;
						for (int i2 = i1; i2 < n; i2++) {
							for (int j2 = i2 ; j2 < n; j2++) { 
								for (int k2 = 0; k2 < n; k2++) {
									double x2 = 0, y2 = 0;
									if (!Eq(p[i2], p[j2], k2, r, x2, y2)) continue;
									bool good = true;
									for (int j = 0; j < n; j++) {
										if (p[j].Dist(x1, y1) > r - p[j].r + 1e-9 && p[j].Dist(x2, y2) > r - p[j].r + 1e-9) {
											good = false;
											break;
										}
									}
									if (good) {
										goto ok;
									}
								}
							}
						}
					}
				}
			}

			d = r;
			continue;
ok:
			u = r;
		}
		printf("%.10lf\n", u);
	}
	return 0;
}