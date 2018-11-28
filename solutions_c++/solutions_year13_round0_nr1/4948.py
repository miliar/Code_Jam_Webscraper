#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("a.out");
char field[4][4];
enum State {XWIN, OWIN, DRAW, INCOMPLETE};

bool isValid(char c1, char c) {
	return c1 == c || c1 == 'T';
}

bool rowComp(int row, char c) {
	for (int i = 0; i < 4; i++) {
		if (!isValid(field[row][i], c))
			return false;
	}

	return true;
}

bool colComp(int col, char c) {
	for (int i = 0; i < 4; i++) {
		if (!isValid(field[i][col], c))
			return false;
	}

	return true;
}

bool diag1(char c) {
	for (int i = 0; i < 4; i++) {
		if (!isValid(field[i][i], c))
			return false;
	}

	return true;
}

bool diag2(char c) {
	for (int i = 0; i < 4; i++) {
		if (!isValid(field[i][3 - i], c))
			return false;
	}

	return true;
}

bool wins(char c) {
	for (int i = 0; i < 4; i++) {
		if (rowComp(i, c))
			return true;
		if (colComp(i, c))
			return true;
	}

	if (diag1(c))
		return true;
	if (diag2(c))
		return true;

	return false;
}

bool finished() {
	for (int i = 0; i < 4; i++) {
		for (int k = 0; k < 4; k++) {
			if (field[i][k] == '.')
				return false;
		}
	}

	return true;
}

State getResult() {
	State s = INCOMPLETE;

	if (wins('X'))
		s = XWIN;
	else if (wins('O'))
		s = OWIN;
	else if (finished())
		s = DRAW;

	return s;
}

int main() {
	int nCases;
	cin >> nCases;

	for (int cnt = 1; cnt <= nCases; cnt++) {
		for (int i = 0; i < 4; i++) {
			for (int k = 0; k < 4; k++) {
				cin >> field[i][k];
			}
		}

		cout << "Case #" << cnt << ": ";
		State s = getResult();
		switch (s) {
		case XWIN:
			cout << "X won" << endl;
			break;
		case OWIN:
			cout << "O won" << endl;
			break;
		case DRAW:
			cout << "Draw" << endl;
			break;
		default:
			cout << "Game has not completed" << endl;
			break;
		}
	}

	return 0;
}
