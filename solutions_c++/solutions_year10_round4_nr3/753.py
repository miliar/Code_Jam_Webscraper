#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

int mat[2][105][105];

int main() {
	int C, _42=1, R, X1, Y1, X2, Y2;
	scanf(" %d", &C);
	while (C--) {
		scanf(" %d", &R);
		memset(mat, 0, sizeof(mat));
		int MX=0, MY=0;
		for (int i=0;i<R;i++) {
			scanf(" %d %d %d %d", &X1, &Y1, &X2, &Y2);
			MX = max(MX, max(X1, X2));
			MY = max(MY, max(Y1, Y2));
			for (int j=X1;j<=X2;j++) {
				for (int k=Y1;k<=Y2;k++) {
					mat[0][j][k] = 1;
				}
			}
		}
		int atual=0;
		int next;
		bool tem;
		int ans = 0;
		while (1) {
			ans++;
			tem = false;
			next = (atual+1)%2;
			memset(mat[next], 0, sizeof(mat[next]));
			/*for (int i=1;i<=MX;i++) {
				for (int j=1;j<=MY;j++) {
					printf("%d", mat[next][i][j]);
				}
				printf("\n");
			}*/
			for (int i=1;i<=MX;i++) {
				for (int j=1;j<=MY;j++) {
					if (mat[atual][i][j] == 0) {
						if (mat[atual][i-1][j] == 1 && mat[atual][i][j-1] == 1) {
							mat[next][i][j] = 1;
							tem = true;
						}
					}
					else if (mat[atual][i][j] == 1) {
						if (mat[atual][i-1][j] == 0 && mat[atual][i][j-1] == 0) {
							mat[next][i][j] = 0;
						}
						else {
							mat[next][i][j] = 1;
							tem = true;
						}
					}
				}
			}
			atual = next;
			if (!tem) break;
		}
		printf("Case #%d: %d\n", _42++, ans);
	}
	return 0;
}
