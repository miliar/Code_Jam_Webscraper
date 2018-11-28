#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
int alt[100][100];
int mark[100][100];
char alter[10000];
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
int H, W;

int get_mark(int x, int y) {
	if (mark[x][y] != -1) return mark[x][y];
	int i, minalt = 100000;
	for (i = 0; i < 4; i++) {
		if (x + dx[i] >= 0 && x + dx[i] < H 
		&& y + dy[i] >= 0 && y + dy[i] < W) {
			if (minalt > alt[x + dx[i]][y + dy[i]]) {
				minalt = alt[x + dx[i]][y + dy[i]];
			}
		}
	}
	if (minalt >= alt[x][y]) return mark[x][y] = x * 100 + y;
	for (i = 0; i < 4; i++) {
		if (x + dx[i] >= 0 && x + dx[i] < H 
		&& y + dy[i] >= 0 && y + dy[i] < W && minalt == alt[x + dx[i]][y + dy[i]]) {
			return mark[x][y] = get_mark(x + dx[i], y + dy[i]);
		}
	}
}

int main() {
	int T;
	int i, j;
	char key;
	int t = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &H, &W);
		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++) {
				scanf("%d", &alt[i][j]);
			}
		}
		memset(mark, -1, sizeof(mark));
		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++) {
				get_mark(i, j);
				//printf("%d ", mark[i][j]);
			}
		}
		memset(alter, 0, sizeof(alter));
		key = 'a';
		printf("Case #%d:\n", t++);
		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++) {
				if (alter[mark[i][j]] == 0) {
					alter[mark[i][j]] = key++;
				}
				if (j > 0) putchar(' ');
				putchar(alter[mark[i][j]]);
			}
			putchar(10);
		}
	}
	return 0;
}
