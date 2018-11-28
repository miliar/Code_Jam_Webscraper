#include <iostream>
#include <string>

using namespace std;

string solve(string * board) {
	int x[4] = { 0 };
	int o[4] = { 0 };
	int open = 0;
	for( int r = 0; r < 4; r++ ) {
		x[0] = x[1] = o[0] = o[1] = 0;
		for( int c = 0; c < 4; c++ ) {
			if ( board[r][c] == 'X' ) x[0]++;
			if ( board[r][c] == 'O' ) o[0]++;
			if ( board[r][c] == 'T' ) { x[0]++; o[0]++; }

			if ( board[c][r] == 'X' ) x[1]++;
			if ( board[c][r] == 'O' ) o[1]++;
			if ( board[c][r] == 'T' ) { x[1]++; o[1]++; }

			if ( board[r][c] == '.' ) open++;
		}

		if ( x[0] == 4 || x[1] == 4 ) {
			return "X won";
		}
		if ( o[0] == 4 || o[1] == 4 ) {
			return "O won";
		}

		if ( board[r][r] == 'X' ) x[2]++;
		if ( board[r][r] == 'O' ) o[2]++;
		if ( board[r][r] == 'T' ) { x[2]++; o[2]++; }

		int c = 4 - r - 1;
		if ( board[r][c] == 'X' ) x[3]++;
		if ( board[r][c] == 'O' ) o[3]++;
		if ( board[r][c] == 'T' ) { x[3]++; o[3]++; }
	}

	if ( x[2] == 4 || x[3] == 4 ) {
		return "X won";
	}
	if ( o[2] == 4 || o[3] == 4 ) {
		return "O won";
	}

	if ( open == 0 ) { 
		return "Draw";
	}
	return "Game has not completed";
}

int main() {
	int numCases;
	cin >> numCases;

	for (int c = 1; c <= numCases; c++) {
		string board[4];
		for (int i = 0; i < 4; i++) {
			cin >> board[i];
		}
		cout << "Case #" << c << ": " << solve(board) << endl;
	}

	return 1;
}