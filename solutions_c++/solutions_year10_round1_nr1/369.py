#include <cstdio>
#include <cstring>

int n, K;
int cnt[55];
char a[55][55];
char b[55][55];

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d", &n, &K);
		for (int i = 0; i < n; i++) {
			scanf("%s", a[i]);
		}
		memset(cnt, 0, sizeof(cnt));
		memset(b, '.', sizeof(b));
		for (int i = 0; i < n; i++) {
			for (int j = n - 1; j >=0; j--) {
				if (a[i][j] != '.') {
					b[cnt[i]++][i] = a[i][j];
				}
			}
		}
		bool red = false, blue = false;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (j + K <= n) {
					bool flag = true;
					for (int k = 1; k < K && flag; k++) {
						flag = (b[i][j] == b[i][j + k]);
					}
					if (flag) {
						if (b[i][j] == 'B') {
							blue = true;
						} else if (b[i][j] == 'R') {
							red = true;
						}
					}
				}
				if (i + K <= n) {
					bool flag = true;
					for (int k = 1; k < K && flag; k++) {
						flag = (b[i][j] == b[i + k][j]);
					}
					if (flag) {
						if (b[i][j] == 'B') {
							blue = true;
						} else {if (b[i][j] == 'R') 
							red = true;
						}
					}
				}
				if (i + K <= n && j + K <= n) {
					bool flag = true;
					for (int k = 1; k < K && flag; k++) {
						flag = (b[i][j] == b[i + k][j + k]);
					}
					if (flag){
						if (b[i][j] == 'B') {
							blue = true;
						} else if (b[i][j] == 'R') {
							red = true;
						}
					}
				}
				if (i - K >= -1 && j + K <= n) {
					bool flag = true;
					for (int k = 1; k < K && flag; k++) {
						flag = (b[i][j] == b[i - k][j + k]);
					}
					if (flag) {
						if (b[i][j] == 'B') {
							blue = true;
						} else if (b[i][j] == 'R') {
							red = true;
						}
					}
				}
			}
		}
		if (red && blue) {
			printf("Case #%d: Both\n", cas);
		} else if (red && !blue) {
			printf("Case #%d: Red\n", cas);
		} else if (!red && blue) {
			printf("Case #%d: Blue\n", cas);
		} else {
			printf("Case #%d: Neither\n", cas);
		}
	}
	return 0;
}
