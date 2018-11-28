#include <iostream>
#include <string>
#include <cassert>
using namespace std;

char matrix[4][5];

inline char check(char &a, char &b, char &c, char &d) {
	if ((a == 'X' || a == 'T') && (b == 'X' || b == 'T')
			&& (c == 'X' || c == 'T') && (d == 'X' || d == 'T'))
		return 'X';
	if ((a == 'O' || a == 'T') && (b == 'O' || b == 'T')
			&& (c == 'O' || c == 'T') && (d == 'O' || d == 'T'))
		return 'O';
	else
		return 'U';
}

inline char check_row(int row) {
	return check(matrix[row][0], matrix[row][1], matrix[row][2], matrix[row][3]);
}

inline char check_column(int column) {
	return check(matrix[0][column], matrix[1][column], matrix[2][column],
			matrix[3][column]);
}

inline char check_diagonals() {
	char result1 = check(matrix[0][0], matrix[1][1], matrix[2][2],
			matrix[3][3]);
	char result2 = check(matrix[0][3], matrix[1][2], matrix[2][1],
			matrix[3][0]);
	if (result1 == 'X' || result2 == 'X')
		return 'X';
	if (result1 == 'O' || result2 == 'O')
		return 'O';
	else
		return 'U';
}

char check_matrix() {
	for (int i = 0; i < 4; i++) {
		char result_row = check_row(i);
		char result_column = check_column(i);
		if (result_row == 'X' || result_column == 'X')
			return 'X';
		if (result_row == 'O' || result_column == 'O')
			return 'O';
	}
	char result_diagonal = check_diagonals();
	if (result_diagonal == 'X')
		return 'X';
	if (result_diagonal == 'O')
		return 'O';
	bool dot_exist = false;
	for (int row = 0; row < 3 && !dot_exist; row++) {
		for (int column = 0; column < 3 && !dot_exist; column++) {
			if (matrix[row][column] == '.')
				dot_exist = true;
		}
	}
	if (dot_exist)
		return 'G';
	else
		return 'D';
}

int main() {
	int T;
	cin >> T;
	for (int cases = 1; cases <= T; cases++) {
		for (int i = 0; i < 4; i++)
			cin >> matrix[i];
		char result = check_matrix();

		cout << "Case #"<< cases << ": ";
		switch (result) {
		case 'X':
			cout << "X won" << endl;
			break;
		case 'O':
			cout << "O won" << endl;
			break;
		case 'D':
			cout << "Draw" << endl;
			break;
		case 'G':
			cout << "Game has not completed" << endl;
			break;
		}
	}
}
