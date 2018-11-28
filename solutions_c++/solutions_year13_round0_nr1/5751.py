/*
 * codejam_qual_A.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: leo
 */

#include <iostream>

using namespace std;

int main() {
	int tc;
	char a[4][4];
	cin >> tc;
	bool has_free;
	char win = 0;
	string s;

	for (int t = 1; t <= tc; ++t) {
		for (int i = 0; i < 4; ++i)
			cin >> a[i][0] >> a[i][1] >> a[i][2] >> a[i][3];

		has_free = false;
		char c;
		bool lose;
		//check rows
		for (int i = 0; i < 4; ++i) { // loop on rows
			c = a[i][0] == 'T' ? a[i][1] : a[i][0];
			if (c == '.') {
				has_free = true;
				continue;
			}
			lose = false;
			for (int j = 1; j < 4 && !lose; ++j) {
				if (a[i][j] == '.') {
					has_free = true;
					lose = true;
				} else if (a[i][j] == 'T')
					continue;
				else if (a[i][j] != c)
					lose = true;
			}
			if (lose == false) {
				win = c;
				goto end;
			}

		}

		//check columns
		for (int j = 0; j < 4; ++j) {
			c = a[0][j] == 'T' ? a[1][j] : a[0][j];
			if (c == '.') {
				has_free = true;
				continue;
			}
			lose = false;
			for (int i = 1; i < 4 && !lose; ++i) { // loop in rows
				if (a[i][j] == '.') {
					has_free = true;
					lose = true;
				} else if (a[i][j] == 'T')
					continue;
				else if (a[i][j] != c)
					lose = true;
			}
			if (lose == false) {
				win = c;
				goto end;
			}
		}

		// check diagonals "\"
		c = a[0][0] == 'T' ? a[1][1] : a[0][0];
		lose = false;
		if (c == '.')
			lose = true;
		for (int i = 1; i < 4 && !lose; ++i) { // loop in rows
			if (a[i][i] == 'T')
				continue;
			else if (a[i][i] != c)
				lose = true;
		}
		if (lose == false) {
			win = c;
			goto end;
		}

		// check diagonals "/"
		c = a[0][3] == 'T' ? a[1][2] : a[0][3];
		lose = false;
		if (c == '.')
			lose = true;
		for (int i = 1; i < 4 && !lose; ++i) { // loop in rows
			if (a[i][3 - i] == 'T')
				continue;
			else if (a[i][3 - i] != c)
				lose = true;
		}
		if (lose == false) {
			win = c;
			goto end;
		}

		if (has_free)
			s = "Game has not completed";
		else
			s = "Draw";
		cout << "Case #" << t << ": " << s << endl;
		goto cont;
		end: cout << "Case #" << t << ": " << win << " won" << endl;
		cont: ;
	}
	return 0;
}

