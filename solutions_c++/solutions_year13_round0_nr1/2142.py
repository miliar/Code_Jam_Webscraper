#include <iostream>
using namespace std;

typedef unsigned int uint;

bool is_row_winner(char const board[4][4], uint row, char player)
{
	for (int j = 0; j < 4; ++j) {
		if (board[row][j] != player && board[row][j] != 'T') return false;
	}
	return true;
}

bool is_column_winner(char const board[4][4], uint column, char player)
{
	for (int i = 0; i < 4; ++i) {
		if (board[i][column] != player && board[i][column] != 'T') return false;
	}
	return true;
}

bool is_main_diagonal_winner(char const board[4][4], char player)
{
	for (int i = 0; i < 4; ++i) {
		if (board[i][i] != player && board[i][i] != 'T') return false;
	}
	return true;
}

bool is_secondary_diagonal_winner(char const board[4][4], char player)
{
	for (int i = 0; i < 4; ++i) {
		if (board[i][4-1-i] != player && board[i][4-1-i] != 'T') return false;
	}
	return true;
}


void solve(char const board[4][4])
{
	//for (uint i = 0; i < 4; ++i) {
	//	for (uint j = 0; j < 4; ++j) {
	//		cout << board[i][j];
	//	}
	//	cout << endl;
	//}
	//return;
	char won = 0;
	// check rows
	for (uint i = 0; i < 4; ++i) {
		if (is_row_winner(board, i, 'O')) won = 'O';
		if (is_row_winner(board, i, 'X')) won = 'X';
	}
	// check columns
	for (uint i = 0; i < 4; ++i) {
		if (is_column_winner(board, i, 'O')) won = 'O';
		if (is_column_winner(board, i, 'X')) won = 'X';
	}
	// check diagonals
	if (is_main_diagonal_winner(board, 'O') || is_secondary_diagonal_winner(board, 'O')) won = 'O';
	if (is_main_diagonal_winner(board, 'X') || is_secondary_diagonal_winner(board, 'X')) won = 'X';
	// print winner
	if (won) {
		cout << won << " won" << endl;
		return;
	}
	// check remaining
	uint remaining = 0;
	for (uint i = 0; i < 4; ++i) {
		for (uint j = 0; j < 4; ++j) {
			if (board[i][j] == '.') remaining++;
		}
	}
	if (!remaining) {
		cout << "Draw" << endl;
		return;
	}
	cout << "Game has not completed" << endl;
}


int main()
{
	uint T;
	char c; // for line breaks
	cin >> T;
	cin.get(c);
	for (uint t = 0; t < T; ++t) {
		char board[4][4];
		for (uint i = 0; i < 4; ++i) {
			for (uint j = 0; j < 4; ++j) {
				cin.get(board[i][j]);
			}
			cin.get(c);
		}
		cin.get(c);	// empty line after every case
		cout << "Case #" << t+1 << ": ";
		solve(board);
	}
	return 0;
}
