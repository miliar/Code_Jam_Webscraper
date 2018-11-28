#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdarg>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <functional>
#include <iterator>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); i++)
#define forit(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define eprintf(...) { fprintf(stderr, __VA_ARGS__); fflush(stderr); }
#define sz(v) ((int)((v).size()))
typedef pair<int, int> ii;
typedef long long LL;

const int dx[] = {1,0,-1,0,1,-1};
const int dy[] = {0,1,0,-1,1,-1};
int n, m;
bool a[200][200];
int c[200][200];
bool corner[6], edge[6];

inline int begin(int x) { return x <= n ? 1 : (x-n+1); }
inline int end(int x) { return x <= n ? n + x - 1 : (n+n-1); }
inline bool good(int x, int y) { return 1 <= x && x < n+n && begin(x) <= y && y <= end(x); }

void go_corner_edge(int x, int y) {
	if (x == 1 && y == 1) corner[0] = 1;
	if (x == 1 && y == n) corner[1] = 1;
	if (x == n && y == 1) corner[2] = 1;
	if (x == n && y == n+n-1) corner[3] = 1;
	if (x == n+n-1 && y == n) corner[4] = 1;
	if (x == n+n-1 && y == n+n-1) corner[5] = 1;
	if (x == 1 && 1 < y && y < n) edge[0] = 1;
	if (y - x == n-1 && x > 1 && x < n) edge[1] = 1;
	if (y == n+n-1 && x > n && x < n+n-1) edge[2] = 1;
	if (x == n+n-1 && y > n && y < n+n-1) edge[3] = 1;
	if (x - y == n-1 && y > 1 && y < n) edge[4] = 1;
	if (y == 1 && 1 < x && x < n) edge[5] = 1;
}

void dfs(int x, int y, int cmp) {
	go_corner_edge(x, y);
	c[x][y] = cmp;
	forn(d, 6) {
		int xx = x + dx[d], yy = y + dy[d];
		if (!good(xx, yy) || !a[xx][yy] || c[xx][yy]) continue;
		dfs(xx, yy, cmp);
	}
}

void dfs2(int x, int y, int cmp) {
	go_corner_edge(x, y);
	c[x][y] = cmp;
	forn(d, 6) {
		int xx = x + dx[d], yy = y + dy[d];
		if (!good(xx, yy) || a[xx][yy] || c[xx][yy]) continue;
		dfs2(xx, yy, cmp);
	}
}

bool go(int X, int Y) {
	a[X][Y] = 1;
	int cmp = 0;
	memset(c, 0, sizeof c);
	int ans = 0;
	for (int x = 1; x < n+n; x++) {
		for (int y = begin(x); y <= end(x); y++) {
			if (a[x][y]) {
				if (!c[x][y]) {
					forn(u,6) corner[u] = 0, edge[u] = 0;
					cmp++;
					dfs(x, y, cmp);
					int crs = 0, eds = 0;
					forn(u,6) crs += corner[u], eds += edge[u];
					if (crs >= 2) ans |= 2;
					if (eds >= 3) ans |= 4;
				}
			}
		}
	}
	for (int x = 1; x < n+n; x++) {
		for (int y = begin(x); y <= end(x); y++) {
			if (!a[x][y]) {
				if (!c[x][y]) {
					forn(u,6) corner[u] = 0, edge[u] = 0;
					cmp++;
					dfs2(x, y, cmp);
					int crs = 0, eds = 0;
					forn(u,6) crs += corner[u], eds += edge[u];
					if (eds == 0 && crs == 0) ans |= 1;
				}
			}
		}
	}
	if (!ans) return false;
	stringstream ss;
	if (ans & 2) ss << "-bridge";
	if (ans & 4) ss << "-fork";
	if (ans & 1) ss << "-ring";
	printf("%s", ss.str().substr(1).c_str());
	return true;
}

int main() {
	int __;
	scanf("%d", &__);
	forn(_, __) {
		printf("Case #%d: ", _+1);
		memset(a, 0, sizeof a);
		scanf("%d%d", &n, &m);
		bool b = true;
		forn(i, m) {
			int x, y;
			scanf("%d%d", &x, &y);
			if (b && go(x, y)) {
				printf(" in move %d", i+1);
				b = false;
			}
		}
		if (b) printf("none");
		printf("\n");
	}
	return 0;
}
