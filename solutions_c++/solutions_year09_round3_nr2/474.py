#include <cstdio>
#include <cmath>

using namespace std;

int n;
double x, y, z, vx, vy, vz;

const double eps = 1e-9;

int sgn(const double &x) {
	return (x > eps) - (x < -eps);
}

double msqrt(const double &x) {
	if (sgn(x) <= 0)
		return 0;
	return sqrt(x);
}

void calc() {
	double A = (vx * vx + vy * vy + vz * vz);
	double B = 2 * (x * vx + y * vy + z * vz);
	double C = (x * x + y * y + z * z);

	if (sgn(A) == 0) {
		printf("%.7lf %.7lf\n", msqrt(C), 0.0);
		return;
	}

	if (sgn(-B / (2 * A)) <= 0) {
		printf("%.7lf %.7lf\n", msqrt(C), 0.0);
		return;
	}

	double ans = (4 * A * C - B * B) / (4 * A);
	if (ans < 0) ans = 0;

	double anst = -B / (2 * A);
	if (anst < 0) anst = 0;
	printf("%.7lf %.7lf\n", sqrt(ans), anst);
}

int main() {
	int ca;
	scanf("%d", &ca);
	for (int T = 1; T <= ca; ++T) {
		printf("Case #%d: ", T);
		scanf("%d", &n);
		x = y = z = vx = vy = vz = 0;
		for (int i = 0; i < n; ++i) {
			double tx, ty, tz, tvx, tvy, tvz;
			scanf("%lf%lf%lf%lf%lf%lf", &tx, &ty, &tz, &tvx, &tvy, &tvz);
			x += tx;
			y += ty;
			z += tz;
			vx += tvx;
			vy += tvy;
			vz += tvz;
		}
		x /= n;
		y /= n;
		z /= n;
		vx /= n;
		vy /= n;
		vz /= n;
		calc();
	}
	return 0;
}
