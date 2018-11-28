#include <iostream>
#include <string>
#include <sstream>
#include <cassert>

using namespace std;

string bord[5];

bool wins(char c) {
	bool success = true;
	for (int i = 0; i < 4; i++) {
		success = true;
		for (int j = 0; j < 4 && success; j++) {
			if (bord[i][j] != c && bord[i][j] != 'T') success = false;
		}
		if (success) return true;
		success = true;
		for (int j = 0; j < 4 && success; j++) {
			if (bord[j][i] != c && bord[j][i] != 'T') success = false;
		}
		if (success) return true;
	}
	success = true;
	for (int i = 0; i < 4 && success; i++) {
		if (bord[i][i] != c && bord[i][i] != 'T') success = false;
	}
	if (success) return true;
	success = true;
	for (int i = 0; i < 4 && success; i++) {
		if (bord[i][3-i] != c && bord[i][3-i] != 'T') success = false;
	}
	return success;
}

int main() {
	string s;
	getline(cin, s);
	stringstream ss(s);
	int T;
	ss >> T;
	assert(T > 0 && T <= 1000);
	for (int i = 0; i < T; i++) {
		for (int j = 0; j < 5; j++) {
			getline(cin, bord[j]);
			assert(bord[j].size() == (j < 4 ? 4 : 0));
		}
		bool O = wins('O');
		bool X = wins('X');
		bool complete = true;
		for (int j = 0; j < 4 && complete; j++)
			for (int k = 0; k < 4 && complete; k++)
				if (bord[j][k] == '.') complete = false;
		cout << "Case #" << (i + 1) << ": ";
		if (O)
			cout << "O won" << endl;
		else if (X)
			cout << "X won" << endl;
		else if (complete)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}
	return 0;
}
