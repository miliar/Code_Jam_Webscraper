#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
//#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int, pii> pip;
typedef pair<pii, int> ppi;
typedef pair<int64, int64> pii64;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
//typedef complex<double> point;
#define FAIL ++*(int*)0
#define eps  1e-9
#define inf  0x7f7f7f7f
#define left huyleft
#define right huyright
#define MP make_pair
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define TASK "B"
#define RR 151

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int n, m;
int H;
int c[1 << 7][1 << 7];
int f[1 << 7][1 << 7];

inline bool ok (int x, int y) {
	return x >= 0 && y >= 0 && x < n && y < m;
}

inline bool can (int x1, int y1, int x2, int y2) {
	return c[x2][y2] - f[x2][y2] >= 50 && c[x2][y2] - f[x1][y1] >= 50 && 
		c[x1][y1] - f[x2][y2] >= 50;
}

inline bool can_height (int x1, int y1, int x2, int y2, double h) {
	return c[x2][y2] - h >= 50;
}

map< pair<pii, double>, double> dist;
int cnt[1 << 7][1 << 7];

double dijkstra () {
	memset(cnt, 0, sizeof cnt);
	int x = 0, y = 0;
	dist.clear();
	dist[MP(MP(x, y), H)] = 0.0;
	priority_queue< pair<double, pair<pii, double> >, vector< pair<double, pair<pii, double> > >, greater< pair<double, pair<pii, double> > > > pq;
	pq.push(MP(0.0, MP(MP(x, y), H)));
	while (!pq.empty()) {
		if (sz(pq) > 100000) cerr << sz(pq) << endl;
		pair<pii, double> cur = pq.top().second;
		double curd = pq.top().first;
		pq.pop();
		x = cur.first.first;
		y = cur.first.second;
		if (++cnt[x][y] > 100) continue;
		double h = cur.second;
		if (x == n - 1 && y == m - 1) return curd;
		if (fabs(dist[cur] - curd) > eps) continue;
		for (int i = 0; i < 4; ++i) {
			int tx = x + dx[i];
			int ty = y + dy[i];
			if (!ok(tx, ty) || !can(x, y, tx, ty)) continue;
			double hd = c[tx][ty] - h;
			double td = max(50.0 - hd, 0.0) / 10.0;
			if (fabs(td) < eps && fabs(h - H) < eps) {
				if (!dist.count(MP(MP(tx, ty), h))) {
					dist[MP(MP(tx, ty), h)] = 0.0;
					pq.push(MP(curd + td, MP(MP(tx, ty), h)));
				}
				continue;
			}
			if (h - td * 10.0 - f[x][y] >= 20)
				td += 1.0;
			else
				td += 10.0;
			double th = h - td * 10.0;
			if (!dist.count(MP(MP(tx, ty), th)) || dist[MP(MP(tx, ty), th)] - eps > curd + td) {
				dist[MP(MP(tx, ty), th)] = curd + td;
				pq.push(MP(curd + td, MP(MP(tx, ty), th)));
			}
		}
	}
	return -1.0;
}

void solve () {
	scanf("%d%d%d", &H, &n, &m);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			scanf("%d", &c[i][j]);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			scanf("%d", &f[i][j]);
	printf("%.20lf\n", dijkstra());
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int T;
	char buf[32];
	gets(buf);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
