#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 110;

bool mat[MAXN][MAXN], tmat[MAXN][MAXN];
int cas, R, C, n, minX, minY, maxX, maxY;

inline bool ok() {
	for (int i = 1; i <= R; i ++)
		for (int j = 1; j <= C; j ++)
			if (mat[i][j])
				return false;
	return true;
}

inline int cal() {
	int ret = 0;

	while(! ok()) {
// 		for (int i = 1; i <= R; i ++) {
// 			for (int j = 1; j <= C; j ++)
// 				printf("%d", mat[i][j]);
// 			puts("");
// 		}
// 		puts("");

		memcpy(tmat, mat, sizeof(mat));
		for (int i = 1; i <= R+1; i ++) {
			for (int j = 1; j <= C+1; j ++) {
				if (mat[i][j] && ! mat[i-1][j] && ! mat[i][j-1])
					tmat[i][j] = false;
				else if (! mat[i][j] && mat[i-1][j] && mat[i][j-1]) {
					tmat[i][j] = true;
					R = max(R, i);
					C = max(C, j);
				}
			}
		}
		ret ++;
		memcpy(mat, tmat, sizeof(tmat));
	}
	return ret;
}

int main() {
	freopen("in.txt", "r", stdin);
 	freopen("out.txt", "w", stdout);

	scanf("%d", &cas);
	for (int c = 1; c <= cas; c ++) {
		R = C = 0;
		memset(mat, false, sizeof(mat));

		scanf("%d", &n);
		for (int i = 0; i < n; i ++) {
			scanf("%d%d%d%d", &minY, &minX, &maxY, &maxX);

			R = max(R, maxX);
			C = max(C, maxY);
			for (int r = minX; r <= maxX; r ++) {
				for (int c = minY; c <= maxY; c ++) {
					mat[r][c] = true;
				}
			}
		}
		printf("Case #%d: %d\n", c, cal());
	}

	return 0;
}