#include <iostream>

using namespace std;

int main() {

	int T;
	cin >> T;
	char field[5][5];
	
	for (int t=0; t<T; t++) {
		int dot = 0;
		for (int i=0;i<4;i++) {
			cin >> field[i];
			for (int j=0;j<4;j++) {
				if (field[i][j] == '.') dot++;
			}
		}

		int nx = 0,no = 0;
		for (int i=0;i<4;i++) {
			nx = 0; no = 0;
			for (int j=0;j<4;j++) {
				if (field[i][j] == 'X' || field[i][j] == 'T') nx++;
				if (field[i][j] == 'O' || field[i][j] == 'T') no++;
			}
			if (nx == 4 || no == 4) break;
			nx = 0; no = 0;
			for (int j=0;j<4;j++) {
				if (field[j][i] == 'X' || field[j][i] == 'T') nx++;
				if (field[j][i] == 'O' || field[j][i] == 'T') no++;
			}
			if (nx == 4 || no == 4) break;
		}
		if (nx < 4 && no < 4) {
			nx = 0; no = 0;
			for (int i=0;i<4;i++) {
				if (field[i][i] == 'X' || field[i][i] == 'T') nx++;
				if (field[i][i] == 'O' || field[i][i] == 'T') no++;
			}
		}
		if (nx < 4 && no < 4) {
			nx = 0; no = 0;
			for (int i=0;i<4;i++) {
				if (field[i][3-i] == 'X' || field[i][3-i] == 'T') nx++;
				if (field[i][3-i] == 'O' || field[i][3-i] == 'T') no++;
			}
		}
		
		cout << "Case #" << (t+1) << ": ";
		if (nx == 4) {
			cout << "X won" << endl;
		} else if (no == 4) {
			cout << "O won" << endl;
		} else if (dot == 0) {
			cout << "Draw" << endl;
		} else {
			cout << "Game has not completed" << endl;
		}
	
	}

	return 0;
}


