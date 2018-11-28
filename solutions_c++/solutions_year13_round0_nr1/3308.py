#include <iostream>
#include <string>

using namespace std;

int same(char a, char b, char c, char d) {
	if (a == 'T') a = b;
	if (b == 'T') b = a;
	if (c == 'T') c = a;
	if (d == 'T') d = a;

	if (a == b && b == c && c == d) {
		if (a == 'X') return 1;
		if (a == 'O') return 2;
	}
	return 0;
}

void doit(int casenum) {
	string line[4];

	for (int i = 0; i < 4; ++i) {
		cin >> line[i];
	}

	int winner = 0;

	for (int i = 0; i < 4 && winner == 0; ++i) {
		winner = same(line[i][0], line[i][1], line[i][2], line[i][3]);
		if (winner == 0)
			winner = same(line[0][i], line[1][i], line[2][i], line[3][i]);
	}
	if (winner == 0) {
		winner = same(line[0][0], line[1][1], line[2][2], line[3][3]);
	}
	if (winner == 0) {
		winner = same(line[0][3], line[1][2], line[2][1], line[3][0]);
	}
	/*Case #1: X won
 Case #2: Draw
 Case #3: Game has not completed
*/
	cout << "Case #" << casenum << ": ";

	if (winner == 1) {
		cout << "X won" << endl;
	} else if (winner == 2) {
		cout << "O won" << endl;
	} else {
		bool finished = true;
		for (int i = 0; i < 4; ++i) {
			if (line[i].find('.') != string::npos) {
				finished = false;
				break;
			}
		}
		if (finished) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
	}
}

int main() {
	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		doit(i);
	}

	return 0;
}