#include <iostream>
#include <fstream>

#define FOR(i,n) for(int i = 0; i < (n); ++i)

using namespace std;

int main() {
	ifstream fin("a2.in");
	ofstream fout("a2.out");
	int t;
	fin >> t;
	char a[4][4];
	for (int tt = 1; tt <= t; ++tt) {
		FOR(i,4)
			FOR(j,4)
				fin >> a[i][j];
		int empty = 0;
		bool oWon = false, xWon = false;
		FOR(i,4) {
			int o = 0, x = 0;
			FOR(j,4) {
				if (a[i][j] == 'O') ++o;
				else if (a[i][j] == 'X') ++x;
				else if (a[i][j] == 'T') { ++o; ++x; }
				else if (a[i][j] == '.') { ++empty; }
			}
			if (o == 4) oWon = true;
			if (x == 4) xWon = true;
		}
		FOR(j,4) {
			int o = 0, x = 0;
			FOR(i,4) {
				if (a[i][j] == 'O') ++o;
				else if (a[i][j] == 'X') ++x;
				else if (a[i][j] == 'T') { ++o; ++x; }
				else if (a[i][j] == '.') { ++empty; }
			}
			if (o == 4) oWon = true;
			if (x == 4) xWon = true;
		}
		int o = 0, x = 0;
		FOR(i,4) {
			if (a[i][i] == 'O') ++o;
			else if (a[i][i] == 'X') ++x;
			else if (a[i][i] == 'T') { ++o; ++x; }
			else if (a[i][i] == '.') { ++empty; }
		}
		if (o == 4) oWon = true;
		if (x == 4) xWon = true;
		o = 0; x = 0;
		FOR(i,4) {
			if (a[i][3-i] == 'O') ++o;
			else if (a[i][3-i] == 'X') ++x;
			else if (a[i][3-i] == 'T') { ++o; ++x; }
			else if (a[i][3-i] == '.') { ++empty; }
		}
		if (o == 4) oWon = true;
		if (x == 4) xWon = true;
		fout << "Case #" << tt << ": ";
		if (oWon) fout << "O won";
		else if (xWon) fout << "X won";
		else if (empty == 0) fout << "Draw";
		else fout << "Game has not completed";
		fout << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
