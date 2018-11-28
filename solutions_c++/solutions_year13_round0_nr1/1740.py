#include <iostream>
using namespace std;

int T;
int row_sums[4];
int col_sums[4];
int diag_sums[2];

int main()
{
	cin >> T;
	for (int i = 0; i < T; i++) {
		char tmp;
		int value;
		bool free_squares, winner;
		
		// Init
		free_squares = false;
		winner = false;
		diag_sums[0] = 0;
		diag_sums[1] = 0;
		for (int j = 0; j < 4; j++) {
			row_sums[j] = 0;
			col_sums[j] = 0;
		}
		
		// Input and calculations
		for (int row = 0; row < 4; row++) {
			for (int col = 0; col < 4; col++) {
				cin >> tmp;
				if (tmp == 'O') value = 1;
				else if (tmp == 'X') value = -1;
				else if (tmp == '.') value = 0;
				else if (tmp == 'T') value = 100;
				
				if (value == 0) free_squares = true;
				row_sums[row] += value;
				col_sums[col] += value;
				if (row == col) diag_sums[0] += value;
				else if (row == (3-col)) diag_sums[1] += value;				
			}
		}
		
		// Check
		if (diag_sums[0] == 4 || diag_sums[0] == 103 ||
			diag_sums[1] == 4 || diag_sums[1] == 103) {
				cout << "Case #" << i+1 << ": O won" << endl;
				continue;
		}
		else if (diag_sums[0] == -4 || diag_sums[0] == 97 ||
			diag_sums[1] == -4 || diag_sums[1] == 97) {
				cout << "Case #" << i+1 << ": X won" << endl;
				continue;
		}
		for (int j = 0; j < 4; j++) {
			if (row_sums[j] == 4 || row_sums[j] == 103 ||
				col_sums[j] == 4 || col_sums[j] == 103) {
					cout << "Case #" << i+1 << ": O won" << endl;
					winner = true;
					break;
			}
			else if (row_sums[j] == -4 || row_sums[j] == 97 ||
				col_sums[j] == -4 || col_sums[j] == 97) {
					cout << "Case #" << i+1 << ": X won" << endl;
					winner = true;
					break;
			}
		}
		if (!winner) {
			if (free_squares) {
				cout << "Case #" << i+1 << ": Game has not completed" << endl;
			}
			else {
				cout << "Case #" << i+1 << ": Draw" << endl;
			}
		}
	}
	return 0;
}
