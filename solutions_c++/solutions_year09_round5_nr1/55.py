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

const int dd[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

typedef double dbl;
typedef long double ldbl;
typedef long long i64;

char s[20][20];

map<int, bool> dangerous;
int u[100][100];

inline pair<int, pair<int, int> > simplify(int n, int m, const vector<short> &v) {
	int r = 0;
	int y = m, x = n;
	for (int i = 0; i < n; ++i) if (v[i]) {
		if (x == n) {
			x = i;
		}
		for (int j = 0; j < m; ++j) {
			if (v[i] & (1 << j)) {
				if (j < y) y = j;
				break;
			}
		}
	}
	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < 5; ++j) {
			if (v[x + i] & (1 << (y + j))) {
				r |= 1 << (i * 5 + j);
			}
		}
	}
	return mp(r, mp(x, y));
}

inline bool isdanger(int n, int m, int l, const vector<short> &v) {
	pair<int, pair<int, int> > w = simplify(n, m, v);
	if (dangerous.find(w.first) != dangerous.end()) return dangerous[w.first];
	static int tt = 0;
	++tt;
	for (int i = w.second.first; i < n; ++i) if (v[i]) {
		for (int j = w.second.second; j < m; ++j) {
			if (v[i] & (1 << j)) {
				int q[10];
				int h = 0, t = 0;
				q[t++] = (i << 10) + j;
				u[i][j] = tt;
				while (h < t) {
					int w = q[h++];
					int x = w >> 10, y = w & 1023;
					for (int k = 0; k < 4; ++k) {
						int xx = x + dd[k][0], yy = y + dd[k][1];
						if ((xx >= 0) && (yy >= 0) && (xx < n) && (yy < m) && (v[xx] & (1 << yy)) && (u[xx][yy] != tt)) {
							u[xx][yy] = tt;
							q[t++] = (xx << 10) + yy;
						}
					}
				}
				return dangerous[w.first] = (t != l);
			}
		}
	}
	return dangerous[w.first] = false;
}

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		dangerous.clear();
		int result = -1;
		int n, m; scanf("%d %d", &n, &m);
		vector<short> w(n);
		vector<short> b(n);
		vector<short> g(n);
		int l = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%s", s[i]);
			w[i] = b[i] = g[i] = 0;
			for (int j = 0; j < m; ++j) {
				if (s[i][j] == '#') w[i] |= 1 << j;
				else if (s[i][j] == 'x') g[i] |= 1 << j;
				else if (s[i][j] == 'o') ++l, b[i] |= 1 << j;
				else if (s[i][j] == 'w') {
					++l;
					b[i] |= 1 << j;
					g[i] |= 1 << j;
				}
			}
		}
		if (!isdanger(n, m, l, b) && !isdanger(n, m, l, g)) {
			queue<vector<short> > q;
			map<vector<short>, int> d;
			d[b] = 0;
			q.push(b);
			while (!q.empty()) {
				vector<short> v = q.front(); q.pop();
				int dv = d[v];
				if (v == g) {
					result = dv;
					break;
				}
				bool dangerous = isdanger(n, m, l, v);
				for (int i = 0; i < n; ++i) if (v[i]) {
					for (int j = 0; j < m; ++j) if (v[i] & (1 << j)) {
						if (j && (j < m - 1) && !(v[i] & (1 << (j - 1))) && !(v[i] & (1 << (j + 1))) && !(w[i] & (1 << (j - 1))) && !(w[i] & (1 << (j + 1)))) {
							v[i] ^= (1 << j) | (1 << (j - 1));
							if ((d.find(v) == d.end()) && (!dangerous || !isdanger(n, m, l, v))) {
								d[v] = dv + 1;
								q.push(v);
							}
							v[i] ^= (1 << j) | (1 << (j - 1));
							v[i] ^= (1 << j) | (1 << (j + 1));
							if ((d.find(v) == d.end()) && (!dangerous || !isdanger(n, m, l, v))) {
								d[v] = dv + 1;
								q.push(v);
							}
							v[i] ^= (1 << j) | (1 << (j + 1));
						}
						if (i && (i < n - 1) && !(v[i - 1] & (1 << j)) && !(v[i + 1] & (1 << j)) && !(w[i - 1] & (1 << j)) && !(w[i + 1] & (1 << j))) {
							v[i - 1] ^= (1 << j);
							v[i] ^= (1 << j);
							if ((d.find(v) == d.end()) && (!dangerous || !isdanger(n, m, l, v))) {
								d[v] = dv + 1;
								q.push(v);
							}
							v[i - 1] ^= (1 << j);
							v[i] ^= (1 << j);
							v[i + 1] ^= (1 << j);
							v[i] ^= (1 << j);
							if ((d.find(v) == d.end()) && (!dangerous || !isdanger(n, m, l, v))) {
								d[v] = dv + 1;
								q.push(v);
							}
							v[i + 1] ^= (1 << j);
							v[i] ^= (1 << j);
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", tt + 1, result);
		fflush(stdout);
	}
	return 0;
}
