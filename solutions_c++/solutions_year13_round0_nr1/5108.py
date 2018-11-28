#include <cstdio>

using namespace std;

int main() {
	int T, t, i, j;
	char board[4][4];
	bool Full, wX, wO;

	scanf("%d\n", &T);

	for (t=0 ; t<T ; t++) {
		for (int i=0 ; i<4 ; i++)
			scanf("%c%c%c%c\n", &board[i][0],
				&board[i][1], &board[i][2], &board[i][3]);

		Full = true;
		wX = false;
		wO = false;
		for (i=0 ; !wX && !wO && i<4 ; i++) {
			for (j=0 ; Full && j<4 ; j++)
				if (board[i][j] == '.')
					Full = false;
			
			wX = true;
			wO = true;
			for (j=0 ; j<4 ; j++) {
				wX = wX && (board[i][j]=='T' || board[i][j]=='X');
				wO = wO && (board[i][j]=='T' || board[i][j]=='O');
			}

			if (wX || wO)
				break;

			wX = true;
			wO = true;
			for (j=0 ; j<4 ; j++) {
				wX = wX && (board[j][i]=='T' || board[j][i]=='X');
				wO = wO && (board[j][i]=='T' || board[j][i]=='O');
			}
		}

		if (!wX && !wO) {
			wX = true;
			wO = true;
			for (i=0 ; i<4 ; i++) {
				wX = wX && (board[i][3-i]=='T' || board[i][3-i]=='X');
				wO = wO && (board[i][3-i]=='T' || board[i][3-i]=='O');
			}
		}

		if (!wX && !wO) {
			wX = true;
			wO = true;
			for (i=0 ; i<4 ; i++) {
				wX = wX && (board[i][i]=='T' || board[i][i]=='X');
				wO = wO && (board[i][i]=='T' || board[i][i]=='O');
			}
		}

		if (wX)			printf("Case #%d: X won\n", t+1);
		else if (wO)	printf("Case #%d: O won\n", t+1);
		else if (Full)	printf("Case #%d: Draw\n", t+1);
		else			printf("Case #%d: Game has not completed\n", t+1);
	}
	return 0;
}
