#include <iostream>
#include <cstdio>

using namespace std;

enum sqv {E, X, O, T};

sqv char_to_sqv(char c);

int main() {
	int tn;
	cin >> tn;
	for (int t = 0; t < tn; t++) {

		// read
		sqv field[4][4];
		bool containsE = false;
		while (getchar() != '\n');
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				field[i][j] = char_to_sqv(getchar());
				containsE = containsE || field[i][j] == E;
			}
			while (getchar() != '\n');
		}

		string* result = NULL;

		// rows
		for (int i = 0; result == NULL && i < 4; i++) {
			sqv winner = (sqv)T;
			for (int j = 0; j < 4; j++) {
				if (winner == T) {
					winner = field[i][j];
				} else if (field[i][j] != T && winner != field[i][j]) {
					winner = E;
				}
			}
			if (winner == X) {
				result = new string("X won");
			} else if (winner == O) {
				result = new string("O won");
			}
		}

		// cols
		for (int i = 0; result == NULL && i < 4; i++) {
			int winner = T;
			for (int j = 0; j < 4; j++) {
				if (winner == T) {
					winner = field[j][i];
				} else if (field[j][i] != T && winner != field[j][i]) {
					winner = E;
				}
			}
			if (winner == X) {
				result = new string("X won");
			} else if (winner == O) {
				result = new string("O won");
			}
		}
		
		// diagonals
		if (result == NULL) {
			int winner = T;
			for (int i = 0; i < 4; i++) {
				if (winner == T) {
					winner = field[i][i];
				} else if (field[i][i] != T && winner != field[i][i]) {
					winner = E;
				}
			}
			if (winner == X) {
				result = new string("X won");
			} else if (winner == O) {
				result = new string("O won");
			}
		}
		if (result == NULL) {
			int winner = T;
			for (int i = 0; i < 4; i++) {
				if (winner == T) {
					winner = field[i][3-i];
				} else if (field[i][3-i] != T && winner != field[i][3-i]) {
					winner = E;
				}
			}
			if (winner == X) {
				result = new string("X won");
			} else if (winner == O) {
				result = new string("O won");
			}
		}


		if (result == NULL) {
			if (containsE) {
				result = new string("Game has not completed");
			} else {
				result = new string("Draw");
			}
		}

		cout << "Case #" << t+1 << ": " << *result << endl;
	}
}

sqv char_to_sqv(char c) {
	switch (c) {
	case 'X':
		return X;
	case 'O':
		return O;
	case 'T':
		return T;
	case '.':
	default:
		return E;
	}
}
