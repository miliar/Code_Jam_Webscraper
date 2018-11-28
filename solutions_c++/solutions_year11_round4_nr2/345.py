#include <cmath>
#include <iostream>
using namespace std;

const int maxn = 500 + 10;
const double eps = 1e-8;

int tcase, R, C, D, w[maxn][maxn];
int xw[maxn][maxn], sxw[maxn][maxn], yw[maxn][maxn], syw[maxn][maxn], sw[maxn][maxn];
int ans;

void init() {
	scanf("%d%d%d", &R, &C, &D);
	for (int i = 1; i <= R; ++i) {
		scanf("\n");
		for (int j = 1; j <= C; ++j)
			w[i][j] = getchar() - '0';
	}
}

void work() {
	//prepare
	for (int i = 1; i <= R; ++i)
		for (int j = 1; j <= C; ++j) {
			sw[i][j] = sw[i][j-1] - sw[i-1][j-1] + sw[i-1][j] + w[i][j];
			xw[i][j] = i*w[i][j], yw[i][j] = j*w[i][j];
			sxw[i][j] = sxw[i][j-1] - sxw[i-1][j-1] + sxw[i-1][j] + xw[i][j];
			syw[i][j] = syw[i][j-1] - syw[i-1][j-1] + syw[i-1][j] + yw[i][j];
		}

	//main procedure
	ans = 0;
	int sumx, sumy, sumw;
	for (int k = min(R, C); k >= 3 && !ans; --k)
		for (int i = R; i >= k && !ans; --i)
			for (int j = C; j >= k && !ans; --j) {
				sumx = sxw[i][j] - sxw[i][j-k] - sxw[i-k][j] + sxw[i-k][j-k];
				sumy = syw[i][j] - syw[i][j-k] - syw[i-k][j] + syw[i-k][j-k];
				sumw = sw[i][j] - sw[i][j-k] - sw[i-k][j] + sw[i-k][j-k];
				
				sumx -= xw[i][j] + xw[i][j-k+1] + xw[i-k+1][j] + xw[i-k+1][j-k+1];
				sumy -= yw[i][j] + yw[i][j-k+1] + yw[i-k+1][j] + yw[i-k+1][j-k+1];
				sumw -= w[i][j] + w[i][j-k+1] + w[i-k+1][j] + w[i-k+1][j-k+1];

				if (fabs(sumx - sumw * (i - (k-1)/2.0)) < eps && fabs(sumy - sumw * (j - (k-1)/2.0)) < eps) {
					ans = k;
					//cout << i << " "<< j << endl;
				}
			}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int k = 1; k <= tcase; ++k) {
		init();
		work();
		if (ans) printf("Case #%d: %d\n", k, ans);
		else printf("Case #%d: IMPOSSIBLE\n", k);
	}
	return 0;
}
