#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1024;

struct node {
	int idx;
	int r;
	node() {}
	node(int idx, int r):idx(idx), r(r) {}
};

node v[MAXN];
int x[MAXN], y[MAXN];
int outx[MAXN], outy[MAXN];
int W, L;

inline bool cmp(const node &a, const node &b) {
	return a.r > b.r;
}

inline bool vx(int i, int j) {
	return (i == 0 || i == W) && (j == 0 || j == L);
}

int main() {
	int i, j, k;
	int m, n;
	int tc, cn(0);
	int cx, cy, pre;

	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &tc);
	while (tc--) {
		scanf("%d%d%d", &n, &W, &L);
		for (i=0; i<n; ++i) {
			scanf("%d", &v[i].r);
			v[i].idx = i;
		}
		sort(v, v+n, cmp);
		x[0] = 0, y[0] = 0;
		cx = 0, cy = v[0].r;
		pre = v[0].r;
		for (i=1; i<n; ++i) {
			if (v[i].r + cy > L) {
				cx = pre, cy = 0;
				pre = cx + 2 * v[i].r;
			}
			if (cx == 0) x[i] = cx;
			else x[i] = cx + v[i].r;
			if (cy == 0) y[i] = cy;
			else y[i] = cy + v[i].r;
			cy = y[i] + v[i].r;
		}
		for (i=0; i<n; ++i) outx[v[i].idx] = x[i], outy[v[i].idx] = y[i];
		printf("Case #%d:", ++cn);
		for (i=0; i<n; ++i) printf(" %d %d", outx[i], outy[i]);
		puts("");
	}

	return 0;
}