#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

char Board[4][4];

ifstream fin("atxt.in");
ofstream fout("atxt.out");

bool check(char ch) {
	// Vertical
	for (int r, c=0; c<4; ++c) {
		for (r=0; r<4; ++r) {
			if (Board[r][c] == 'T') continue;
			if (Board[r][c] == '.' || Board[r][c] != ch) break;
		}
		if (r >= 4) return true;
	}
	// Horizontal
	for (int c, r=0; r<4; ++r) {
		for (c=0; c<4; ++c) {
			if (Board[r][c] == 'T') continue;
			if (Board[r][c] == '.' || Board[r][c] != ch) break;
		}
		if (c >= 4) return true;
	}
	// Diagonal
	// backslash
	int i;
	for (i=0; i<4; ++i) {
		if (Board[i][i] == 'T') continue;
		if (Board[i][i] == '.' || Board[i][i] != ch) break;
	}
	if (i >= 4) return true;
	// slash
	for (i=0; i<4; ++i) {
		if (Board[i][3-i] == 'T') continue;
		if (Board[i][3-i] == '.' || Board[i][3-i] != ch) break;		
	}
	if (i >= 4) return true;
	return false;
}

int main() {
	int testcase, N, M;
	//cin >> testcase;
	fin >> testcase;
	for (int tc=1; tc<=testcase; ++tc) {
		string line;
		bool incomplete = false;
		for (int i=0; i<4; ++i) {
			//cin >> line;
			fin >> line;
			for (int j=0; j<4; ++j) {
				Board[i][j] = line[j];
				if (line[j] == '.') incomplete = true;
			}
		}
		// Check X
		bool cx = check('X');
		bool co = check('O');
		//cout << "Case #" << tc << ": ";
		fout << "Case #" << tc << ": ";
		if (cx && co) {
			//cout << "Draw";
			fout << "Draw";
		} else if (cx && !co) {
			//cout << "X won";
			fout << "X won";
		} else if (!cx && co) {
			//cout << "O won";
			fout << "O won";
		} else if (!cx && !co) {
			if (incomplete) {
				//cout << "Game has not completed";
				fout << "Game has not completed";
			} else {
				//cout << "Draw";
				fout << "Draw";
			}
		}
		//cout << endl;
		fout << endl;
	}

	return 0;
}