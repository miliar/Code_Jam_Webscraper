#include <cstdio>

int T, t;
char M[1<<3][1<<3];

int main(void){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	while (T --) {
		for (int c = 0; c < 4; c ++)
			scanf(" %s", M[c]);
		printf("Case #%d: ", ++ t);
		int C = 0;
		for (int r = 0; r < 4; r ++) {
			for (int c = 0; c < 4; c ++) {
				if (M[r][c] != '.') C ++;
			}
		}
		int X, Y, O;
		int winner = -1;
		for (int r = 0; r < 4; r ++) {
			O = X = Y = 0;
			for (int c = 0; c < 4; c ++) {
				if (M[r][c] == 'T') Y ++;
				if (M[r][c] == 'X') X ++;
				if (M[r][c] == 'O') O ++;
			}
			if ((X == 3 && Y == 1) || X == 4) winner = 0;
			if ((O == 3 && Y == 1) || O == 4) winner = 1;
		}
		for (int c = 0; c < 4; c ++) {
			O = X = Y = 0;
			for (int r = 0; r < 4; r ++) {
				if (M[r][c] == 'T') Y ++;
				if (M[r][c] == 'X') X ++;
				if (M[r][c] == 'O') O ++;
			}
			if ((X == 3 && Y == 1) || X == 4) winner = 0;
			if ((O == 3 && Y == 1) || O == 4) winner = 1;
		}
		O = X = Y = 0;
		for (int x = 0; x < 4; x ++) {
			if (M[x][x] == 'T') Y ++;
			if (M[x][x] == 'X') X ++;
			if (M[x][x] == 'O') O ++;
		}
		if ((X == 3 && Y == 1) || X == 4) winner = 0;
		if ((O == 3 && Y == 1) || O == 4) winner = 1;
		O = X = Y = 0;
		for (int x = 0; x < 4; x ++) {
			if (M[3-x][x] == 'T') Y ++;
			if (M[3-x][x] == 'X') X ++;
			if (M[3-x][x] == 'O') O ++;
		}
		if ((X == 3 && Y == 1) || X == 4) winner = 0;
		if ((O == 3 && Y == 1) || O == 4) winner = 1;
		if (winner == -1) {
			if (C < 16) printf("Game has not completed\n");
			else printf("Draw\n");
		} else {
			if (winner == 0) printf("X won\n");
			else printf("O won\n");
		}
	}

	return 0;
}