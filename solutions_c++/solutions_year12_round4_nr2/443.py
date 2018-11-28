#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef pair<int, int> pii;
typedef long long llong;

#define mp make_pair
#define lowbit(x) ((x) & (-(x)))
#define pf(x) ((x) * (x))
#define two(x) (1 << (x))
#define twoL(x) ((llong) 1 << (x))
#define clr(x, c) memset(x, c, sizeof(x))

inline void ch_max(int &x, int y) {if (x < y) x = y;}
inline void ch_min(int &x, int y) {if (x > y) x = y;}

const double pi = acos(-1.0);
const double eps = 1e-9;


const int N = 1005;
int W, L;
int R[N], n;

struct P {
	int r, k;
}p[N];

bool cmp(P a, P b) {
	return a.r > b.r;
}

vector< pii > vp;

void add_vp(int x, int y) {
	if (x < 0 || x > W || y < 0 || y > L) return ;
	vp.push_back(mp(x, y));
}
struct Node {
	int x0, y0, x1, y1;
	void init(int _x0, int _y0, int _x1, int _y1) {
		x0 = _x0;
		y0 = _y0;
		x1 = _x1;
		y1 = _y1;
	}
	void ad() {
		if (x0 > x1) swap(x0, x1);
		if (y0 > y1) swap(y0, y1);
	}
}node[N];

int ax[4] = {1, 1, -1, -1};
int ay[4] = {1, -1, 1, -1};

bool ok(int m) {
	int i, j, k = m;
	int x = (node[k].x0 + node[k].x1) / 2;
	int y = (node[k].y0 + node[k].y1) / 2;
	if (x < 0 || x > W || y < 0 || y > L) return false;

	for (i = 0; i < m; ++i) {
		if (node[i].x1 <= node[k].x0) continue;
		if (node[k].x1 <= node[i].x0) continue;
		if (node[i].y1 <= node[k].y0) continue;
		if (node[k].y1 <= node[i].y0) continue;
		return false;
	}
	return true;
}
void solve() {
	int i, j, k;
	sort(p, p + n, cmp);
	vp.clear();
	
	if (W > L) {
		int max_x = 0;
		for (i = 0; i < n; ++i) {
			if (max_x > W) break;
			int x = max_x, y = 0;
			node[i].init(x - p[i].r, y - p[i].r, x + p[i].r, y + p[i].r);
			max_x += p[i].r;
			if (i + 1 < n) {
				max_x += p[i + 1].r;
			}

			add_vp(node[i].x0, node[i].y0);
			add_vp(node[i].x0, node[i].y1);
			add_vp(node[i].x1, node[i].y0);
			add_vp(node[i].x1, node[i].y1);
		}
	} else {
		int max_y = 0;
		for (i = 0; i < n; ++i) {
			if (max_y > L) break;
			int x = 0, y = max_y;
			node[i].init(x - p[i].r, y - p[i].r, x + p[i].r, y + p[i].r);
			max_y += p[i].r;
			if (i + 1 < n) {
				max_y += p[i + 1].r;
			}

			add_vp(node[i].x0, node[i].y0);
			add_vp(node[i].x0, node[i].y1);
			add_vp(node[i].x1, node[i].y0);
			add_vp(node[i].x1, node[i].y1);
		}
	}
	
	for (; i < n; ++i) {
		for (j = 0; j < vp.size(); ++j) {
			int x = vp[j].first;
			int y = vp[j].second;
 			for (k = 0; k < 4; ++k) {
				int tx = x + ax[k] * p[i].r * 2;
				int ty = y + ay[k] * p[i].r * 2;
				node[i].init(x, y, tx, ty);
				node[i].ad();
				if (ok(i)) break;
			}
			if (k < 4) break;
		}
		if (j == vp.size()) {
			cout << "God" <<endl;
		}
		add_vp(node[i].x0, node[i].y0);
		add_vp(node[i].x0, node[i].y1);
		add_vp(node[i].x1, node[i].y0);
		add_vp(node[i].x1, node[i].y1);
	}
}
int main() {
	freopen("GCJ\\B-large.in", "r", stdin);
	//freopen("GCJ\\in.txt", "r", stdin);
	freopen("GCJ\\out.txt", "w", stdout);
	int i, j, k, t, nc = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d%d", &n, &W, &L);
		for (i = 0; i < n; ++i) {
			scanf("%d", &p[i].r);
			p[i].k = i;
		}
		solve();
		int x[N], y[N];
		for (i = 0; i < n; ++i) {
			x[p[i].k] = (node[i].x0 + node[i].x1) / 2;
			y[p[i].k] = (node[i].y0 + node[i].y1) / 2;
		}
		printf("Case #%d:", ++nc);
		for (i = 0; i < n; ++i) {
			printf(" %d %d", x[i], y[i]);
		}
		printf("\n");
	}
	return 0;
}