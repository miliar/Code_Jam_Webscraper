#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <string>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

//#define DBG


string spam;
vector <int> a;
long long st[10000], fn[10000], sp[10000];

bool simple (long long x) {
	for (int q = 2; q * q <= x; ++q) {
		if (x % q == 0) {
			return false;
		}
	}
	return true;
}
int main() {
#ifdef DBG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int j = 0; j < t; ++j) {
		int r, c, d;
		cin >> r >> c >> d;
		vector <string> a;
		getline (cin, spam);
		int k = min(r, c);
		for (int i = 0; i < r; ++i) {
			getline (cin, spam);
			a.push_back(spam);
		}
		int ff = false;
		for (int i = k; i >= 3; --i) {
			for (int ii = 0; ii + i <= r; ++ii)
				for (int jj = 0; jj + i <= c; ++jj) {
					int x1 = ii;
					int x2 = ii + i - 1;
					int yy1 = jj;
					int yy2 = jj + i - 1;
					double xc = (x1 + x2) * 1.0 / 2;
					double yc = (yy1 + yy2) * 1.0 / 2;
					double xx1 = 0;
					double yyy1 = 0;
					for (int iii = ii; iii < ii + i; ++iii) {
						for (int jjj = jj; jjj < jj + i; ++jjj) {
							xx1 += (iii - xc) * (d + (a[iii][jjj] - '0'));
							yyy1 += (jjj - yc) * (d + (a[iii][jjj] - '0'));
						}
					}
					xx1 -= (ii - xc) * (d + (a[ii][jj] - '0'));
					xx1 -= (ii - xc) * (d + a[ii][jj + i - 1] - '0');
					xx1 -= (ii + i - 1 - xc) * (d + (a[ii + i - 1][jj] - '0'));
					xx1 -= (ii + i - 1  - xc) * (d + a[ii + i - 1][jj + i - 1] - '0');
					yyy1 -= (jj - yc) * (d + (a[ii][jj] - '0'));
					yyy1 -= (jj + i - 1 - yc) * (d + a[ii][jj + i - 1] - '0');
					yyy1 -= (jj - yc) * (d + (a[ii + i - 1][jj] - '0'));
					yyy1 -= (jj + i - 1 - yc) * (d + a[ii + i - 1][jj + i - 1] - '0');
					if (xx1 == 0 && yyy1 == 0 && !ff)  {
						ff = true;
						cout << "Case #" << j + 1 << ": " << i << endl;
					}
				}
		}
		if (!ff) {
			cout << "Case #" << j + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}