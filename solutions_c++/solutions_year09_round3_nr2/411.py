#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

const double eps = 1.0e-9;

inline int sgn(const double &a) {
	return (a > eps ? 1 : (a < -eps ? -1 : 0));
}//sgn

struct point {
	double x, y, z;

	point(const double &_x, const double &_y, const double &_z) : 
		x(_x), y(_y), z(_z) {}
	point() {}

	point operator + (const point &p) const {
		return point(x + p.x, y + p.y, z + p.z);
	}
	point operator - (const point &p) const {
		return point(x - p.x, y - p.y, z - p.z);
	}
	point operator * (const double &a) const {
		return point(x * a, y * a, z * a);
	}
	point operator ^ (const point &p) const {
		return point(y * p.z - z * p.y, z * p.x - x * p.z, x * p.y - y * p.x);
	}
	double operator * (const point &p) const {
		return (x * p.x + y * p.y + z * p.z);
	}
	point trunc(double a) const {
		//assert(sgn(len()) > 0);
		a /= len();
		return point(x * a, y * a, z * a);
	}
	double len2() const {
		return (x * x + y * y + z * z);
	}
	double len() const {
		return sqrt(x * x + y * y + z * z);
	}

	void read() {
		scanf("%lf %lf %lf", &x, &y, &z);
	}
	void print() const {
		printf("%lf %lf %lf\n", x, y, z);
	}
};

point cross(const point &a, const point &b, const point &c) {
	return (b - a) ^ (c - a);
}//cross

int npoint;
point pos[505], vel[505];

void solve() {
	point ctr(0.0, 0.0, 0.0), vctr(0.0, 0.0, 0.0);

	for (int i = 0; i < npoint; i++) {
		ctr = ctr + pos[i];
		vctr = vctr + vel[i];
	}

	ctr = ctr * (1.0 / npoint);
	vctr = vctr * (1.0 / npoint);

	double dmin, tmin;
	if (sgn(ctr.x) == 0 && sgn(ctr.y == 0) && sgn(ctr.z) == 0) {
		dmin = 0.0; tmin = 0.0;
	}
	else if (sgn(vctr.x) == 0 && sgn(vctr.y) == 0 && sgn(vctr.z) == 0) {
		dmin = ctr.len(); tmin = 0.0;
	}
	else {
		double prj = (ctr * vctr) / vctr.len();
		if (sgn(prj) >= 0) {
			dmin = ctr.len(); tmin = 0.0;
		}
		else {
			//point h = ctr + vctr.trunc(-prj);
			dmin = ctr.len2() - prj * prj;
			if (sgn(dmin) <= 0) dmin = 0.0;
			else dmin = sqrt(dmin);
			tmin = (-prj) / vctr.len();
		}
	}
	printf("%.8lf %.8lf\n", dmin, tmin);
}//solve

int main() {
	int nCase;

	scanf("%d", &nCase);
	for (int t = 1; t <= nCase; t++) {
		scanf("%d", &npoint);
		for (int i = 0; i < npoint; i++) {
			pos[i].read(); vel[i].read();
		}

		printf("Case #%d: ", t);
		solve();
	}
}
