#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;
int r, c, d, a[15][15];
char buf[15];

bool test(int ri, int cj, int k) {
	double rm = 0., cm = 0.;
	double rc = (ri + ri + k - 1) / 2., cc = (cj + cj + k - 1) / 2.;
	for (int i = ri; i < ri + k; ++i) {
		for (int j = cj; j < cj + k; ++j) {
			if (i == ri && j == cj)continue;
			if (i == ri && j == cj + k - 1)continue;
			if (i == ri + k - 1 && j == cj)continue;
			if (i == ri + k - 1 && j == cj + k - 1)continue;
			rm += (i - rc)*(a[i][j] + d);
			cm += (j - cc)*(a[i][j] + d);
		}
	}
	return fabs(rm) < 1e-9 && fabs(cm) < 1e-9;
}

int main(int argc, char** argv) {
	int T;
	scanf("%d", &T);
	for (int nCase = 1; nCase <= T; ++nCase) {
		int ans = -1;
		scanf("%d%d%d", &r, &c, &d);
		for (int i = 0; i < r; ++i) {
			scanf("%s", buf);
			for (int j = 0; j < c; ++j) {
				a[i][j] = buf[j] - '0';
			}
		}
		for (int k = r < c ? r : c; k >= 3 && ans == -1; --k) {
			for (int i = 0; i + k <= r && ans == -1; ++i) {
				for (int j = 0; j + k <= c && ans == -1; ++j) {
					if (test(i, j, k)) {
						ans = k;
					}
				}
			}
		}
		printf("Case #%d: ", nCase);
		if (ans == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
