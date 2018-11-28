//============================================================================
// Name        : CodeJam.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>

using namespace std;

int main() {
	int cunt,i,j,k, c_win;
	bool draw=false;
	char in;
	cin >> cunt;
	int field[4][4];
	for (k=1; k<=cunt; ++k){
		c_win = 1;
		for (i=0; i<4; ++i){
			for (j=0; j<4; j++){
				cin >> in;
				switch (in){
				case '.':
					field[j][i] = 0;
					c_win=0;
					break;
				case 'T':
					field[j][i] = 1;
					break;
				case 'O':
					field[j][i] = 2;
					break;
				case 'X':
					field[j][i] = 3;
					break;
				}

			}
		}

		if (((field[0][0] == 3 || field [0][0] == 1)&&(field[1][1] == 3 || field [1][1] == 1)&&(field[2][2] == 3 || field [2][2] == 1)&&(field[3][3] == 3 || field [3][3] == 1)) ||
			((field[0][3] == 3 || field [0][3] == 1)&&(field[1][2] == 3 || field [1][2] == 1)&&(field[2][1] == 3 || field [2][1] == 1)&&(field[3][0] == 3 || field [3][0] == 1)) ||
			((field[0][0] == 3 || field [0][0] == 1)&&(field[0][1] == 3 || field [0][1] == 1)&&(field[0][2] == 3 || field [0][2] == 1)&&(field[0][3] == 3 || field [0][3] == 1)) ||
			((field[1][0] == 3 || field [1][0] == 1)&&(field[1][1] == 3 || field [1][1] == 1)&&(field[1][2] == 3 || field [1][2] == 1)&&(field[1][3] == 3 || field [1][3] == 1)) ||
			((field[2][0] == 3 || field [2][0] == 1)&&(field[2][1] == 3 || field [2][1] == 1)&&(field[2][2] == 3 || field [2][2] == 1)&&(field[2][3] == 3 || field [2][3] == 1)) ||
			((field[3][0] == 3 || field [3][0] == 1)&&(field[3][1] == 3 || field [3][1] == 1)&&(field[3][2] == 3 || field [3][2] == 1)&&(field[3][3] == 3 || field [3][3] == 1)) ||
			((field[0][0] == 3 || field [0][0] == 1)&&(field[1][0] == 3 || field [1][0] == 1)&&(field[2][0] == 3 || field [2][0] == 1)&&(field[3][0] == 3 || field [3][0] == 1)) ||
			((field[0][1] == 3 || field [0][1] == 1)&&(field[1][1] == 3 || field [1][1] == 1)&&(field[2][1] == 3 || field [2][1] == 1)&&(field[3][1] == 3 || field [3][1] == 1)) ||
			((field[0][2] == 3 || field [0][2] == 1)&&(field[1][2] == 3 || field [1][2] == 1)&&(field[2][2] == 3 || field [2][2] == 1)&&(field[3][2] == 3 || field [3][2] == 1)) ||
			((field[0][3] == 3 || field [0][3] == 1)&&(field[1][3] == 3 || field [1][3] == 1)&&(field[2][3] == 3 || field [2][3] == 1)&&(field[3][3] == 3 || field [3][3] == 1))){
			c_win=3;
		}
		if (((field[0][0] == 2 || field [0][0] == 1)&&(field[1][1] == 2 || field [1][1] == 1)&&(field[2][2] == 2 || field [2][2] == 1)&&(field[3][3] == 2 || field [3][3] == 1)) ||
			((field[0][3] == 2 || field [0][3] == 1)&&(field[1][2] == 2 || field [1][2] == 1)&&(field[2][1] == 2 || field [2][1] == 1)&&(field[3][0] == 2 || field [3][0] == 1)) ||
			((field[0][0] == 2 || field [0][0] == 1)&&(field[0][1] == 2 || field [0][1] == 1)&&(field[0][2] == 2 || field [0][2] == 1)&&(field[0][3] == 2 || field [0][3] == 1)) ||
			((field[1][0] == 2 || field [1][0] == 1)&&(field[1][1] == 2 || field [1][1] == 1)&&(field[1][2] == 2 || field [1][2] == 1)&&(field[1][3] == 2 || field [1][3] == 1)) ||
			((field[2][0] == 2 || field [2][0] == 1)&&(field[2][1] == 2 || field [2][1] == 1)&&(field[2][2] == 2 || field [2][2] == 1)&&(field[2][3] == 2 || field [2][3] == 1)) ||
			((field[3][0] == 2 || field [3][0] == 1)&&(field[3][1] == 2 || field [3][1] == 1)&&(field[3][2] == 2 || field [3][2] == 1)&&(field[3][3] == 2 || field [3][3] == 1)) ||
			((field[0][0] == 2 || field [0][0] == 1)&&(field[1][0] == 2 || field [1][0] == 1)&&(field[2][0] == 2 || field [2][0] == 1)&&(field[3][0] == 2 || field [3][0] == 1)) ||
			((field[0][1] == 2 || field [0][1] == 1)&&(field[1][1] == 2 || field [1][1] == 1)&&(field[2][1] == 2 || field [2][1] == 1)&&(field[3][1] == 2 || field [3][1] == 1)) ||
			((field[0][2] == 2 || field [0][2] == 1)&&(field[1][2] == 2 || field [1][2] == 1)&&(field[2][2] == 2 || field [2][2] == 1)&&(field[3][2] == 2 || field [3][2] == 1)) ||
			((field[0][3] == 2 || field [0][3] == 1)&&(field[1][3] == 2 || field [1][3] == 1)&&(field[2][3] == 2 || field [2][3] == 1)&&(field[3][3] == 2 || field [3][3] == 1))){
			c_win=2;
		}
		switch (c_win){
			case 1:
				cout << "Case #" << k << ": Draw" << endl;
				break;
			case 0:
				cout << "Case #" << k << ": Game has not completed" << endl;
				break;
			case 2:
				cout << "Case #" << k << ": O won" << endl;
				break;
			case 3:
				cout << "Case #" << k << ": X won" << endl;
				break;

		}
	}
	return 0;
}
