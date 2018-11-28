#include <cstdio>
#include <cstring>
const int MAX = 128;
const int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}}; 

int t, H, W;
int almap[MAX][MAX];
int label[MAX][MAX];
int lab = 1;

int find_lowest(int r, int c) {
	int ret = -1;
	int local = almap[r][c], lowest = almap[r][c];
	for (int i = 0; i < 4; ++i) {
		int nr = r + dir[i][0];
		int nc = c + dir[i][1];
		if (nr >= 0 && nc >= 0 && nr < H && nc < W) {
			if (almap[nr][nc] < lowest) {
				ret = i;
				lowest = almap[nr][nc];
			}
		}
	}
	return ret;
}

int find_lowest_label(int r, int c) {
	int lowest_d = find_lowest(r, c);
	if (lowest_d == -1)
		return 0;
	else
		return label[r + dir[lowest_d][0]][c + dir[lowest_d][1]];
}

int flood_fill(int r, int c) {
	int lowest = find_lowest(r, c);
	if (label[r][c] != 0) {
		return label[r][c];
	} else {
		if (lowest != -1) {
			int col = flood_fill(r + dir[lowest][0], c + dir[lowest][1]);
			label[r][c] = col;
			//printf("fill %d %d with %d\n", r, c, col);
			return col;
		} else {
			//printf("sink %d %d col %d\n", r, c, lab);
			return label[r][c] = lab++;
		}
	}
}

int main() {
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		scanf("%d%d", &H, &W);
		lab = 1;
		memset(almap, 0, sizeof(almap));
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) scanf("%d", &almap[i][j]);
		}
		memset(label, 0, sizeof(label));
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (!label[i][j]) flood_fill(i, j);
			}
		}
		printf("Case #%d:\n", kase + 1);
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) printf("%c%s", label[i][j] - 1 + 'a', j == W - 1 ? "\n" : " ");
		}
	}
	return 0;
}

