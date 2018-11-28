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

bool u[1000][1000];
int d[1000][1000];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int h, w, r;
		scanf("%d %d %d", &h, &w, &r);
		memset(u, 0, sizeof(u));
		memset(d, 0, sizeof(d));
		for (int i = 0; i < r; ++i) {
			int x, y; scanf("%d %d", &x, &y);
			--x; --y; u[x][y] = true;
		}
		memset(d, 0, sizeof(d));
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) if (!u[i][j]) {
				if (!i && !j) d[i][j] = 1;
				else {
					d[i][j] = 0;
					if ((i >= 2) && (j >= 1) && (d[i - 2][j - 1] > 0)) d[i][j] += d[i - 2][j - 1];
					if ((i >= 1) && (j >= 2) && (d[i - 1][j - 2] > 0)) {
						d[i][j] += d[i - 1][j - 2];
					}
					d[i][j] %= 10007;
				}
			}
		}
		
		printf("Case #%d: %d\n", tt + 1, d[h - 1][w - 1]);
	}
	return 0;
}
