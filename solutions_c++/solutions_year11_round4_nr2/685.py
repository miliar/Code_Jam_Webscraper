#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#define out(v) cout << #v << ": " << (v) << endl
using namespace std;
typedef long long LL;

int T, R, C, D;
int mat[15][15];
int sgn(double x, double eps = 1.0e-9) {
	return (x > eps) - (x < -eps);
}
bool gao(int x, int y, int K) {
	double cx = K / 2.0, cy = K / 2.0;
	double sumx = 0.0, sumy = 0.0;
	for (int i = 0; i < K; ++i)
		for (int j = 0; j < K; ++j) {
			if (i == 0 && j == 0) continue;
			if (i == 0 && j == K - 1) continue;
			if (i == K - 1 && j == 0) continue;
			if (i == K - 1 && j == K - 1) continue;
			sumx += (i + 0.5 - cx) * mat[x + i][y + j];
			sumy += (j + 0.5 - cy) * mat[x + i][y + j];
		}
	//printf("c %f %f sum %f %f\n", cx, cy, sumx, sumy);
	return (sgn(sumx) == 0 && sgn(sumy) == 0);
}
int main() {
	scanf("%d", &T);
	for (int id = 1; id <= T; ++id) {
		scanf("%d%d%d", &R, &C, &D);
		for (int i = 0; i < R; ++i)
			for (int j = 0; j < C; ++j) {
				scanf("%1d", &mat[i][j]);
				mat[i][j] += D;
			}
		int ans = -1;
		for (int i = 0; i < R; ++i)
			for (int j = 0; j < C; ++j)
				for (int K = 3; i + K <= R && j + K <= C; ++K)
					if (gao(i, j, K))
						ans = max(ans, K);
		printf("Case #%d: ", id);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}
