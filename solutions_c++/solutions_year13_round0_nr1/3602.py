#include <cstdio>

const int SZ = 8;
const int DIRX[8][2]={{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1}};
char graph[SZ][SZ];

bool walk(char player, int row, int col, int dir, int remain) {
	if (remain == 1) return true;
	int nr = row + DIRX[dir][0];
	int nc = col + DIRX[dir][1];
	if (nr >= 0 && nc >= 0 && nr < 4 && nc < 4) {
		if (graph[nr][nc] == player || graph[nr][nc] == 'T') {
			return walk(player, nr, nc, dir, remain - 1);
		}
	}
	return false;
}

bool check(int row, int col) {
	char c = graph[row][col];
	if (c != 'X' && c != 'O') {
		return false;
	}
	for (int i = 0; i < 8; ++i) {
		if (walk(graph[row][col], row, col, i, 4)) {
			return true;
		}
	}
	return false;
}

int main() {
	int N;
	scanf("%d", &N);
	for (int kase = 0; kase < N; ++kase) {
		for (int i = 0; i < 4; ++i)
			scanf("%s", graph[i]);
		char winner = ' ';
		bool completed = true;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (graph[i][j] == '.')
					completed = false;
				if (check(i, j)) {
					winner = graph[i][j];
					break;
				}
			}
		}
		printf("Case #%d: ", kase + 1);
		if (winner != ' ') {
			printf("%c won\n", winner);
		} else if (completed) {
			printf("Draw\n");
		} else {
			printf("Game has not completed\n");
		}
	}
	return 0;
}
