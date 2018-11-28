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

char s[100][100];
int d[20][1 << 12];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n, m; scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%s", s[i]);
		}
		memset(d, ~0, sizeof(d));
		d[0][0] = 0;
		for (int i = 0; i < n; ++i) {
			int x = 0;
			for (int j = 0; j < m; ++j) {
				if (s[i][j] == 'x') x |= 1 << j;
			}
			for (int j = 0; j < 1 << m; ++j) if (d[i][j] != -1) {
				for (int k = 0; k < 1 << m; ++k) {
					if (k & x) continue;
					bool f = true;
					int l = 0;
					for (int t = 0; t < m; ++t) {
						if ((t < m - 1) && (k & (1 << t)) && (k & (1 << (t + 1)))) {
							f = false;
							break;
						}
						if (k & (1 << t)) {++l;
							if (((t < m - 1) && (j & (1 << (t + 1)))) || (t && (j & (1 << (t - 1))))) {
								f = false;
								break;
							}
						}
					}
					if (!f) continue;
//					cout << j << " " << k << endl;
					d[i + 1][k] = max(d[i + 1][k], d[i][j] + l);
//					cout << d[i][j] << " " << l << " " << i + 1 << " " << k << " " << d[i + 1][k] << endl;
				}
			}
		}
		int result = 0;
		for (int j = 0; j < 1 << m; ++j) if (d[n][j] != -1) {
			result = max(result, d[n][j]);
		}
		printf("Case #%d: %d\n", tt + 1, result);
	}
	return 0;
}
