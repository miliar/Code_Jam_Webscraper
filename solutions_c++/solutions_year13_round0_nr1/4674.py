#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool hasWon(string board[], char p)
{
	int tR = -1, tC = -1;
	for (int r = 0; r < 4; r++)
		for (int c = 0; c < 4; c++)
			if (board[r][c] == 'T') { tR = r; tC = c; }
	bool flag = false;
	if (tR != -1) board[tR][tC] = p;
	for (int r = 0; r < 4 && !flag; r++)
		if (board[r][0] == p && board[r][1] == p && board[r][2] == p && board[r][3] == p ||
			board[0][r] == p && board[1][r] == p && board[2][r] == p && board[3][r] == p)
				flag = true;
	if (board[0][0] == p && board[1][1] == p && board[2][2] == p && board[3][3] == p ||
		board[3][0] == p && board[2][1] == p && board[1][2] == p && board[0][3] == p)
			flag = true;
	if (tR != -1) board[tR][tC] = 'T';
	return flag;
}

int main()
{
	ifstream fin("in.in");
	ofstream fout("out.out");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		string board[4];
		fin >> board[0] >> board[1] >> board[2] >> board[3];
		bool xWon = hasWon(board, 'X');
		bool oWon = hasWon(board, 'O');
		bool hasBlanks = false;
		for (int r = 0; r < 4; r++)
			for (int c = 0; c < 4; c++)
				if (board[r][c] == '.') hasBlanks = true;
		string status;
		if (xWon) status = "X won";
		else if (oWon) status = "O won";
		else if (!hasBlanks) status = "Draw";
		else status = "Game has not completed";
		fout << "Case #" << t << ": " << status << endl;
	}
}