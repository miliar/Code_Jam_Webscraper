#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <complex>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef complex<long double> point;

long double det(const point& p1, const point& p2) {
	return (conj(p1) * p2).imag();
}

long double dot(const point& p1, const point& p2) {
	return (conj(p1) * p2).real();
}

long double size(const point& c1, long double r1, const point& c2, long double r2) {
	long double d = abs(c1 - c2);
	if(d - abs(r1 - r2) <= 0) return 0;
	long double x = (d * d + r1 * r1 - r2 * r2) / (2 * d);
	long double t1 = acos(x / r1), t2 = acos((d - x) / r2);
	return r1 * r1 * t1 + r2 * r2 * t2 - d * r1 * sin(t1);
}

point ps[2];
point qs[20];

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		printf("Case #%d:", t + 1);
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; ++i) cin >> ps[i].real() >> ps[i].imag();
		for(int i = 0; i < m; ++i) cin >> qs[i].real() >> qs[i].imag();
		for(int i = 0; i < m; ++i) {
			printf(" %.10f", (double)size(ps[0], abs(ps[0] - qs[i]), ps[1], abs(ps[1] - qs[i])));
		}
		puts("");
	}
	return 0;
}
