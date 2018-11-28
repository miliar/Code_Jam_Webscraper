#include <algorithm>
#include <climits>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;


char winner(string (&board)[4])
{
	int vertical[4][4] = {0};
	int horizontal[4][4] = {0};
	int diagonalDR[4][4] = {0};
	int diagonalDL[4][4] = {0};

	int numEmpty = 0;

	for(int r=0;r<4;r++) {
		for(int c=0;c<4;c++) {

			if(board[r][c] == '.') {
				numEmpty++;
				continue;
			}

			if(r > 0 && 
				(	(board[r][c] == board[r-1][c]) ||
					(board[r][c] == 'T') ||
					(board[r-1][c] == 'T')
				)
			)
				vertical[r][c] = vertical[r-1][c]+1;

			if(c > 0 && 
				(	(board[r][c] == board[r][c-1]) ||
					(board[r][c] == 'T') ||
					(board[r][c-1] == 'T')
				)
			)
				horizontal[r][c] = horizontal[r][c-1]+1;

			if(r > 0 && c > 0 &&
				(
					(board[r][c] == board[r-1][c-1]) ||
					(board[r][c] == 'T') ||
					(board[r-1][c-1] == 'T')
				)
			)
				diagonalDR[r][c] = diagonalDR[r-1][c-1]+1;

			if(r > 0 && c < 3 &&
				(
					(board[r][c] == board[r-1][c+1]) ||
					(board[r][c] == 'T') ||
					(board[r-1][c+1] == 'T')
				)
			)
				diagonalDL[r][c] = diagonalDL[r-1][c+1]+1;


			if(vertical[r][c] >= 3)
			{
				char winner = board[r][c];
				if(winner == 'T')
					winner = board[r-1][c];

				return winner;
			}

			if(horizontal[r][c] >= 3)
			{
				char winner = board[r][c];
				if(winner == 'T')
					winner = board[r][c-1];

				return winner;
			}

			if(diagonalDR[r][c] >= 3)
			{
				char winner = board[r][c];
				if(winner == 'T')
					winner = board[r-1][c-1];

				return winner;
			}

			if(diagonalDL[r][c] >= 3)
			{
				char winner = board[r][c];
				if(winner == 'T')
					winner = board[r-1][c+1];

				return winner;
			}
		}
	}

	return numEmpty;
}

int main(void)
{
	FILE* fin = fopen("A-small-attempt0.in", "r");
	FILE* fout = fopen("A-small-attempt0.out", "w");

	int numTests;
	fscanf(fin, "%d\n", &numTests);

	for(int testIndex=0;testIndex<numTests;testIndex++)
	{
		char lineBuf[80];
		string board[4];
		for(int i=0;i<4;i++)
		{
			board[i] = fgets(lineBuf, 79, fin);
		}
		fgets(lineBuf, 79, fin);

		char w = winner(board);

		fprintf(fout, "Case #%d: ", testIndex+1);

		if(w == 'X')
			fprintf(fout, "X won");
		else if(w == 'O')
			fprintf(fout, "O won");
		else if(w == 0)
			fprintf(fout, "Draw");
		else
			fprintf(fout, "Game has not completed");

		fprintf(fout, "\n");
	}

	fclose(fin);
	fclose(fout);
}
