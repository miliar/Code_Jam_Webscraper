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

int arr[500][500];

int main(int argc, char *argv[]) {
	int T; scanf(" %d", &T);
	for (int X = 1; X <= T; ++X) {
		int R, cnt = 0, res = 0;
		int mx = 0, my = 0;
		cin >> R;
		memset(arr, 0, sizeof(arr));
		loop (i, R) {
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			--x1; --y1; --x2; --y2;
			for (int x = x1; x <= x2; ++x) {
				for (int y = y1; y <= y2; ++y) {
					if (!arr[x][y]) cnt++;
					arr[x][y] = 1;
					mx = max(mx, x);
					my = max(my, y);
				}
			}
		}
		while (cnt) {
			++res;
			for (int x = mx; x >= 0; --x) {
				for (int y = my; y >= 0; --y) {
					if (arr[x][y] == 0 && x > 0 && y > 0 && arr[x-1][y] == 1 && arr[x][y-1] == 1) {
						arr[x][y] = 1;
						++cnt;
						mx = max(mx, x);
						my = max(my, y);
					}
					if (arr[x][y] == 1 && x > 0 && y > 0 && arr[x-1][y] == 0 && arr[x][y-1] == 0) {
						arr[x][y] = 0;
						--cnt;
					}
					if (arr[x][y] == 1 && (x==0 || y == 0)) {
						arr[x][y] = 0;
						--cnt;
					}
				}
			}
		//	cout << cnt << endl;
		}

		printf("Case #%d: %d\n", X, res);
	}
	return 0;
}
