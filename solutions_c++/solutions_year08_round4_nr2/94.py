#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

#define fn(i, n)	for(int i = 0; i < (n); ++i)
#define eps			1e-6
#define eq(a, b)	(fabs((a) - (b)) < eps)

int n, m, ss;

int main() {
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);

	int T;
	cin >> T;
	fn(test, T) {
		cin >> n >> m >> ss;
		int x2, y2, x3, y3;
		double a, b, c, p, S, s;
		bool ok = false;
		s = ss;
		cout << "Case #" << test+1 << ": ";
		fn(x2, n+1) {
			fn(y2, m+1) {
				fn(x3, n+1) {
					fn(y3, m+1) {
						a = sqrt((double)x3*x3 + y3*y3);
						b = sqrt((double)x2*x2 + y2*y2);
						c = sqrt((double)(x2-x3)*(x2-x3) + (y2-y3)*(y2-y3));
						p = (a + b + c) / 2.0;
						S = 2 * sqrt(p*(p-a)*(p-b)*(p-c));
						if (eq(S, s)) {
							ok = true;
							cout << "0 0 " << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3;
							x2 = 100000000;
							x3 = 100000000;
							y2 = 100000000;
							y3 = 100000000;
						}
					}
				}
			}
		}
		if (!ok) cout << "IMPOSSIBLE";
		cout << endl;
	}

	return 0;
}
