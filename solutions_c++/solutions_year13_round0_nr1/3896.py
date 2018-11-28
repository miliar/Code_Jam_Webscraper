#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

// Setup the initial game state flags
char board[5][5];
bool x_win=false, o_win=false, in_prog=false;

void checkGameStat(char boardRow[])
{
	int x=0, o=0, t=0;
	// Check the different game states
	for (int i=0; i<4;i++)
	{
		if (boardRow[i]=='X') x++;
		else if (boardRow[i]=='O') o++;
		else if (boardRow[i]=='T') t++;
		else in_prog=true;
	}

	if (x==4 || (x==3 && t==1)) x_win = true;
	if (o==4 || (o==3 && t==1)) o_win = true;
}

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int C;
	scanf("%d",&C);

	for (int test=1;test<=C;test++) {
		char board_row[4];
		char board_row2[4];

		// Reset flags
		x_win=false, o_win=false, in_prog=false;

		// Read the board
		for (int i=0; i<4;i++)
			cin >> board[i];

		// Now check the win by row
		for (int i=0; i<4;i++)
		{
			for (int j=0; j<4;j++)
			{
				board_row[j]=board[i][j];
				board_row2[j]=board[j][i];
			}
			// Check both row and column rows
			checkGameStat(board_row);
			checkGameStat(board_row2);
		}

		// Finally check diagonals too
		for (int i=0, j=0, k=3; i<4;i++)
		{
			board_row[j]=board[i][j++];
			board_row2[i]=board[i][k--];
		}
		checkGameStat(board_row);
		checkGameStat(board_row2);

		// Print the results
		string s="";
		if (x_win) s = "X won";
		else if (o_win) s = "O won";
		else if (in_prog) s = "Game has not completed";
		else s = "Draw";

		cout << "Case #" << test << ": " << s << endl;
	}
}
