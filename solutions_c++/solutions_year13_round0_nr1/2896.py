/*
 * main.cc
 *
 *  Created on: 12 Apr 2013
 *      Author: shuss
 *
 *  Compiler:
 *  	Minimalist GNU for Windows (MinGW)
 *  	www.mingw.org
 *  	"MinGW provides a complete Open Source programming tool set ..."
 */

// STL
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
// Data Structures
#include <vector>
#include <set>
#include <map>
#include <stack>
// Math
#include <cmath>
#include <algorithm>
using namespace std;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define DREP(i,n) for (int i((n)-1); i >= 0; --i)

const int inc[2] = { 1, -1 };

char nonT(char a, char b) {
	if ('T' == a) {
		return b;
	}
	return a;
}

int main() {
	int ncases;
	string mystr;
	getline(cin, mystr);
	stringstream(mystr) >> ncases;

	REP (casenum,ncases) {
		bool draw = true;
		///////////////////////////////////////////
		// Input
		char board[4][4];
		REP(i,4) {
			REP(j,4) {
				cin >> board[i][j];
				if ('.' == board[i][j]) {
					draw = false;
				}
			}
		}
		///////////////////////////////////////////
		// i = 0
		char winner = '.';
		int diag1 = 0;
		int diag2 = 0;
		REP(i,4) {
			if (board[i][i] != '.') {
				char c = board[0][0];
				if (c == 'T'){
					c = board[1][1];
				}
				if (c == board[i][i] || board[i][i] == 'T') {
					diag1++;
					if (diag1 == 4) {
						winner = nonT(board[0][0], board[i][i]);
						break;
					}
				}
			}
			if (board[3 - i][i] != '.') {
				char c = board[3][0];
				if (c == 'T') {
					c = board[2][1];
				}
				if (c == board[3 - i][i] || board[3-i][i] == 'T') {
					diag2++;
					if (diag2 == 4) {
						winner = nonT(board[3][0], board[3 - i][i]);
						break;
					}
				}
			}
			int row = 0;
			int column = 0;
			REP(j,4) {
				if (board[i][j] != '.') {
					char c = board[i][0];
					if (c == 'T') {
						c = board[i][1];
					}
					if (c == board[i][j] || board[i][j] == 'T') {
						row++;
					}
				}
				if (board[j][i] != '.') {
					char c = board[0][i];
					if (c == 'T') {
						c = board[1][i];
					}
					if(c == board[j][i] || board[j][i] == 'T')
					column++;
				}
				if (row == 4) {
					winner = nonT(board[i][0], board[i][j]);
					break;
				}
				if (column == 4) {
					winner = nonT(board[0][i], board[j][i]);
					break;
				}
			}
		}

		if (winner == '.') {
			if (draw) {
				cout << "Case #" << casenum + 1 << ": Draw" << endl;
			} else {
				cout << "Case #" << casenum + 1 << ": Game has not completed"
						<< endl;
			}
		}
		else{
			cout << "Case #" << casenum + 1 << ": " << winner << " won" << endl;
		}
	}

	return 0;
}
