// a.cpp
// Tic-Tac-Toe-Tomek
//

#include <iostream>
#include <string>
using namespace std;

const char InitialSymbol = 'T';
const char EmptySquare = '.';

bool win(const string board[], char symbol)
{
	// horizontal
	for (int r = 0 ; r < 4 ; r++) {
		bool bWin = true;
		for (int c = 0 ; c < 4 ; c++) {
			if (board[r][c] != symbol && board[r][c] != InitialSymbol) {
				bWin = false;
				break;
			}
		}
		if (bWin)
			return true;
	}

	// vertical
	for (int c = 0 ; c < 4 ; c++) {
		bool bWin = true;
		for (int r = 0 ; r < 4 ; r++) {
			if (board[r][c] != symbol && board[r][c] != InitialSymbol) {
				bWin = false;
				break;
			}
		}
		if (bWin)
			return true;
	}

	// diagonal 1
	bool bWin = true;
	for (int r = 0 ; r < 4 ; r++) {
		if (board[r][r] != symbol && board[r][r] != InitialSymbol) {
			bWin = false;
			break;
		}
	}
	if (bWin)
		return true;

	// diagonal 2
	bWin = true;
	for (int r = 0 ; r < 4 ; r++) {
		if (board[r][3-r] != symbol && board[r][3-r] != InitialSymbol) {
			bWin = false;
			break;
		}
	}
	if (bWin)
		return true;

	return false;
}

int main()
{
	int T;
	
	cin >> T;
	getchar();
	for (int t = 1 ; t <= T ; t++) {
		string board[4];
		char ans = 'D';

		for (int r = 0 ; r < 4 ; r++)
			getline(cin, board[r]);
		if (t < T)
			getchar();
		
		
		if (win(board, 'X'))	// X
			ans = 'X';
		else if (win(board, 'O'))	// O
			ans = 'O';
		else {	// Draw or Not Completed
			for (int r = 0 ; r < 4 ; ++r)
			for (int c = 0 ; c < 4 ; ++c)
				if (board[r][c] == EmptySquare)
					ans = 'N';
		}
		

		if (t > 1)
			cout << endl;
		cout << "Case #" << t << ": ";
		switch(ans) {
		case 'X':
			cout << "X won";
			break;
		case 'O':
			cout << "O won";
			break;
		case 'N':
			cout << "Game has not completed";
			break;
		case 'D':
			cout << "Draw";
			break;
		}
	}

	return 0;
}