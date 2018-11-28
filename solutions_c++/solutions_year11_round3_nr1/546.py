#include <stdio.h>
const int MAXN = 50;
int n, m;
char map[MAXN][MAXN];
int rest;
int main() {
	int cases;
	scanf("%d", &cases);
	for (int k = 0; k < cases; ++k) {
		printf("Case #%d:\n", k + 1);
		scanf("%d%d\n", &n, &m);
		rest = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%c", &map[i][j]);
				rest += map[i][j] == '#';
			}
			scanf("\n");
		}
		int mini = 0, minj;
		while ((rest > 0) && (rest % 4 == 0)) {
			bool found = false;
			for (int i = mini; i < n; ++i) {
				for (int j = 0; j < m; ++j)
					if (map[i][j] == '#') {
						mini = i;
						minj = j;
						found = true;
						break;
					}
				if (found) break;
			}
			if ((map[mini][minj] == '#') && (map[mini + 1][minj] == '#')
					&& (map[mini][minj + 1] == '#') && (map[mini + 1][minj + 1] == '#')) {
				map[mini][minj] = '/';
				map[mini][minj + 1] = '\\';
				map[mini + 1][minj] = '\\';
				map[mini + 1][minj + 1] = '/';
				rest -= 4;
			} else {
				break;
			}
		}
		if (rest == 0) {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < m; ++j)
					printf("%c", map[i][j]);
				printf("\n");
			}
		} else {
			printf("Impossible\n");
		}
	}
	return 0;
}
