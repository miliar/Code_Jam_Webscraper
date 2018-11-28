//============================================================================
// Name        : GCJA.cpp
// Author      : Hossam El-Deen, Waleed, Bassem
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int arr[256];
string s[4];

int main() {
	freopen("A-large.in", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
	freopen("A-large.out", "wt", stdout); // same for out.txt
	int T, ctrX, ctrO, ctrT;
	bool d, end;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		string S[10];
		d = 0;
		end = 1;
		for (int i = 0; i < 4; ++i) {
			cin >> s[i];
			S[i] = s[i];
			for (int j = 0; j < 4; ++j) {
				S[4 + j] += s[i][j];
				if (s[i][j] == '.')
					end = 0;
			}
			S[8] += s[i][i];
			S[9] += s[i][3 - i];
		}
		//End of tazbeet
		for (int i = 0; i < 10; ++i) {
			ctrX = count(S[i].begin(), S[i].end(), 'X');
			ctrO = count(S[i].begin(), S[i].end(), 'O');
			ctrT = count(S[i].begin(), S[i].end(), 'T');
			if (ctrX == 4 || (ctrX == 3 && ctrT == 1)) {
				cout << "X won" << endl;
				d = 1;
				break;
			}
			if (ctrO == 4 || (ctrO == 3 && ctrT == 1)) {
				cout << "O won" << endl;
				d = 1;
				break;
			}
		}
		if (d)
			continue;
		if (end)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}
	return 0;
}

