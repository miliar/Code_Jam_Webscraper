#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

#define max(a, b) (((a) > (b)) ? (a) : (b))
#define min(a, b) (((a) > (b)) ? (b) : (a))
#define abs(a) (((a) > 0) ? (a) : (-(a)))

using namespace std;

string s[4];

string get() {
	bool all = true;
	for (int i = 0; i < 4; i++) {
		int nO=0, nX=0, nT=0, nP=0;
		for (int j = 0; j < 4; j++) {
			if (s[i][j] == 'O') nO++;
			if (s[i][j] == '.') nP++;
			if (s[i][j] == 'X') nX++;
			if (s[i][j] == 'T') nT++;
		}
		if (nO == 4 || (nO == 3 && nT == 1)) return "O won";
		if (nX == 4 || (nX == 3 && nT == 1)) return "X won";
		if (nP != 0) all = false;
	}
	for (int j = 0; j < 4; j++) {
		int nO=0, nX=0, nT=0, nP=0;
		for (int i = 0; i < 4; i++) {
			if (s[i][j] == 'O') nO++;
			if (s[i][j] == '.') nP++;
			if (s[i][j] == 'X') nX++;
			if (s[i][j] == 'T') nT++;
		}
		if (nO == 4 || (nO == 3 && nT == 1)) return "O won";
		if (nX == 4 || (nX == 3 && nT == 1)) return "X won";
		if (nP != 0) all = false;
	}
	int nO=0, nX=0, nT=0, nP=0;
	for (int i = 0; i < 4; i++) {
		if (s[i][i] == 'O') nO++;
		if (s[i][i] == '.') nP++;
		if (s[i][i] == 'X') nX++;
		if (s[i][i] == 'T') nT++;
		if (nO == 4 || (nO == 3 && nT == 1)) return "O won";
		if (nX == 4 || (nX == 3 && nT == 1)) return "X won";
		if (nP != 0) all = false;
	}
	nO=0, nX=0, nT=0, nP=0;
	for (int i = 0; i < 4; i++) {
		if (s[i][3-i] == 'O') nO++;
		if (s[i][3-i] == '.') nP++;
		if (s[i][3-i] == 'X') nX++;
		if (s[i][3-i] == 'T') nT++;
		if (nO == 4 || (nO == 3 && nT == 1)) return "O won";
		if (nX == 4 || (nX == 3 && nT == 1)) return "X won";
		if (nP != 0) all = false;
	}
	if (all) return "Draw";
	return "Game has not completed";
}

int main () {
	int tests;
	scanf ("%d", &tests);
	for (int t = 0; t < tests; t++) {
		for (int i = 0; i < 4; i++)
			cin >> s[i];
		cout << "Case #" << t+1 << ": " << get() << endl;
	}
}

