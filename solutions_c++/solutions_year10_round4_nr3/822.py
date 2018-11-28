#include <stdio.h>
#include <string.h>

int m[2][1000][1000];

int main() {
	int C, _42 = 0;
	scanf(" %d", &C);
	while (C--) {
		memset(m, 0, sizeof(m));

		int R;
		scanf(" %d", &R);
		for (int r=0; r < R; r++) {
			int x1,y1,x2,y2;
			scanf(" %d %d %d %d", &x1, &y1, &x2, &y2);
			for (int y=y1; y <= y2; y++) {
				for (int x=x1; x <= x2; x++) {
					m[0][y][x] = 1;
				}
			}
		}

		bool bacteria = true;
		int ans = 0;
		int H=900, W=900;
		int t=0;
		do {
			bacteria = false;
			ans++;
			memset(m[1-t], 0, sizeof(m[1-t]));

			for (int i=0; i < H; i++) {
				for (int j=0; j < W; j++) {
					if (m[t][i][j]) {
						if ((i>0 && m[t][i-1][j]) || (j>0 && m[t][i][j-1])) {
							// fica viva
							m[1-t][i][j] = 1;
							bacteria = true;
						}
					}
					else {
						if ((i>0 && m[t][i-1][j]) && (j>0 && m[t][i][j-1])) {
							// nasce
							m[1-t][i][j] = 1;
							bacteria = true;
						}
					}
				}
			}

			t = 1-t;
		} while (bacteria);

		printf("Case #%d: %d\n", ++_42, ans);
	}
	return 0;
}
