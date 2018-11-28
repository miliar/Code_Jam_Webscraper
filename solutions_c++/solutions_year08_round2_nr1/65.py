#include <iostream>
#include <set>
using namespace std;
#define N 105
int T, t, i, j, k, n;

long long a, b, c, d, m;
long long x0, y0, x, y, res;
long long a1, a2, a3, b1, b2, b3;

struct pt {
	long long x, y;
	friend int operator < (pt x, pt y) {
		if (x.x != y.x) {
			return x.x < y.x;
		}
		return x.y < y.y;
	}
};

set <pt> s;
pt p[N], tp;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	cin >> T;
	for (t = 1; t  <= T; t ++) {
		cin >> n;
		memset(p, 0, sizeof(p));
		s.clear();
		cin >> a >> b >> c >> d >> x0 >> y0 >> m;
		i = 0;
		p[i].x = x0;
		p[i].y = y0;
		x = x0;
		y = y0;
		s.insert(p[i]);
		for (i = 1; i < n; i ++) {
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			p[i].x = x;
			p[i].y = y;
		}

		res = 0;
		for (i = 0; i < n; i ++) {
			for (j = i + 1; j < n; j ++) {
				for (k = j + 1; k < n; k ++) {
					x = (p[i].x + p[j].x + p[k].x);
					y = (p[i].y + p[j].y + p[k].y);
					if (x % 3 == 0 && y % 3 == 0) {
						res ++;
					}
				}
			}
		}

		cout << "Case #" << t << ": " << res << endl;
	}
	return 0;
}



			


