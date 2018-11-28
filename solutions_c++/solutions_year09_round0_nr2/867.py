#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>

#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <list>

#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) a.size() - 1
#define all(a) a.begin(), a.end()
#define I (int)
#define I64 (long long)
#define LD (long double)
#define VI vector<int>
#define pti pair<int, int>
#define ptd pair<long double, long double>
#define sqr(x) ((x) * (x))

const long double EPS = 1E-9;
const int INF = (int)1E9;
const long long INF64 = (long long)1E18;
const long double PI = 2 * acos(.0);

typedef long double ld;
typedef long long ll;

int n, m;
int a[110][110];
int d[110][110];
char col[30];
bool used[110][110];
int st[110][110];
vector<pti> vt;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

inline bool exist(int x, int y) {
	return 0 <= x && x < n &&
		0 <= y && y < m;
}

int getColor(int x, int y) {
	if (used[x][y])return d[x][y];

	used[x][y] = true;

	if (binary_search(all(vt), mp(x, y))) {
		return d[x][y] = (int)(lower_bound(all(vt), mp(x, y)) - vt.begin());
	} else {
		forn(i, 4) {
			int xx = x + dx[i];
			int yy = y + dy[i];
			if (exist(xx, yy) && a[xx][yy] == st[x][y]) {
				return d[x][y] = getColor(xx, yy);
			}
		}	
	}

	return -INF;
}

void solve() {
	scanf("%d%d", &n, &m);
	memset(used, 0, sizeof(used));
	memset(st, 0, sizeof(st));
	memset(col, 0, sizeof(col));
	memset(d, 0, sizeof(d));
	vt.clear();

	forn(i, n) {
		forn(j, m) {
			scanf("%d", &a[i][j]);
		}
	}

	forn(i, n) {
		forn(j, m) {
			forn(k, 4) {
				int xx = i + dx[k];
				int yy = j + dy[k];
				if (exist(xx, yy) && a[i][j] > a[xx][yy]) {
					st[i][j]++;
				}
			}

			if (st[i][j] == 0) {
				vt.pb(mp(i, j));
			}
		}
	}

	forn(i, n) {
		forn(j, m) {
			st[i][j] = INF;
			forn(k, 4) {
				int xx = i + dx[k];
				int yy = j + dy[k];
				if (exist(xx, yy)) {
					st[i][j] = min(st[i][j], a[xx][yy]);
				}
			}
		}
	}

	sort(all(vt));
	vt.erase(unique(all(vt)), vt.end());

	char cur = 'a';

	forn(i, n) {
		forn(j, m) {
			if (col[getColor(i, j)] == 0) {
				col[d[i][j]] = cur;
				cur++;
			}
			printf("%c", col[d[i][j]]);
			if (j + 1 != m)
				printf(" ");
		}
		printf("\n");
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	cin >> t;

	forn(i, t) {
		printf("Case #%d:\n", i + 1);
		solve();
	}
	
    return 0;
}
