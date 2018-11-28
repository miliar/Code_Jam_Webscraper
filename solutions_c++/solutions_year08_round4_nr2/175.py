#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define FORC( it, V ) for( __typeof( (V).begin() ) it = (V).begin(); it != (V).end(); ++it )
#define SZ(a) a.size()

int n, m, s;

void read_data() {
	cin >> n >> m >> s;
}

void check(int &x1, int &y1, int &x2, int &y2, int &x3, int &y3) {
	int S = (x1 + x2) * (y1 - y2) + (x2 + x3) * (y2 - y3) + (x3 + x1) * (y3 - y1);
	S = abs(S);
	assert(S == s);
	assert(0 <= x1 && x1 <= n);
	assert(0 <= x2 && x2 <= n);
	assert(0 <= x3 && x3 <= n);

	assert(0 <= y1 && y1 <= m);
	assert(0 <= y2 && y2 <= m);
	assert(0 <= y3 && y3 <= m);
}

bool ok(int &x1, int &y1, int &x2, int &y2, int &x3, int &y3) {
	int minx = 0;
	minx <?= x1;
	minx <?= x2;
	minx <?= x3;
	int maxx = 0;
	maxx >?= x1;
	maxx >?= x2;
	maxx >?= x3;
	
	if (maxx - minx > n) {
		return false;
	}
	x1 -= minx;
	x2 -= minx;
	x3 -= minx;
	return true;
} 

void process() {
	if (s > m * n) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	int x1 = 0;
	int y1 = 0;
	//case 1
	FOR(x2, 1, n) {
		int y2 = 0;
		int len = x2 - x1;
		if (s % len != 0) continue;
		int h = s / len;
		if (h <= m) {
			int x3 = 0;
			int y3 = h;
			cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
			check(x1, y1, x2, y2, x3, y3);
			return;
		}
	}
	//case 2
	FOR(y2, 1, m) FOR(x2, -n, n) {
		FOR(y3, y2, m) {
			int tmp;
		    tmp = x2 * y3 - s;
		    if (abs(tmp) % y2 == 0) {
				int x3 = tmp / y2;
				if (ok(x1, y1, x2, y2, x3, y3)) {
					cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
					check(x1, y1, x2, y2, x3, y3);
					return;					
				}
			}

		    tmp = x2 * y3 + s;
		    if (abs(tmp) % y2 == 0) {
				int x3 = tmp / y2;
				if (ok(x1, y1, x2, y2, x3, y3)) {
					cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
					check(x1, y1, x2, y2, x3, y3);
					return;					
				}				
			}

		}
	}
	cout << "IMPOSSIBLE" << endl;
}

int main() {
	int test;
	cin >> test;
	FOR(i, 1, test) {
		cout << "Case #" << i << ": ";
		read_data();
		process();
	}
	return 0;
};

