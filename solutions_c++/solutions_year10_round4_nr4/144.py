#include <iostream>
#include <cstdio>
#include <vector>
#include <complex>
using namespace std;

typedef long double num;
typedef complex<double> point;
typedef vector<point> poly;

num shared(num r1, num r2, num oy) {
	num x,y,a,b,acc;
	y = (oy*oy + r2*r2 - r1*r1) / (2 * oy);
	x = sqrt(r2 * r2 - y * y);
	acc = x * oy;
	a = acos(y / r2);
	b = acos((oy - y) / r1);
	return (r2 * r2 * a + r1 * r1 * b - acc);
}

num solve(poly & p, point buck) {
	return shared(abs(p[0] - buck), abs(p[1] - buck), abs(p[1] - p[0]));
}

int main(void) {
	int i, j, t, n, m;
	num x, y;
	poly p;
	for (cin >> t, i = 1; i <= t; ++i) {
		cin >> n >> m;
		p.resize(n);
		for (j = 0; j < n; ++j) {
			cin >> x >> y;
			p[j] = point(x, y);
		}
		cout << "Case #" << i << ":";
		for (j = 0; j < m; ++j) {
			cin >> x >> y;
			printf(" %.7Lf", solve(p, point(x, y)));
		}
		cout << endl;
		p.clear();
	}
	return 0;
}
