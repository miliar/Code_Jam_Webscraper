#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <map>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int geti() { int n; scanf("%d", &n); return n; }
long double getd() { long double n; scanf("%L", &n); return n; }

#define i(n) for (int i = 0; i < (n); i++)
#define j(n) for (int j = 0; j < (n); j++)

char line[100];

int N, T;
long double xi, yi, zi, vx, vy, vz;
long double dmin, tmin;

int flip(int a) {
	if (a == 0) {
		return 1;
	} else if (a == 1) {
		return 0;
	} else {
		return a;
	}
}

void setup() {
	xi = yi = zi = vx = vy = vz = 0;
	N = geti();
	int xs = 0;
	int ys = 0;
	int zs = 0;
	int vxs = 0;
	int vys = 0;
	int vzs = 0;
	i(N) {
		xs += geti();
		ys += geti();
		zs += geti();
		vxs += geti();
		vys += geti();
		vzs += geti();
	}

	xi = (long double)xs / (long double)N;
	yi = (long double)ys / (long double)N;
	zi = (long double)zs / (long double)N;
	vx = (long double)vxs / (long double)N;
	vy = (long double)vys / (long double)N;
	vz = (long double)vzs / (long double)N;

}

long double x(long double t) {
	return vx * t + xi;
}
long double y(long double t) {
	return vy * t + yi;
}
long double z(long double t) {
	return vz * t + zi;
}

long double d(long double t) {
	long double xt = x(t);
	long double yt = y(t);
	long double zt = z(t);
	return sqrt(xt * xt + yt * yt + zt * zt);
}

void doIt() {
	long double a = vx*vx + vy*vy + vz*vz;
	long double b = vx*xi + vy*yi + vz*zi;
	long double aT = 0;
	if (a != 0) {
		aT = (-b)/a;
	}
	if (aT < 0) aT = 0;
	tmin = aT;
	dmin = d(tmin);
}

int Case;

void print() {
	printf("Case #%d: %Lf %Lf\n", Case, dmin, tmin);
}

int main() {

	//freopen("B-test.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	T = geti();

	getc(stdin);

	for (Case = 1; Case <= T; Case++) {
		setup();
		doIt();
		print();
	}
}