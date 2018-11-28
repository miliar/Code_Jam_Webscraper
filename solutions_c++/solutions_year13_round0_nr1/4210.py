#include <cstdio>

using namespace std;

const int N = 4;
const int MAXN = 100;
char grid[MAXN][MAXN];

bool checkr(int r, char player) {
	char bad = 'X';
	if (bad == player) bad = 'O';
	for(int i = 0; i < N; ++i) {
		if (grid[r][i] == bad || grid[r][i] == '.') return false;
	}
	return true;
}

bool checkc(int c, char player) {
	char bad = 'X';
	if (bad == player) bad = 'O';
	for(int i = 0; i < N; ++i) {
		if (grid[i][c] == bad || grid[i][c] == '.') return false;
	}
	return true;
}

bool checkd1(char player) {
	char bad = 'X';
	if (bad == player) bad = 'O';
	for(int i = 0; i < N; ++i) {
		if (grid[i][i] == bad || grid[i][i] == '.') return false;
	}
	return true;
}

bool checkd2(char player) {
	char bad = 'X';
	if (bad == player) bad = 'O';
	for(int i = 0; i < N; ++i) {
		if (grid[i][N - 1 - i] == bad || grid[i][N - 1 - i] == '.') return false;
	}
	return true;
}

int Q;

int main() {
	scanf("%d", &Q);
	for(int q = 1; q <= Q; ++q) {
		printf("Case #%d: ", q);
		for(int i = 0; i < N; ++i) {
			scanf("%s", grid[i]);
		}

		bool full = true;
		for(int i = 0; i < N; ++i) {
			for(int j = 0; j < N; ++j) {
				if (grid[i][j] == '.') full = false;
			}
		}

		int res = 0;
		for(int i = 0; i < N; ++i) {
			if (checkr(i, 'X') || checkc(i, 'X')) {
				res = 1;
				break;
			} else if (checkr(i, 'O') || checkc(i, 'O')) {
				res = 2;
				break;
			}
		}

		if (checkd1('X') || checkd2('X')) {
			res = 1;
		} else if (checkd1('O') || checkd2('O')) {
			res = 2;
		}

		if (res == 0) {
			if (full) {
				printf("Draw\n");
			} else {
				printf("Game has not completed\n");
			}
		} else if (res == 1) {
			printf("X won\n");
		} else {
			printf("O won\n");
		}
	}

	return 0;
}
