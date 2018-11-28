#include <iostream>
#include <string>
#include <sstream>

using namespace std;

bool finished(char b[][4]) {
	for (int j=0; j<4; j++) {
		for (int i=0; i<4; i++) {
			if (b[j][i]=='.') {
				return false;
			}
		}
	}
	return true;
}

bool be(char c, char a) {
	return (c==a||c=='T')?true:false;
}

bool is(char b[][4], char a) {
	for (int j=0; j<4; j++) {
		if (be(b[j][0], a) && be(b[j][1], a) && be(b[j][2], a) && be(b[j][3], a)) {
			return true;
		} else if (be(b[0][j], a) && be(b[1][j], a) && be(b[2][j], a) && be(b[3][j], a)) {
			return true;
		} 
	}
	if (be(b[0][0], a) && be(b[1][1], a) && be(b[2][2],a ) && be(b[3][3], a)) {
		return true;
	} else if (be(b[0][3], a) && be(b[1][2], a) && be(b[2][1], a) && be(b[3][0], a)) {
		return true;
	}
	return false;
}

int main() {
	int t;
	cin >> t;
	string line;
	getline(cin, line);
	for (int T=1; T<=t; T++) {
		char board[4][4];
		for (int i=0; i<4; i++) {
			getline(cin, line);
			stringstream ccin(line);
			for (int j=0; j<4; j++) {
				ccin >> board[i][j];
			}
		}
		getline(cin, line);
		cout << "Case #" << T << ": ";
		if (is(board, 'O')) {
			cout << "O won" << endl;
		} else if (is(board, 'X')) {
			cout << "X won" << endl;
		} else if (finished(board)) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
	}
	return 0;
}
