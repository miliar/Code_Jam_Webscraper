#include <cstdio>
#define N 4

char B[N][N];

bool check_left_diagonal(char c) {
	for (int i = 0; i < N; ++ i) {
		if (B[i][i] != 'T' && B[i][i] != c)
				return false;
	}
	return true;
}

bool check_right_diagonal(char c) {
	for (int i = 0; i < N; ++ i) {
		if (B[i][N-i-1] != 'T' && B[i][N-i-1] != c)
				return false;
	}
	return true;
}

bool check_unfinished() {
	for (int i = 0; i < N; ++ i)
		for (int j = 0; j < N; ++ j)
			if (B[i][j] == '.')
				return true;
	return false;
}

bool check_row(int row, int c) {
	for (int i = 0; i < N; ++i) {
		if (B[row][i] != 'T' && B[row][i] != c) {
			return false;		
		}
	}
	return true;
}

bool check_col(int col, int c) {
	for (int i = 0; i < N; ++i) {
		if (B[i][col] != 'T' && B[i][col] != c) {
			return false;		
		}
	}
	return true;
}

int check_win(int c) {
	if (check_left_diagonal(c) || check_right_diagonal(c)) {
		return true;
	}
	for (int i = 0; i < N; ++i) {
		if (check_row(i, c) || check_col(i, c)) {
			return true;
		}
	}
	return false;
}

int main() {
	
	int t;
	scanf("%d", &t);

	for (int z = 1; z <= t; ++ z) {
		for(int i = 0; i < N; ++ i) {
			scanf("%s", B[i]);
		}
		printf("Case #%d: ", z);

		if (check_win('X')) {
			printf("X won\n");
		} else if (check_win('O')) {
			printf("O won\n");
		} else if (check_unfinished()) {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}
	}

}
