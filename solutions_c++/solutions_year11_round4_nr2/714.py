#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#define eps 1e-11
#define feq(x,y) (((x)-(y))<(eps))
#define fl(x,y) ((x)+(eps)<(y))
#define fle(x,y) ((x)<(y)+(eps))
typedef long long LL;
using namespace std;

template<class T> string toString(const T &x) {ostringstream sout; sout << x; return sout.str();}
int toInt(string s) {istringstream sin(s); int n; sin >> n; return n; }

int r, c, d;
int a[505][505];

int solve() {
	for (int ww = min(r, c); ww >= 3 ; --ww) {
		int w = ww / 2;
		if (ww & 1) {
			//printf("%d %d %d %d\n", w, r - w, w, c - w);
			for (int cx = w; cx < r - w; ++cx) {
				for (int cy = w; cy < c - w; ++cy) {
					//printf("center: %d %d\n", cx, cy);
					LL x = 0, y = 0;
					for (int i = cx - w; i <= cx + w; ++i) {
						for (int j = cy - w; j <= cy + w; ++j) {
							if (i == cx - w && j == cy - w) continue;
							if (i == cx - w && j == cy + w) continue;
							if (i == cx + w && j == cy - w) continue;
							if (i == cx + w && j == cy + w) continue;
							x += (i - cx) * a[i][j];
							y += (j - cy) * a[i][j];
						}
					}
					if (x == 0 && y == 0) {
						//printf("%d %d\n", cx, cy);
						return ww;
					}
				}
			}
		} else {
			for (int ccx = w; ccx <= r - w; ++ccx) {
				for (int ccy = w; ccy <= c - w; ++ccy) {
					//printf("center: %d %d\n", cx, cy);
					double cx = ccx - 0.5, cy = ccy - 0.5;
					double x = 0, y = 0;
					for (int i = ccx - w; i < ccx + w; ++i) {
						for (int j = ccy - w; j < ccy + w; ++j) {
							if (i == ccx - w && j == ccy - w) continue;
							if (i == ccx - w && j == ccy + w - 1) continue;
							if (i == ccx + w - 1 && j == ccy - w) continue;
							if (i == ccx + w - 1 && j == ccy + w - 1) continue;
							x += (i - cx) * a[i][j];
							y += (j - cy) * a[i][j];
						}
					}
					if (x == 0 && y == 0) {
						//printf("%d %d\n", cx, cy);
						return ww;
					}
				}
			}

		}
	}
	return -1;
}

int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		scanf("%d %d %d", &r, &c, &d);
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				scanf("%1d", &a[i][j]);
				a[i][j] += d;
			}
		}
		//printf("%d %d %d\n", r, c, d);
		printf("Case #%d: ", ++cas);
		int ret = solve();
		if (ret == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ret);
	}
	return 0;
}
