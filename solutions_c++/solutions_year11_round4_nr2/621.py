#include <stdio.h>
#include <string>
#include <map>
#include <set>
#include <cmath>
using namespace std;

int R, C, D;
char a[505][505];
long long t[505][505];
int i, j, ii, jj;
double sx, sy;
long long mass;
int K = 0;

int main() {
	int kejs, kejsis;
	scanf("%d", &kejsis);
	for (kejs = 1; kejs <= kejsis; kejs++) {
		printf("Case #%d: ", kejs);
		scanf("%d%d%d", &R, &C, &D);
		for (i = 0; i < R; i++) {
			scanf("%s", a[i]);
			for (j = 0; j < C; j++) {
				t[i][j] = a[i][j] - '0' + D;
			}
		}
		for (K = min(R, C); K >= 3; K--) {
			for (ii = 0; ii <= R - K; ii++) {
				for (jj = 0; jj <= C - K; jj++) {
					sx = sy = 0;
					mass = 0;
					for (i = 0; i < K; i++) {
						for (j = 0; j < K; j++) {
							if (i == K-1 && j == K-1) continue;
							if (i == 0 && j == K-1) continue;
							if (i == K-1 && j == 0) continue;
							if (i == 0 && j == 0) continue;
							mass += t[i+ii][j+jj];
							sx += (i+ii) * t[i+ii][j+jj];
							sy += (j+jj) * t[i+ii][j+jj];
						}
					}
					if (fabs(sx / mass - (ii + (K-1) / 2.)) < 1e-9 && fabs(sy / mass - (jj + (K-1) / 2.)) < 1e-9) break;
				}
				if (jj <= C-K) break;
			}
			if (ii <= R-K) break;
		}
		if (K < 3) printf("IMPOSSIBLE\n");
		else printf("%d\n", K);
	}
	return 0;
}

