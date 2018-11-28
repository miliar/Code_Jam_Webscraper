
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main() {

	int cases;
	scanf("%d\n", &cases);

	for (int caseNo=0; caseNo < cases; caseNo++) {

		char board[4][10];

		for (int i=0; i<4; i++) {
			memset(board+i, 0, sizeof(char)*10);
		}

		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {

				char s;
				scanf("%c", &s);

				int c = 0;
				     if (s == 'X') {c = 1;}
				else if (s == 'O') {c = 2;}
				else if (s == 'T') {c = 3;}

				board[c][i]++;
				board[c][4+j]++;

				if (i==j)   {board[c][8]++;}
				if (i+j==3) {board[c][9]++;}
				
			}
			scanf("\n");
		}

		int empty = 0;
		char winner = 0;
		for (int i=0; i<10; i++) {
			empty += board[0][i];

			if (board[1][i] + board[3][i] == 4) {
				winner = 'X';
				break;
			}
			if (board[2][i] + board[3][i] == 4) {
				winner = 'O';
				break;
			}
		}

		printf("Case #%d: ", caseNo+1);
		if (winner != 0) {
			printf("%c won\n", winner);
		} else if (empty != 0) {
			printf("Game has not completed\n");
		} else {
			printf("Draw\n");
		}

		scanf("\n");
	}


	return 0;
}