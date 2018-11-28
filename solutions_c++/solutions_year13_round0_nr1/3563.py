#include <iostream>
#include <fstream>

using namespace std;

enum Results {
	X = 1,
	O = 2,
	GOING = 3,
	DRAW = 4
};

bool allFilled(int a[4][4]) {
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			if (a[i][j] == 3)
				return false;

	return true;
}

int solve(int a[4][4]) {
	for (int i=0; i< 4; i++) {
		int check = a[i][0] |  a[i][1] | a[i][2] | a[i][3];	
		if (check == 1 || check == 2)
			return check;
	}

	for (int j=0; j< 4; j++) {
		int check = a[0][j] |  a[1][j] | a[2][j] | a[3][j];	
		if (check == 1 || check == 2)
			return check;
	}

	int check = a[0][0] | a[1][1] | a[2][2] | a[3][3];
	if (check == 1 || check == 2)
		return check;

	check = a[0][3] | a[1][2] | a[2][1] | a[3][0];
	if (check == 1 || check == 2)
		return check;

    if (allFilled(a)){
		return DRAW;
	} else {
		return GOING;
	}

}


void printBoard(int board[4][4]) {
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			cout << board[i][j];
		}
		cout << endl;
	}
}

int charToInt(char ch) {
	if (ch == 'T') {
		return 0;
	} else if (ch == 'X') {
		return X;
	} else if (ch == 'O') {
		return O;
	} else {
		return 3;
	}
}

int main()
{
	int n;
	fstream fin("input.txt", fstream::in);
	fin >> n;

	for (int caseNo=1; caseNo <= n; ++caseNo) {
		int board [4][4];
		char ch;
		for (int i=0; i<4; i++) {
			for (int j=0; j<4; j++) {
				fin >> ch;
				board[i][j] = charToInt(ch);	
			}
		}

		// printBoard(board);

		int res = solve(board);
		cout << "Case #" << caseNo << ": ";
		switch (res) {
			case X:
				cout << "X won" << endl;
				break;
			case O:
				cout << "O won" << endl;
				break;
			case GOING:
				cout << "Game has not completed" << endl;
				break;
			case DRAW:
				cout << "Draw" << endl;
				break;
		}

	}

	return 0;
}
