#include <cstdio>

using namespace std;

int main()
{
	int T;
	
	scanf("%d", &T);
	
	for (int testcase = 1; testcase <= T; testcase++){
		char board[4][5];
		int Ti = -1, Tj = -1;
		for (int i = 0; i < 4; i++)
			scanf("%s", board[i]);
		
		bool dflag = true;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (board[i][j] == '.') dflag = false;
				else if (board[i][j] == 'T'){
					Ti = i; Tj = j;
				}
			}
		}
		
		int state = -1;
		
		if (~Ti) board[Ti][Tj] = 'X';
		int row[4] = {0}, col[4] = {0}, diag[2] = {0};
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				row[i] += (board[i][j] == 'X');
				col[j] += (board[i][j] == 'X');
				if (i == j) diag[0] += (board[i][j] == 'X');
				if (i + j == 3) diag[1] += (board[i][j] == 'X');
			}
		}
		
		for (int i = 0; i < 4; i++){
			if (row[i] == 4 || col[i] == 4|| (i < 2 && diag[i] == 4)) state = 1;
		}
		for (int i = 0; i < 4; i++){
			col[i] = row[i] = 0;
			if (i < 2) diag[i] = 0;
		}
		
		if (~Ti) board[Ti][Tj] = 'O';
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				row[i] += (board[i][j] == 'O');
				col[j] += (board[i][j] == 'O');
				if (i == j) diag[0] += (board[i][j] == 'O');
				if (i + j == 3) diag[1] += (board[i][j] == 'O');
			}
		}
		
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 2; j++)
				if (row[i] == 4 || col[i] == 4 || (i < 2 && diag[i] == 4)) state = 0;
		}
		
		printf("Case #%d: ", testcase);
		if (state >= 0) printf("%c won\n", state ? 'X' : 'O');
		else printf("%s\n", dflag ? "Draw" : "Game has not completed");
	}
	
	return (0);
}
