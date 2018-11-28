#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <string>
#include <time.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define Vi vector<int>
#define Vd vector<double>
#define Vs vector<string>

char sz[4][5];

bool four(char ch) {
	for (int r=0; r<4; r++) {
		bool found = true;
		for (int c=0; c<4; c++)
			if (sz[r][c]!=ch && sz[r][c]!='T') { found=false; break; }
		if (found)	return true;
	}
	for (int r=0; r<4; r++) {
		bool found = true;
		for (int c=0; c<4; c++)
			if (sz[c][r]!=ch && sz[c][r]!='T') { found=false; break; }
		if (found)	return true;
	}
	{
		bool found = true;
		for (int c=0; c<4; c++)
			if (sz[c][c]!=ch && sz[c][c]!='T') { found=false; break; }
		if (found)	return true;
	}
	{
		bool found = true;
		for (int c=0; c<4; c++)
			if (sz[c][3-c]!=ch && sz[c][3-c]!='T') { found=false; break; }
		if (found)	return true;
	}
	return false;
}

bool has_dots() {
	int count = 0;
	for (int r=0; r<4; r++)
		for (int c=0; c<4; c++)
			if (sz[r][c]=='.') return true;
	return false;
}

int main() {
	int T;
	cin >> T;

	for (int i=1; i<=T; i++) {
		for (int j=0; j<4; j++)
			cin >> sz[j];
		cin.ignore(100,'\n');

		///for (int j=0; j<4; j++) cout << sz[j] << " "<< endl;

		cout << "Case #" << i << ": ";
		if (four('X')) cout << "X won" << endl;
		else
		if (four('O')) cout << "O won" << endl;
		else
		if (!has_dots()) cout << "Draw" << endl;
		else
		cout << "Game has not completed" << endl;
	}
	return 0;
}
