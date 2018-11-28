#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>

using namespace std;

const double PI = 2 * acos(0.0);

int N;
double f, R, t, r, g;
double sum, x, y;

double S(double a, double b, double c)
{
	double p;
	
	p = (a + b + c) / 2.0;
	
	return (sqrt(p * (p - a) * (p - b) * (p - c)));
}

double ff(double len)
{
	double cosa, ang, ans;
	
	cosa = (2.0 * (R - t) * (R - t) - len * len) / (2.0 * (R - t) * (R - t));
	ang = acos(cosa);
	ans = (R - t) * (R - t) * ang / 2.0;
	
	return (ans - S(R - t, R - t, len));
}

double done(double x, double y)
{
	double ans;
	double x1, y1, x2, y2;
	
	if ((x + g) * (x + g) + (y + g) * (y + g) <= (R - t) * (R - t))
		ans = g * g;
	else {
		if (x * x + (y + g) * (y + g) <= (R - t) * (R - t)) {
			y1 = y + g;
			x1 = sqrt((R - t) * (R - t) - y1 * y1);
		} else {
			x1 = x;
			y1 = sqrt((R - t) * (R - t) - x1 * x1);
		}
		
		if ((x + g) * (x + g) + y * y <= (R - t) * (R - t)) {
			x2 = x + g;
			y2 = sqrt((R - t) * (R - t) - x2 * x2);
		} else {
			y2 = y;
			x2 = sqrt((R - t) * (R - t) - y2 * y2);
		}
		
		if (fabs(y1 - y - g) < 1e-6 && fabs(x2 - x - g) < 1e-6) {
			ans = g * (x1 - x);
			ans += (y2 - y + g) * (x2 - x1) / 2.0;
			ans += ff(sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
		} else if (fabs(y1 - y - g) < 1e-6 && fabs(y2 - y) < 1e-6) {
			ans = g * (x1 - x);
			ans += g * (x2 - x1) / 2.0;
			ans += ff(sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
		} else if (fabs(x1 - x) < 1e-6 && fabs(y2 - y) < 1e-6) {
			ans = (y1 - y) * (x2 - x) / 2.0;
			ans += ff(sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
		}
	}
	
	if (fabs(x - y) < 1e-6)
		return (ans / 2.0);
	else
		return (ans);
}

int main()
{
	int i;
	
	freopen("C.output", "w", stdout);
	
	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		t += f;
		r += f;
		g -= 2 * f;
		sum = 0.0;
		
		if (g > 0) {
			for (x = r; x < R - t; x += g + 2 * r)
				for (y = r; y < R - t && y <= x; y += g + 2 * r)
					if (x * x + y * y < (R - t) * (R - t))
						sum += done(x, y);
		}
		
		printf("Case #%d: %.6lf\n", i + 1, 1 - 8.0 * sum / (PI * R * R));
	}
	
	return (0);
}
