#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <cassert>
#include <algorithm>
#include <cmath>
using namespace std;

double p[10][3];

#define sqr(x) ((x)*(x))

int main() {
	freopen("inputd.txt", "r", stdin);
	freopen("outputd.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt) {
		int n;
		cin >> n;
		assert(n <= 3);
		if (n > 3) continue;
		cout << "Case #" << tt << ": " << flush;
		for (int i = 0; i < n; ++i) {
			cin >> p[i][0] >> p[i][1] >> p[i][2];
		}
		double ans = 1 << 20;
		if (n == 3)  {
			{ 
				double l1 = p[0][2];
				double l2 = p[1][2] + p[2][2] + sqrt(sqr(p[1][0] - p[2][0]) + sqr(p[1][1] - p[2][1]));
				double res = max(l1, l2 * 0.5);
				ans = min(ans, res);
			}
			{ 
				double l1 = p[1][2];
				double l2 = p[0][2] + p[2][2] + sqrt(sqr(p[0][0] - p[2][0]) + sqr(p[0][1] - p[2][1]));
				double res = max(l1, l2 * 0.5);
				ans = min(ans, res);
			}
			{ 
				double l1 = p[2][2];
				double l2 = p[1][2] + p[0][2] + sqrt(sqr(p[1][0] - p[0][0]) + sqr(p[1][1] - p[0][1]));
				double res = max(l1, l2 * 0.5);
				ans = min(ans, res);
			}
		}
		else if (n == 2) {
			ans = max(p[0][2], p[1][2]);
		}
		else if (n == 1) {
			ans = p[0][2];
		}
		
		printf("%.6lf\n", ans); 
	
	}
	return 0;
}