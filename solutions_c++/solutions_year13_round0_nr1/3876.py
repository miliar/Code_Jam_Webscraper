/*
 * A1.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Darin
 */

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int main() {

	freopen("t.in", "r", stdin);
	freopen("t.out","w",stdout);
	string s[5];
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		bool complete = true;
		for (int i = 0; i <= 3; i++) {
			cin >> s[i];
			for (int j = 0; j <= 3; j++) {
				if (s[i][j] == '.') complete = false;
			}
		}
		string ss;
		getline(cin,ss);
		bool xwon,owon;
		xwon = false;
		owon = false;
		int countx = 0;
		int counto = 0;
		int countt = 0;
		for (int i = 0; i <= 3; i++) {
			countx = 0;
			counto = 0;
			countt = 0;
			for (int j = 0; j <= 3; j++) {
				if (s[i][j] == 'O') counto++; else
				if (s[i][j] == 'X') countx++; else
				if (s[i][j] == 'T') countt++; else break;
			}
			if (countx == 4 || (countx == 3 && countt == 1)) xwon = true;
			if (counto == 4 || (counto == 3 && countt == 1)) owon = true;
		}
		for (int i = 0; i <= 3; i++) {
			countx = 0;
			counto = 0;
			countt = 0;
			for (int j = 0; j <= 3; j++) {
				if (s[j][i] == 'O') counto++; else
				if (s[j][i] == 'X') countx++; else
				if (s[j][i] == 'T') countt++; else break;
			}
			if (countx == 4 || (countx == 3 && countt == 1)) xwon = true;
			if (counto == 4 || (counto == 3 && countt == 1)) owon = true;
		}
		countx = 0;
		counto = 0;
		countt = 0;
		for (int i = 0; i <= 3; i++){
			if (s[i][i] == 'O') counto++; else
			if (s[i][i] == 'X') countx++; else
			if (s[i][i] == 'T') countt++; else break;
		}
		if (countx == 4 || (countx == 3 && countt == 1)) xwon = true;
		if (counto == 4 || (counto == 3 && countt == 1)) owon = true;

		countx = 0;
		counto = 0;
		countt = 0;
		for (int i = 0; i <= 3; i++){
			if (s[i][3-i] == 'O') counto++; else
			if (s[i][3-i] == 'X') countx++; else
			if (s[i][3-i] == 'T') countt++; else break;
		}
		if (countx == 4 || (countx == 3 && countt == 1)) xwon = true;
		if (counto == 4 || (counto == 3 && countt == 1)) owon = true;


		cout << "Case #" << test << ": ";
		if (xwon) cout << "X won" << endl; else
		if (owon) cout << "O won" << endl; else
		if (!complete) cout << "Game has not completed" << endl; else
			cout << "Draw" << endl;
	}
	return 0;
}
