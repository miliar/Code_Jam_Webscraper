#include <iostream>
using namespace std;

int i, j, k, n, m;
int x1, y1, x2, y2, x3, y3, x, y, z, d;
int t, T;
int s, r;

int ab(int x) {
	return x >= 0 ? x : -x;
}

int maax(int x, int y) {
	return x > y ? x : y;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n >> m >> s;
		
		x1 = 0;
		y1 = 0;
		r = 0;
		for (x2 = -n; x2 <= n; x2 ++) {
		for (y2 = -m; y2 <= m; y2 ++) {
			if (x1==x2&&y1==y2) continue;
		for (x3 = maax(-n, x2 - n); x3 <= n && x3 <= x2 + n; x3 ++) {
		for (y3 = maax(-m, y2 - m); y3 <= m && y3 <= y2 + m; y3 ++) {
			if ( (x1==x2&&y1==y2) || (x1==x3&&y1==y3) || (x2==x3&&y2==y3) ) {
				continue;
			}
			d = ab(x2 * y3 - y2 * x3);
			if (d == s) {
				r = 1;
				break;
			}
		}
		if (r == 1) break;
		}
		if (r == 1) break;
		}
		if (r == 1) break;
		}
		cout << "Case #" << t << ": ";
		if (r == 0) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		} 
		if (x2 < 0) {
			d = -x2;
			x1 += d;
			x2 += d;
			x3 += d;
		}
		if (x3 < 0) {
			d = -x3;
			x1 += d;
			x2 += d;
			x3 += d;
		}
		if (y2 < 0) {
			d = -y2;
			y1 += d;
			y2 += d;
			y3 += d;
		}
		if (y3 < 0) {
			d = -y3;
			y1 += d;
			y2 += d;
			y3 += d;
		}
		cout << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << ' ' << endl;
	}
	return 0;
}
			


