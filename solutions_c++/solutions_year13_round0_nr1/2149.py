#include <iostream>
using namespace std;

int main()
{
	int t, u = 1;
	cin >> t;
	while (t--) {
		int cntx, cnto, i, j, dot = 0;
		char a[10][10];
		for (i = 0; i < 4; i++) {
			cin >> a[i];
			for (j = 0; j < 4; j++) {
				if (a[i][j] == '.') {
					dot++;
				}
			}
		}
		int d2x = 0;
		int d1x = 0;
		int d1o = 0;
		int d2o = 0;
		//checking for x won or 'o'
		for (i = 0; i < 4; i++) {
			if (a[i][i] == 'X' || a[i][i] == 'T') {
				d1x++;
			}
			if (a[i][i] == 'O' || a[i][i] == 'T') {
				d1o++;
			}
			if (a[i][3 - i] == 'X' || a[i][3 - i] == 'T') {
				d2x++;
			}
			if (a[i][3 - i] == 'O' || a[i][3 - i] == 'T') {
				d2o++;
			}
		}
		for (i = 0; i < 4; i++) {
			cnto = 0, cntx = 0;
			for (j = 0; j < 4; j++) {
				if (a[i][j] == 'T') {
					cntx++;
					cnto++;
				} else if (a[i][j] == 'X') {
					cntx++;
				} else if (a[i][j] == 'O') {
					cnto++;
				}
			}
			if (cntx == 4 || cnto == 4) {
				break;
			}
			cnto = 0, cntx = 0;
			for (j = 0; j < 4; j++) {
				if (a[j][i] == 'T') {
					cntx++;
					cnto++;
				} else if (a[j][i] == 'X') {
					cntx++;
				} else if (a[j][i] == 'O') {
					cnto++;
				}
			}
			if (cntx == 4 || cnto == 4) {
				break;
			}
		}
		cout << "Case #" << u++ << ": ";
		if (cntx == 4 || d1x == 4 || d2x == 4) {
			cout << "X won" << endl;
		} else if (cnto == 4 || d2o == 4 || d1o == 4) {
			cout << "O won" << endl;
		} else if (dot > 0) {
			cout << "Game has not completed" << endl;
		} else {
			cout << "Draw" << endl;
		}
	}
	return 0;
}
