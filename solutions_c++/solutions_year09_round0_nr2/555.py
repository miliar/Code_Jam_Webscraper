#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char map[200][200];
int alt[200][200], h, w;
char next;

char fill(int i, int j)
{
	bool flow = false;
	int fi, fj;
	if (map[i][j] != 0) return map[i][j];
	if (i > 0) {
		if (alt[i - 1][j] < alt[i][j] && (!flow || alt[i - 1][j] < alt[fi][fj])) {
			flow = true;
			fi = i - 1; fj = j;
		}
	}
	if (j > 0) {
		if (alt[i][j - 1] < alt[i][j] && (!flow || alt[i][j - 1] < alt[fi][fj])) {
			flow = true;
			fi = i; fj = j - 1;
		}
	}
	if (j < w - 1) {
		if (alt[i][j + 1] < alt[i][j] && (!flow || alt[i][j + 1] < alt[fi][fj])) {
			flow = true;
			fi = i; fj = j + 1;
		}
	}
	if (i < h - 1) {
		if (alt[i + 1][j] < alt[i][j] && (!flow || alt[i + 1][j] < alt[fi][fj])) {
			flow = true;
			fi = i + 1; fj = j;
		}
	}
	if (!flow) map[i][j] = next++;
	else map[i][j] = fill(fi, fj);
	return map[i][j];
}

int main()
{
	int cases, cas, i, j;
	scanf("%d", &cases);
	for (cas = 1; cas <= cases; cas++) {
		scanf("%d%d", &h, &w);
		for (i = 0; i < h; i++) {
			for (j = 0; j < w; j++) scanf("%d", &alt[i][j]);
		}
		next = 'a';
		memset(map, 0, sizeof(map));
		for (i = 0; i < h; i++) {
			for (j = 0; j < w; j++) {
				fill(i, j);
			}
		}
		printf("Case #%d:\n", cas);
		for (i = 0; i < h; i++) {
			for (j = 0; j < w; j++) printf("%c ", map[i][j]);
			printf("\n");
		}
	}
	return 0;
}
