#include <cstdio>
#include <cstring>

const int DIRX[8][2]={{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1}};
char RET[4][8] = {"Neither", "Red", "Blue", "Both"};

char map[64][64];
char rotated[64][64];
int T, K, N;

int dfs(int r, int c, char x, int dir) {
	int nr = r + DIRX[dir][0];
	int nc = c + DIRX[dir][1];
	if (nr >= 0 && nc >= 0 && nr < N && nc < N && rotated[nr][nc] == x) {
		return dfs(nr, nc, x, dir) + 1;
	}
	return 1;
}

int check(int r, int c, char x) {
	int ret = 0;
	for (int i = 0; i < 8; ++i) {
		ret >?= dfs(r, c, x, i);
	}
	return ret;
}


int main() {
	scanf("%d", &T);
	for (int kase = 0; kase < T; ++kase) {
		scanf("%d%d", &N, &K);
		memset(map, 0, sizeof(map));
		memset(rotated, 0, sizeof(rotated));
		scanf(" ");
		for (int i = 0; i < N; ++i) {
			scanf("%s", map[i]);
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				rotated[j][N-i-1] = map[i][j];
			}
		}
		for (int i = 0; i < N; ++i) {
			bool fall = true;
			while (fall) {
				int room  = -1;
				bool chg = false;
				for (int j = N-1; j >=0; --j) {
					if (room != -1 && rotated[j][i] != '.') {
						rotated[room][i] = rotated[j][i];
						rotated[j][i] = '.';
						chg = true;
						break;
					} else if (room == -1 && rotated[j][i] == '.') {
						room = j;
					}
				}
				if (room == -1 || chg == false)
					fall = false;
			}
		}
		int cntr = 0, cntb = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (rotated[i][j] == 'R') {
					cntr >?= check(i, j, 'R');
				} else if (rotated[i][j] == 'B') {
					cntb >?= check(i, j, 'B');
				}
			}
		}
		int ret = (cntr >= K) + (cntb >= K) * 2;
		printf("Case #%d: %s\n", kase + 1, RET[ret]);
	}
	return 0;
}

