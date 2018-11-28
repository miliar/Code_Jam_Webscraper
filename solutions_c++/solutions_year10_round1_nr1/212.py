/* Rajat Goel (C++) */
#include <algorithm>
#include <iostream>
#include <iterator>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
const int    INF =     INT_MAX/2-1;
const LL    LINF =     LLONG_MAX/2-1;
const LD     EPS =     1e-7;
#define loop(i, n)     for (int i = 0; i < int(n); ++i)
#define foreach(i, a)  for (typeof((a).begin()) i = (a).begin();i != (a).end(); ++i)
inline int fCMP(LD x, LD y = 0, LD tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

bool check(vector<string> &r, int i, int j, int k, int dx, int dy, char ch) {
	loop (t, k) {
		if (r[i+dx*t][j+dy*t] != ch) return false;
	}
	return true;
}

int main(int argc, char *argv[]) {
	int T; scanf(" %d", &T);
	for (int X = 1; X <= T; ++X) {
		int n, k;
		scanf(" %d %d", &n, &k);
		vector<string> arr(n);
		loop (i, n) cin >> arr[i];

		vector<string> rotated(n, string(n, '.'));
		loop (i, n) loop (j, n) {
			rotated[i][j] = arr[n-1-j][i];
		}
		
		loop (j, n) for (int i = n-1; i >= 0; --i) {
			int _i = i;
			while (_i + 1 < n && rotated[_i+1][j] == '.') {
				swap(rotated[_i+1][j], rotated[_i][j]);
				_i++;
			}
		}
		
		bool red = false, blue = false;
		loop (i, n) loop (j, n) {
			if (i + k - 1 < n) {
				red |= check(rotated, i, j, k, 1, 0, 'R');
				blue |= check(rotated, i, j, k, 1, 0, 'B');
			}
			if (j + k - 1 < n) {
				red |= check(rotated, i, j, k, 0, 1, 'R');
				blue |= check(rotated, i, j, k, 0, 1, 'B');
			}
			if (i + k - 1 < n && j - k - 1 < n) {
				red |= check(rotated, i, j, k, 1, -1, 'R');
				blue |= check(rotated, i, j, k, 1, -1, 'B');
			}
			if (i + k - 1 < n && j + k - 1 < n) {
				red |= check(rotated, i, j, k, 1, 1, 'R');
				blue |= check(rotated, i, j, k, 1, 1, 'B');	
			}
		}

		string ans = "Neither";
		if (red && blue) {
			ans = "Both";
		} else if (red && !blue) {
			ans = "Red";
		} else if (!red && blue) {
			ans = "Blue";
		}

		printf("Case #%d: %s\n", X, ans.c_str());
	}
	return 0;
}
