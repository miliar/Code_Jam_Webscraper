#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

#define abs(x) ((x) < 0 ? (-(x)) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

#define mp make_pair
#define pb push_back

typedef long long i64;

const int MAXN = 200;

int a[MAXN][MAXN];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int r; scanf("%d", &r);
		memset(a, 0, sizeof(a));
		int n = 1, m = 1;
		while (r--) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			if (x1 > x2) x1 ^= x2, x2 ^= x1, x1 ^= x2;
			if (y1 > y2) y1 ^= y2, y2 ^= y1, y1 ^= y2;
			for (int i = y1; i <= y2; ++i) {
				for (int j = x1; j <= x2; ++j) {
					a[i - 1][j - 1] = 1;
				}
			}
			n = max(n, y2 + 1);
			m = max(m, x2 + 1);
		}
		int result = -1;
		bool f = true;
		while (f) {
/*			int k = result & 1;
			int l = (result + 1) & 1;
			memset(a[(result + 1) & 1], 0, sizeof(a));*/
			f = false;
/*			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < m; ++j) {
					cout << a[i][j];
				}
				cout << endl;
			}
			cout << endl;
			cout << endl;*/
			++result;
			for (int i = n - 1; i >= 0; --i) {
				for (int j = m - 1; j >= 0; --j) {
					if (!a[i][j]) {
						if (i && j && a[i - 1][j] && a[i][j - 1]) {
							a[i][j] = 1;
						}
					} else {
						f = true;
						if ((!i || !a[i - 1][j]) && (!j || !a[i][j - 1])) {
							a[i][j] = 0;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", tt + 1, result);
	}
	return 0;
}
