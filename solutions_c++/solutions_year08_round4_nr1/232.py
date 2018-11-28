#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <string>

using namespace std;

const int MAXN = 100000;

int g[MAXN], c[MAXN];
int d[MAXN][2];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n, x; scanf("%d %d", &n, &x);
		for (int i = 0; i < (n - 1) / 2; ++i) {
			scanf("%d %d", &g[i], &c[i]);
		}
		for (int i = (n - 1) / 2; i < n; ++i) {
			int y;
			scanf("%d", &y);
			d[i][y] = 0;
			d[i][1 - y] = -1;
		}
		for (int i = (n - 1) / 2 - 1; i >= 0; --i) {
			int l = (i << 1) + 1, r = l + 1;
			d[i][0] = d[i][1] = -1;
			for (int a = 0; a < 2; ++a) if (d[l][a] != -1) {
				for (int b = 0; b < 2; ++b) if (d[r][b] != -1) {
					int c = a & b;
					if ((g[i] == 1) || (::c[i] == 1)) {
						if ((d[i][c] == -1) || (d[i][c] > d[l][a] + d[r][b] + (g[i] != 1))) {
							d[i][c] = d[l][a] + d[r][b] + (g[i] != 1);
						}
					}
					c = a | b;
					if ((g[i] == 0) || (::c[i] == 1)) {
						if ((d[i][c] == -1) || (d[i][c] > d[l][a] + d[r][b] + (g[i] != 0))) {
							d[i][c] = d[l][a] + d[r][b] + (g[i] != 0);
						}
					}
				}
			}
		}
		printf("Case #%d: ", tt + 1);
		if (d[0][x] == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", d[0][x]);
	}
	return 0;
}
