#include<stdio.h>
#include<string>
const int maxn = 102;
int f[maxn][maxn];
int h, w, R;
char g[maxn][maxn];
int mov[2][2] = {{1, 2}, {2, 1}};
int mod = 10007;
int main() {
	int T;
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		scanf("%d%d%d", &h, &w, &R);
		memset(g, 0, sizeof(g));
		for (int i = 0; i < R; i++) {
			int r, c;
			scanf("%d%d", &r, &c);
			g[r][c] = 1;
		}
		memset(f, 0, sizeof(f));
		f[1][1] = 1;
		for (int i = 1; i < h; i++) {
			for (int j = 1; j < w; j++) {
				for (int k = 0; k < 2; k++) {
					int r = i + mov[k][0];
					int c = j + mov[k][1];
					if (r <= h && c <= w && g[r][c] == 0) {
						f[r][c] = (f[r][c] + f[i][j]) % mod;
					}
				}
			}
		}
		printf("Case #%d: %d\n", casen, f[h][w]);
	}
	return 0;
}

