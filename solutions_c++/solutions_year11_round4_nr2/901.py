#include <stdio.h>
#include <string.h>
#include <math.h>
#define MAXN 20
#define eps 1e-7

char str[MAXN];
int mp[MAXN][MAXN];
int n, m, d;

bool check(int x, int y, int k) {
	if(x + k - 1 >= n || y + k - 1 >= m) return false;
	double dx = 0.0, dy = 0.0, cx = (double)(x + x + k - 1) / 2.0, cy = (double)(y + y + k - 1) / 2.0;
	for(int i = x; i <= x + k - 1; ++i)
		for(int j = y; j <= y + k - 1; ++j) {
			if((i == x || i == x + k - 1) && (j == y || j == y + k - 1)) continue;
			dx += (i - cx) * mp[i][j];
			dy += (j - cy) * mp[i][j];
		}
	return fabs(dx) < eps && fabs(dy) < eps;
}

int main() {
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int caseT = 1; caseT <= cases; ++caseT) {
		scanf("%d%d%d", &n, &m, &d);
		for(int i = 0; i < n; ++i) {
			scanf("%s", str);
			for(int j = 0; j < m; ++j) mp[i][j] = str[j] - '0' + d;
		}
		int res = 0;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j) {
				double cx = 0.0, cy = 0.0;
				for(int len = 1; i - len >= 0 && i + len < n && j - len >= 0 && j + len < m; ++len) {
					for(int ii = i - len; ii <= i - len; ++ii)
						for(int jj = j - len; jj <= j + len; ++jj) {
							cx += (ii - i) * mp[ii][jj];
							cy += (jj - j) * mp[ii][jj];
						}
					for(int ii = i + len; ii <= i + len; ++ii)
						for(int jj = j - len; jj <= j + len; ++jj) {
							cx += (ii - i) * mp[ii][jj];
							cy += (jj - j) * mp[ii][jj];
						}
					for(int ii = i - len + 1; ii < i + len; ++ii)
						for(int jj = j - len; jj <= j - len; ++jj) {
							cx += (ii - i) * mp[ii][jj];
							cy += (jj - j) * mp[ii][jj];
						}
					for(int ii = i - len + 1; ii < i + len; ++ii)
						for(int jj = j + len; jj <= j + len; ++jj) {
							cx += (ii - i) * mp[ii][jj];
							cy += (jj - j) * mp[ii][jj];
						}
					double tcx = cx, tcy = cy;
					tcx -= (i - len - i) * mp[i - len][j - len];
					tcy -= (j - len - j) * mp[i - len][j - len];
					tcx -= (i - len - i) * mp[i - len][j + len];
					tcy -= (j + len - j) * mp[i - len][j + len];
					tcx -= (i + len - i) * mp[i + len][j - len];
					tcy -= (j - len - j) * mp[i + len][j - len];
					tcx -= (i + len - i) * mp[i + len][j + len];
					tcy -= (j + len - j) * mp[i + len][j + len];
					if(tcx == 0.0 && tcy == 0.0 && len * 2 + 1 > res) res = len * 2 + 1;
				}
			}
		for(int i = 0; i < n - 1; ++i)
			for(int j = 0; j < m - 1; ++j) {
				double cx = 0.0, cy = 0.0;
				for(int len = 1; i - len + 1 >= 0 && i + len < n && j - len + 1 >= 0 && j + len < m; ++len) {
					for(int ii = i - len + 1; ii <= i - len + 1; ++ii)
						for(int jj = j - len + 1; jj <= j + len; ++jj) {
							cx += (ii - i - 0.5) * mp[ii][jj];
							cy += (jj - j - 0.5) * mp[ii][jj];
						}
					for(int ii = i + len; ii <= i + len; ++ii)
						for(int jj = j - len + 1; jj <= j + len; ++jj) {
							cx += (ii - i - 0.5) * mp[ii][jj];
							cy += (jj - j - 0.5) * mp[ii][jj];
						}
					for(int ii = i - len + 2; ii < i + len; ++ii)
						for(int jj = j - len + 1; jj <= j - len + 1; ++jj) {
							cx += (ii - i - 0.5) * mp[ii][jj];
							cy += (jj - j - 0.5) * mp[ii][jj];
						}
					for(int ii = i - len + 2; ii < i + len; ++ii)
						for(int jj = j + len; jj <= j + len; ++jj) {
							cx += (ii - i - 0.5) * mp[ii][jj];
							cy += (jj - j - 0.5) * mp[ii][jj];
						}
					double tcx = cx, tcy = cy;
					tcx -= (i - len + 1 - i - 0.5) * mp[i - len + 1][j - len + 1];
					tcy -= (j - len + 1 - j - 0.5) * mp[i - len + 1][j - len + 1];
					tcx -= (i - len + 1 - i - 0.5) * mp[i - len + 1][j + len];
					tcy -= (j + len - j - 0.5) * mp[i - len + 1][j + len];
					tcx -= (i + len - i - 0.5) * mp[i + len][j - len + 1];
					tcy -= (j - len + 1 - j - 0.5) * mp[i + len][j - len + 1];
					tcx -= (i + len - i - 0.5) * mp[i + len][j + len];
					tcy -= (j + len - j - 0.5) * mp[i + len][j + len];
					if(tcx == 0.0 && tcy == 0.0 && len * 2 + 1 > res) res = 2 * len;
				}
			}
		printf("Case #%d: ", caseT);
		if(res < 3) puts("IMPOSSIBLE");
		else printf("%d\n", res);
	}
	return 0;
}
