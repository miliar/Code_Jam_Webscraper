//============================================================================
// Name        : codejam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
#define MIN(a, b) ((a > b) ? b : a)
#define MAX(a, b) ((a > b) ? a : b)

int main() {
	ifstream fi;
	ofstream fo;
	fi.open("in.in");
	fo.open("out.txt");

	int t;
	fi >> t;
	for (int c = 1; c <= t; c++) {
		int n = 4;
		vector<vector<char> > b(n);
		cout << "a" << endl;
		for (int i = 0; i < n; i++) {
			b[i] = vector<char>(n);
			for (int j = 0; j < n; j++) {
				fi >> b[i][j];
				//cout << b[i][j] << endl;
			}
		}
		for (int i = 0; i < n; i++) {
			//b[i] = vector<char>(n);
			for (int j = 0; j < n; j++) {
				//fi >> b[i][j];
				cout << b[i][j] ;
			}
			cout << endl;
		}

		//Check X won
		bool xwon = false;
		for (int i = 0; i < n; i++) {
			//check each row
			bool rwon = true;
			bool cwon = true;
			for (int j = 0; j < n; j++) {
				if (b[i][j] == 'O' || b[i][j] == '.') {
					rwon = false;
				}
				if (b[j][i] == 'O' || b[j][i] == '.') {
					cwon = false;
				}

			}
			if (rwon || cwon) xwon = true;
		}

		bool lwon = true;
		bool rwon = true;
		for (int i = 0; i < n; i++) {

			if (b[i][i] == 'O' || b[i][i] == '.') {
				lwon = false;
			}
			if (b[i][n - i -1] == 'O' || b[i][n - i -1] == '.') {
				rwon = false;
			}
		}
		if (rwon || lwon) xwon = true;

		bool owon = false;
		for (int i = 0; i < n; i++) {
			//check each row
			bool rwon = true;
			bool cwon = true;
			for (int j = 0; j < n; j++) {
				if (b[i][j] == 'X' || b[i][j] == '.') {
					rwon = false;
				}
				if (b[j][i] == 'X' || b[j][i] == '.') {
					cwon = false;
				}

			}
			if (rwon || cwon) owon = true;
		}

		lwon = true;
		rwon = true;
		for (int i = 0; i < n; i++) {

			if (b[i][i] == 'X' || b[i][i] == '.') {
				lwon = false;
			}
			if (b[i][n - i -1] == 'X' || b[i][n - i -1] == '.') {
				rwon = false;
			}
		}
		if (rwon || lwon) owon = true;

		if (xwon) fo << "Case #" << c << ": X won\n";
		if (owon) fo << "Case #" << c << ": O won\n";
		if (!xwon && !owon) {
			bool draw = true;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (b[i][j] == '.') {
						draw = false;
					}
				}
			}
			if (draw) fo << "Case #" << c << ": Draw\n";
			else fo << "Case #" << c << ": Game has not completed\n";
		}
	}

	fo.close();
	fi.close();
	return 0;
}
