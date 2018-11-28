#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define pb push_back
#define mp make_pair

#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define abs(x) ((x) < 0 ? (-(x)) : (x))

typedef double dbl;
typedef long double ldbl;
typedef long long i64;

const int MAXN = 200;

const int dd[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int w[MAXN][MAXN];

struct V {
	int p, r;
} v[MAXN * MAXN];
int ch[MAXN * MAXN];

int getp(int x) {
	if (x != v[x].p) v[x].p = getp(v[x].p);
	return v[x].p;
}

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n, m; scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", &w[i][j]);
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				int x = i * m + j;
				v[x].p = x;
				v[x].r = 0;
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				int x = -1, y = -1, l = w[i][j];
				for (int k = 0; k < 4; ++k) {
					int xx = i + dd[k][0], yy = j + dd[k][1];
					if ((xx >= 0) && (xx < n) && (yy >= 0) && (yy < m) && (w[xx][yy] < l)) {
						x = xx, y = yy, l = w[xx][yy];
					}
				}
				if (x == -1) continue;
				int a = getp(i * m + j), b = getp(x * m + y);
				if (a != b) {
					if (v[a].r > v[b].r) v[b].p = a;
					else {
						v[a].p = b;
						if (v[a].r == v[b].r) {
							++v[b].r;
						}
					}
				}
			}
		}
		printf("Case #%d:\n", tt + 1);
		for (int i = 0; i < n * m; ++i) {
			ch[i] = -1;
		}
		int next = 'a';
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				int x = getp(i * m + j);
				if (ch[x] == -1) {
					ch[x] = next++;
				}
				putchar(ch[x]);
				if (j < m - 1) putchar(' ');
				else putchar('\n');
			}
		}
	}
	return 0;
}
