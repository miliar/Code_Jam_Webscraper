#include <cstdio>
#include <cstring>

using namespace std;

int T;
char game[8][8];

int main() {
	scanf("%d\n", &T);
	for (int c=1 ; c<=T ; c++) {
		for (int i=0 ; i<4 ; i++)
			gets(game[i]);
		scanf("\n");
		int X, O;
		X = O = 0;
		printf("Case #%d: ", c);
		bool winner = false;
		for (int i=0 ; i<4 ; i++) {
			X = O = 0;
			for (int j=0 ; j<4 ; j++) {
				if (game[i][j] == 'T') X++, O++;
				else if (game[i][j] == 'X') X++;
				else if (game[i][j] == 'O') O++;
			}

			if (X == 4) {
				printf("X won\n");
				winner = true;
			}

			if (O == 4) {
				printf("O won\n");
				winner = true;
			}

			if (winner)
				break;
		}

		if (winner)
			continue;

		for (int i=0 ; i<4 ; i++) {
			X = O = 0;
			for (int j=0 ; j<4 ; j++) {
				if (game[j][i] == 'T') X++, O++;
				else if (game[j][i] == 'X') X++;
				else if (game[j][i] == 'O') O++;
			}

			if (X == 4) {
				printf("X won\n");
				winner = true;
			}

			if (O == 4) {
				printf("O won\n");
				winner = true;
			}

			if (winner)
				break;
		}

		if (winner)
			continue;

		X = O = 0;
		for (int i=0 ; i<4 ; i++) {
			if (game[i][i] == 'T') X++, O++;
			else if (game[i][i] == 'X') X++;
			else if (game[i][i] == 'O') O++;
		}

		if (X == 4) {
			printf("X won\n");
			winner = true;
		}

		if (O == 4) {
			printf("O won\n");
			winner = true;
		}

		if (winner)
			continue;

		X = O = 0;
		for (int i=0 ; i<4 ; i++) {
			if (game[i][4-i-1] == 'T') X++, O++;
			else if (game[i][4-i-1] == 'X') X++;
			else if (game[i][4-i-1] == 'O') O++;
		}

		if (X == 4) {
			printf("X won\n");
			winner = true;
		}

		if (O == 4) {
			printf("O won\n");
			winner = true;
		}

		if (winner)
			continue;

		for (int i=0 ; i<4 && !winner ; i++) {
			for (int j=0 ; j<4 && !winner ; j++) {
				if (game[i][j] == '.') {
					printf("Game has not completed\n");
					winner = true;
				}
			}
		}

		if (winner)
			continue;

		printf("Draw\n");

	}
}
