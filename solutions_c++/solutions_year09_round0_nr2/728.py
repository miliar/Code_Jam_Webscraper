#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_L 101
#define MAX_D 4

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int H, W;
int cell[MAX_L][MAX_L];
int f[MAX_L][MAX_L][2];
char res[MAX_L][MAX_L];
char now;

void find_f() {
	memset(f, -1, sizeof(f));
	for (int i = 0; i< H; ++i)
		for (int j = 0; j < W; ++j) {
			int key_x, key_y;
			int lowest = cell[i][j];
			for (int k = 0; k < MAX_D; ++k) {
				int x = i + dir[k][0];
				int y = j + dir[k][1];
				if (x < 0 || x >= H || y < 0 || y >= W)
					continue;
				if (cell[x][y] < lowest) {
					lowest = cell[x][y];
					key_x = x;
					key_y = y;
				}
			}
			if (lowest < cell[i][j]) {
				f[i][j][0] = key_x;
				f[i][j][1] = key_y;
			}
		}
}

void find_root(int i, int j, int &x, int &y) {
	if (f[i][j][0] == -1) {
		x = i;
		y = j;
		return;
	}
	find_root(f[i][j][0], f[i][j][1], x, y);
	f[i][j][0] = x;
	f[i][j][1] = y;
}

void paint() {
	now = 'a';
	for (int i = 0; i< H; ++i)
		for (int j = 0; j< W; ++j)
			res[i][j] = ' ';

	for (int i = 0; i < H; ++i)
		for (int j = 0; j < W; ++j) {
			int x, y;
			find_root(i, j, x, y);
			if (res[x][y] == ' ') {
				res[i][j] = now;
				res[x][y] = now;
				now++;
			} else
				res[i][j] = res[x][y];
		}
}

int main(int argc, char* argv[]) {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int k = 1; k <= T; ++k) {
		scanf("%d%d", &H, &W);
		for (int i = 0; i < H; ++i)
			for (int j = 0; j< W; ++j)
				scanf("%d", &cell[i][j]);

		find_f();
		
		paint();

		printf("Case #%d:\n", k);
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W - 1; ++j)
				printf("%c ", res[i][j]);
			printf("%c\n", res[i][W-1]);
		}
	}

	return 0;
}
