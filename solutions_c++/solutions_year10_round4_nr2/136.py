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

const int MAXP = 12;

int m[1 << MAXP];
int c[MAXP][1 << MAXP];
i64 d[MAXP][1 << MAXP][MAXP + 1];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int p; scanf("%d", &p);
		for (int i = 0; i < 1 << p; ++i) {
			scanf("%d", &m[i]);
			for (int j = 0; j <= p; ++j) {
				d[0][i][j] = 1000000000000000;
			}
			d[0][i][p - m[i]] = 0;
		}
		for (int i = 0; i < p; ++i) {
			for (int j = 0; j < 1 << (p - 1 - i); ++j) {
				scanf("%d", &c[i][j]);
			}
		}
		for (int i = 0; i < p; ++i) {
			for (int j = 0; j < 1 << (p - i); ++j) {
				for (int k = 0; k <= p; ++k) {
					d[i + 1][j][k] = 1000000000000000;
				}
			}
			for (int j = 0; j < 1 << (p - i); j += 2) {
				for (int k = 0; k <= p; ++k) {
					for (int l = 0; l <= p; ++l) {
						d[i + 1][j >> 1][max(k, l)] = min(d[i + 1][j >> 1][max(k, l)], d[i][j][k] + d[i][j + 1][l]);
						if (k || l) {
							d[i + 1][j >> 1][max(k - 1, l - 1)] = min(d[i + 1][j >> 1][max(k - 1, l - 1)], d[i][j][k] + d[i][j + 1][l] + c[i][j >> 1]);
						}
					}
				}
			}
/*			for (int j = 0; j < 1 << (p - i); ++j) {
				for (int k = 0; k <= p; ++k) {
				if (d[i][j][k] != 1000000000000000) cout << i << " "<< j << " " << k << " " << d[i][j][k] << endl;
				}
			}*/
		}
		i64 result = d[p][0][0];
		printf("Case #%d: %lld\n", tt + 1, result);
	}
	return 0;
}
