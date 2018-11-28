#include <iostream>
#include <string>
using namespace std;

char board[4][4];

void read_input() {
	char newline;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> board[i][j];
		}
	}
}

void print_board() {
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cout << board[i][j];
		}
		cout << "\n";
	}
}

string solve() {
	bool haveEmpty = false;
	bool haveT = false;
	int xCount = 0;
	int oCount = 0;

	/// Check row
	for (int i = 0; i < 4; ++i) {
		haveT = false;
		xCount = oCount = 0;
		for (int j = 0; j < 4; ++j) {
			switch (board[i][j]) {
				case 'X': xCount+=1; break;
				case 'O': oCount++; break;
				case 'T': haveT = true; break;
				default: haveEmpty = true; break;
			}
		}
		if ((xCount==4) || (xCount==3&&haveT)) return "X won";
		if ((oCount==4) || (oCount==3&&haveT)) return "O won";
	}

	/// Check column
	for (int i = 0; i < 4; ++i) {
		haveT = false;
		xCount = oCount = 0;
		for (int j = 0; j < 4; ++j) {
			switch (board[j][i]) {
				case 'X': xCount++; break;
				case 'O': oCount++; break;
				case 'T': haveT = true; break;
				default: haveEmpty = true; break;
			}
		}
		if ((xCount==4) || (xCount==3&&haveT)) return "X won";
		if ((oCount==4) || (oCount==3&&haveT)) return "O won";
	}

	/// Check diagonal 1
	haveT = false;
	xCount = oCount = 0;
	for (int i = 0; i < 4; ++i) {
		switch (board[i][i]) {
			case 'X': xCount++; break;
			case 'O': oCount++; break;
			case 'T': haveT = true; break;
			default: haveEmpty = true; break;
		}
	}
	if ((xCount==4) || (xCount==3&&haveT)) return "X won";
	if ((oCount==4) || (oCount==3&&haveT)) return "O won";

	/// Check diagonal 2
	haveT = false;
	xCount = oCount = 0;
	for (int i = 0; i < 4; ++i) {
		switch (board[i][3-i]) {
			case 'X': xCount++; break;
			case 'O': oCount++; break;
			case 'T': haveT = true; break;
			default: haveEmpty = true; break;
		}
	}
	if ((xCount==4) || (xCount==3&&haveT)) return "X won";
	if ((oCount==4) || (oCount==3&&haveT)) return "O won";


	if (haveEmpty) return "Game has not completed";
	else return "Draw";
}

int main(int argc, char const *argv[])
{
	int t,T;

	cin >> T;

	for (t = 1; t <= T; ++t) {
		read_input();
		//print_board();

		cout << "Case #" << t << ": " << solve() << "\n";
	}

	return 0;
}
