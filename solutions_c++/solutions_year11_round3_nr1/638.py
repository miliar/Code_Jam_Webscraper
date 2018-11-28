#include <stdio.h>


int main() {
	int ntc, tc;
	int i, j, k;
	int R, C;
	char colored[100][100];
	scanf("%d", &ntc);
	for (tc = 1; tc <= ntc; tc++) {
		scanf("%d %d", &R, &C);
		for (i = 0; i < R; i++) {
			scanf("%s", colored[i]);
		}
		bool good = true;
		for (i = 0; good && i < R-1; i++) {
			for (j = 0; good && j < C-1; j++) {
				if (colored[i][j] == '#') {
					if (colored[i+1][j] == '#' && colored[i][j+1] == '#' && colored[i+1][j+1] == '#') {
						colored[i][j] = '/';
						colored[i+1][j] = '\\';
						colored[i][j+1] = '\\';
						colored[i+1][j+1] = '/';
					} else {
						good = false;
					}
				}
			}
		}
		for (i = 0; good && i < R; i++) for (j = 0; good && j < C; j++) if (colored[i][j] == '#') good = false;
		printf("Case #%d:\n", tc);
		if (good) {
			for (i = 0; i < R; i++) {
				printf("%s\n", colored[i]);
			}
		} else printf("Impossible\n");
	}
	return 0;
}

