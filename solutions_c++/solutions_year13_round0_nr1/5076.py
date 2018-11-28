#include <cstdio>

int main() {
	char table[4][4], winner;
	int T, count_X = 0, count_O = 0, count_T = 0, x, y, i;

	freopen("ttt.in", "r", stdin);
	freopen("ttt.out", "w", stdout);

	scanf("%d\n", &T);
	for (i = 0; i < T; ++i) {
		count_X = 0;
		count_O = 0;
		count_T = 0;
		winner = 'N';
		for (x = 0; x < 4; ++x) {
			for (y = 0; y < 4; ++y) {
				scanf("%c", &table[x][y]);
				if (table[x][y] == 'X')
					++count_X;
				else if (table[x][y] == 'O')
					++count_O;
				else if (table[x][y] == 'T')
					++count_T;
			}
			scanf("\n");
		}
		scanf("\n");
		for (x = 0; (x < 4) and (winner == 'N'); ++x) {
			winner = 'X';
			for (y = 0; y < 4; ++y)
				if ((table[x][y] != 'X') and (table[x][y] != 'T'))
					winner = 'N';
		}
		for (x = 0; (x < 4) and (winner == 'N'); ++x) {
			winner = 'O';
			for (y = 0; y < 4; ++y)
				if ((table[x][y] != 'O') and (table[x][y] != 'T'))
					winner = 'N';
		}
		for (y = 0; (y < 4) and (winner == 'N'); ++y) {
			winner = 'X';
			for (x = 0; x < 4; ++x)
				if ((table[x][y] != 'X') and (table[x][y] != 'T'))
					winner = 'N';
		}
		for (y = 0; (y < 4) and (winner == 'N'); ++y) {
			winner = 'O';
			for (x = 0; x < 4; ++x)
				if ((table[x][y] != 'O') and (table[x][y] != 'T'))
					winner = 'N';
		}
		if (winner == 'N') {
			winner = 'X';
			for (x = 0; x < 4; ++x)
				if ((table[x][x] != 'X') and (table[x][x] != 'T'))
					winner = 'N';
		}
		if (winner == 'N') {
			winner = 'O';
			for (x = 0; x < 4; ++x)
				if ((table[x][x] != 'O') and (table[x][x] != 'T'))
					winner = 'N';
		}
		if (winner == 'N') {
			winner = 'X';
			for (x = 0; x < 4; ++x)
				if ((table[x][3 - x] != 'X') and (table[x][3 - x] != 'T'))
					winner = 'N';
		}
		if (winner == 'N') {
			winner = 'O';
			for (x = 0; x < 4; ++x)
				if ((table[x][3 - x] != 'O') and (table[x][3 - x] != 'T'))
					winner = 'N';
		}

	if (winner != 'N')
		printf("Case #%d: %c won\n", i + 1, winner);
	else if (16 - count_X - count_O - count_T == 0)
		printf("Case #%d: Draw\n", i + 1);
	else
		printf("Case #%d: Game has not completed\n", i + 1);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}




