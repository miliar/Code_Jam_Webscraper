#include <cstdio>
#include <math.h>
#include <iostream>
#include <vector>

using namespace std;

const int n = 4;
static char grid[n][n];

enum Outcome {
	XWin,
	OWin,
	Neither
};

inline bool isX(char c) { return (c == 'X') || (c == 'T'); }
inline bool isO(char c) { return (c == 'O') || (c == 'T'); }
inline bool isT(char c) { return (c == 'T'); }
inline bool isDot(char c) {return (c == '.'); }

Outcome CheckRows() {
	for (int i = 0; i < n; i++) {
		char* startOfRow = grid[i];
		if (isX(*startOfRow) && isX(*(startOfRow+1)) && isX(*(startOfRow+2)) && isX(*(startOfRow+3)))
			return XWin;
		else if (isO(*startOfRow) && isO(*(startOfRow+1)) && isO(*(startOfRow+2)) && isO(*(startOfRow+3)))
			return OWin;
	}
	return Neither;
} 

Outcome CheckColumns() {
	for (int i = 0; i < n; i++)	{
		char* startOfCol = &(grid[0][i]);
		if (isX(*startOfCol) && isX(*(startOfCol+(1*n))) && isX(*(startOfCol+(2*n))) && isX(*(startOfCol+(3*n))))
			return XWin;
		else if (isO(*startOfCol) && isO(*(startOfCol+(1*n))) && isO(*(startOfCol+(2*n))) && isO(*(startOfCol+(3*n))))
			return OWin;
	}
	return Neither;
}

Outcome CheckDiagonals() {
	if (isX(grid[0][0]) && isX(grid[1][1]) && isX(grid[2][2]) && isX(grid[3][3]))
		return XWin;
	else if (isO(grid[0][0]) && isO(grid[1][1]) && isO(grid[2][2]) && isO(grid[3][3]))
		return OWin;
	else if (isX(grid[0][3]) && isX(grid[1][2]) && isX(grid[2][1]) && isX(grid[3][0]))
		return XWin;
	else if (isO(grid[0][3]) && isO(grid[1][2]) && isO(grid[2][1]) && isO(grid[3][0]))
		return OWin;
	return Neither;
}

int main(int argc, char *argv[]) {

	int c, cases;
	cin >> cases;

	for(c = 1; c <= cases; c++)	{
		char gridValue;
		bool haveEmpty = false;
		Outcome outcome;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> gridValue;
				grid[i][j] = gridValue;
				if (isDot(gridValue))
					haveEmpty = true;
			}
		}

		outcome = CheckRows();
		if (outcome == Neither)
			outcome = CheckColumns();
		if (outcome == Neither)
			outcome = CheckDiagonals();

		cout << "Case #" << c << ": ";
		switch (outcome) {
			case XWin:
				cout << "X won" << '\n';
				break;
			case OWin:
				cout << "O won" << '\n';
				break;
			default:
				if (haveEmpty)
					cout << "Game has not completed" << '\n';
				else
					cout << "Draw" << '\n';
				break;
		}
	}
}

