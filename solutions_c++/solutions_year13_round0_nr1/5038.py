#include <iostream>
#include <string>

using namespace std;

string mat[4];

bool win(char ch) {
	for (int i = 0; i < 4; i++) {
		int c1 = 0, c2 = 0;
		for (int j = 0; j < 4; j++) {
			if (mat[i][j] == ch || mat[i][j] == 'T') {
				c1++;
			}
			if (mat[j][i] == ch || mat[j][i] == 'T') {
				c2++;
			}
		}
		if (c1 == 4 || c2 == 4) return true;
	}
	int c1 = 0, c2 = 0;
	for (int i = 0; i < 4; i++) {
		if (mat[i][i] == ch || mat[i][i] == 'T') {
			c1++;
		}
		if (mat[i][3 - i] == ch || mat[i][3 - i] == 'T') {
			c2++;
		}
		if (c1 == 4 || c2 == 4) return true;
	}
	return false;
}

bool finish() {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (mat[i][j] == '.') {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		for (int i = 0; i < 4; i++) {
			cin >> mat[i];
		}
		cout << "Case #" << t << ": ";
		if (win('X')) {
			cout << "X won" << endl;
		} else if (win('O')) {
			cout << "O won" << endl;
		} else if (finish()) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
	} 
}