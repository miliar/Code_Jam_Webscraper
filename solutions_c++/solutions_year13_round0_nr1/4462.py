//============================================================================
// Name        : Test.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int winCase[10][4] = {
		{0, 1, 2, 3},
		{4, 5, 6, 7},
		{8, 9, 10, 11},
		{12, 13, 14, 15},
		{0, 4, 8, 12},
		{1, 5, 9, 13},
		{2, 6, 10, 14},
		{3, 7, 11, 15},
		{0, 5, 10, 15},
		{3, 6, 9, 12}
};

void func_for_2270488(int nCases) {
	string srcStr;
	string retStr;

	for(int i = 0; i < nCases; i++) {
		char x[17];
		char o[17];

		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr); retStr.append(srcStr);
		getline(cin, srcStr);

		for(int j = 0; j < 16;j++) {
			if(retStr[j] == 'T') {
				x[j] = 'X';
				o[j] = 'O';
			} else {
				x[j] = o[j] = retStr[j];
			}
		}
		x[16] = 0;
		o[16] = 0;

		// 1: X won
		// 2: O won
		// 3: Draw
		// 4: Game has not completed
		int result = 0;
		int ax = 0;
		int ao = 0;
		int isFull = 1;
		for(int k = 0; k < 10; k++) {
			ax = ao = 0;
			for(int l = 0; l < 16; l++) {
				if(x[l] == '.') {
					isFull = 0;
					break;
				}
			}

			for(int l = 0; l < 4; l++) {
				if(x[winCase[k][l]] == 'X') {
					ax++;
				}

				if(o[winCase[k][l]] == 'O') {
					ao++;
				}
			}

			if(ax == 4) {
				result = 1;
				break;
			} else if(ao == 4) {
				result = 2;
				break;
			}
		}

		if(result == 0) {
			if(isFull == 1) {
				result = 3;
			} else {
				result = 4;
			}
		}
		// check x win

		cout << "Case #" << (i+1);
		switch(result) {
		case 1:
			cout << ": X won" << endl;
			break;
		case 2:
			cout << ": O won" << endl;
			break;
		case 3:
			cout << ": Draw" << endl;
			break;
		case 4:
			cout << ": Game has not completed" << endl;
			break;
		case 0:
		default:
			break;
		}
		//cout << "Case #" << (i+1) << ": " << x << endl;
		//cout << "Case #" << (i+1) << ": " << o << endl;
		retStr.clear();
	}
}
int main(int argc, char* argv[]) {
	int nCases = 0;
	string srcStr;

	//freopen("D:/A-small-practice.in","rt",stdin);
    //

	freopen("D:/GCJ2013/20130413/A-large.in", "rt", stdin);
	freopen("D:/GCJ2013/20130413/A-large.out", "wt", stdout);

	getline(cin, srcStr);
	nCases = atoi(srcStr.c_str());

	func_for_2270488(nCases);


	return 0;
}
