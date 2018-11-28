#include <fstream>
#include <string>
using namespace std;

string board[4];
ifstream in("input_a.txt");
ofstream out("output_a.txt");

bool check_row(int row, char ch) {
	int count = 0;

	for (int i = 0; i < 4; i++) {
		if (board[row][i] == ch) {
			count += 1;
		}
		else if (board[row][i] != 'T') {
			return false;
		}
	}
	return count >= 3;
}

bool check_col(int col, char ch) {
	int count = 0;

	for (int i = 0; i < 4; i++) {
		if (board[i][col] == ch) {
			count += 1;
		}
		else if (board[i][col] != 'T') {
			return false;
		}
	}
	return count >= 3;
}

bool check_diag(char ch) {
	int count = 0;

	for (int i = 0; i < 4; i++) {
		if (board[i][i] == ch) {
			count += 1;
		}
		else if (board[i][i] != 'T') {
			return false;
		}
	}
	return count >= 3;
}

bool check_rev_diag(char ch) {
	int count = 0;

	for (int i = 0; i < 4; i++) {
		if (board[i][3 - i] == ch) {
			count += 1;
		}
		else if (board[i][3 - i] != 'T') {
			return false;
		}
	}
	return count >= 3;
}

int compute() {
	for (int i = 0; i < 4; i++) {
		if (check_row(i, 'X')) {
			return 1;
		}
		else if (check_row(i, 'O')) {
			return 2;
		}
	}

	for (int i = 0; i < 4; i++) {
		if (check_col(i, 'X')) {
			return 1;
		}
		else if (check_col(i, 'O')) {
			return 2;
		}
	}

	if (check_diag('X') || check_rev_diag('X')) {
		return 1;
	}
	else if (check_diag('O') || check_rev_diag('O')) {
		return 2;
	}

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == '.') {
				return 4;
			}
		}
	}
	return 3;
}

int main() {
	int t;
	in >> t;

	for (int i = 0; i < t; i++) {
		for (int j = 0; j < 4; j++) {
			in >> board[j];
		}
		in.ignore();

		out << "Case #" << (i + 1) << ": ";
		switch (compute()) {
			case 1:
				out << "X won\n";
				break;
			case 2:
				out << "O won\n";
				break;
			case 3:
				out << "Draw\n";
				break;
			case 4:
				out << "Game has not completed\n";
				break;
		}
	}
	return 0;
}
