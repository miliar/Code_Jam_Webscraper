#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

char s[600];
int a[600][600];
int dm[600][600];
int dmu[600][600];
int dml[600][600];
int res[600];
bool GetSqr(int n, int m) {
	int sq = n * m;
	for (int i = 0; i < n; i++) {
		dml[i][0] = (a[i][0] <= 1);
		for (int j = 1; j < m; j++) {
			if (a[i][j] > 1) {
				dml[i][j] = 0;
			} else if (a[i][j - 1] == a[i][j]) {
				dml[i][j] = 1;
			} else {
				dml[i][j] = dml[i][j - 1] + 1;
			}
		}
	}
	for (int j = 0; j < m; j++) {
		dmu[0][j] = (a[0][j] <= 1);
		for (int i = 1; i < n; i++) {
			if (a[i][j] > 1) {
				dmu[i][j] = 0;
			} else if (a[i - 1][j] == a[i][j]) {
				dmu[i][j] = 1;
			} else {
				dmu[i][j] = dmu[i - 1][j] + 1;
			}
		}
	}

	int cmx = 0, ri = 0, rj = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] > 1) {
				sq--;
				dm[i][j] = 0;
				continue;
			}
			if (!i || !j) {
				dm[i][j] = 1;
			} else if (a[i - 1][j - 1] == a[i - 1][j]) {
				dm[i][j] = 1;
			} else {
				dm[i][j] = min(dm[i - 1][j - 1] + 1, min(dmu[i][j], dml[i][j]));
			}
			if (dm[i][j] > cmx) {
				cmx = dm[i][j];
				ri = i;
				rj = j;
			}
		}
	}
	if (cmx == 0) return false;
	if (cmx == 1) {
		res[1] += sq;
		return false;
	}
	res[cmx]++;
	for (int i = 0; i < cmx; i++) {
		for (int j = 0; j < cmx; j++) {
			a[ri - i][rj - j] = 666;
		}
	}
	return true;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", s);
			char *p = s;
			for (int j = 0; j < m;  p++) {
				int v = 0;
				if ('0' <= *p && *p <= '9') {
					v = *p - '0';
				} else {
					v = *p - 'A' + 10;
				}
				int nv = 0;
				for (int mur = 0; mur < 4; mur++) {
					nv = (nv + nv) + (v & 1);
					v /= 2;
				}
				v = nv;
				for (int k = 0; k < 4; k++, v >>= 1) {
					a[i][j++] = v & 1;
				}
			}
		}
		while (GetSqr(n, m));
		int k = 0;
		for (int i = 600; i >= 1; i--) {
			if (res[i] > 0) {
				k++;
			}
		}
		printf("Case #%d: %d\n", itest, k);
		for (int i = 600; i >= 1; i--) {
			if (res[i] > 0) {
				printf("%d %d\n", i, res[i]);
				res[i] = 0;
			}
		}
	}
	return 0;
}