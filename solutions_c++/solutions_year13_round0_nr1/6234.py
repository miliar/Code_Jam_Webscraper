#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

char game[4][4];

/* x= zeile; y = spalte*/
bool fourInRow(char c, int xStart, int yStart, int xDir, int yDir) {
	int i = 0;
	int x=xStart;
	int y=yStart;
	while (i < 4) {
		if (!(0 <= x && x < 4) || !(0<= y && y < 4)) {
			break;
		}

		if (!(game[x][y] == c || game[x][y] == 'T')) {
			return false;
		}

		i++;
		x += xDir;
		y += yDir;
	}

	return i == 4;
}

bool checkWinAllDir(char c, int xStart, int yStart) {
	return fourInRow(c, xStart, yStart, 0, 1)
		|| fourInRow(c, xStart, yStart, 0, -1)
		|| fourInRow(c, xStart, yStart, 1, -1)
		|| fourInRow(c, xStart, yStart, 1, 0)
		|| fourInRow(c, xStart, yStart, 1, 1)
		|| fourInRow(c, xStart, yStart, -1, 1)
		|| fourInRow(c, xStart, yStart, -1, 0)
		|| fourInRow(c, xStart, yStart, -1, -1);
}

bool isDraw() {
	for (int x=0; x < 4; x++) {
		for (int y=0; y < 4; y++) {
			if (game[x][y] == '.') {
				return false;
			}
		}
	}
	return true;
}

void printBoard() {
	for(int zeile=0; zeile < 4; zeile++) {
		for(int spalte=0; spalte < 4; spalte++){
			cout << game[zeile][spalte];
		}
		cout << endl;
	}
}

string getGameStatus() {
	bool xWon = false;
	bool oWon = false;
	bool draw = false;
	//cout << "getGameStatus";
	// check who won
	if (isDraw()) {
		draw = true;
	} 

	for (int zeile=0; zeile < 4; zeile++) {
		for (int spalte=0;spalte<4;spalte++) {
			//cout << "check " << zeile << "|" << spalte << endl;
			xWon = xWon || checkWinAllDir('X', zeile, spalte);
			oWon = oWon || checkWinAllDir('O', zeile, spalte);
		}
	}

	// return status
	if (xWon) {
		return "X won";
	} else if (oWon) {
		return "O won";
	} else if (draw) {
		return "Draw";
	} else {
		return "Game has not completed";
	}
}

int main(void)
{
	unsigned short int t;
	char ignore;
	cin >> t; //number of test cases

	for(int i=1; i <= t; i++){ //loops for each case
		for (int zeile=0;zeile<4;zeile++) {
			for (int spalte=0;spalte<4;spalte++) {
				cin >> game[zeile][spalte];
				//cout << zeile << "|" << spalte << endl;
			}
		}
		//printBoard();
		cout << "Case #" << i << ": " << getGameStatus() << endl;
	}

	return 0;
}
