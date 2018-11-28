#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

int chk_win (char a[][5])
{


	int i, j;
	
	if (a[0][0] == a[1][1] && a[1][1] == a[2][2] && a[2][2] == a[3][3] && (a[0][0] == 'X' || a[0][0] == 'O')) {
		if (a[0][0] == 'X') {
			return 1;
		} else {
			return 2;
		}
	} else if (a[0][3] == a[1][2] && a[1][2] == a[2][1] && a[2][1] == a[3][0] && (a[0][3] == 'X' || a[0][3] == 'O')) {
		if (a[0][3] == 'X') {
			return 1;
		} else {
			return 2;
		}
	} else {
		
		for (i = 0; i < 4; i++) {
			if (a[i][0] == a[i][1] && a[i][1] == a[i][2] && a[i][2] == a[i][3] && (a[i][0] == 'X' || a[i][0] == 'O')) {
				if (a[i][0] == 'X') {
					return 1;
				} else {
					return 2;
				}
			}
		}
		for (i = 0; i < 4; i++) {
			if (a[0][i] == a[1][i] && a[1][i] == a[2][i] && a[2][i] == a[3][i] && (a[0][i] == 'X' || a[0][i] == 'O')) {
				if (a[0][i] == 'X') {
					return 1;
				} else {
					return 2;
				}
			}
		}
	}
	return 0;
}
	
int main ()
{

	
	int t, i, j;
	cin >> t;
	int cas = 0;
	while (t--) {
		char a[5][5];
		int dot = 0, tx = 0, ty = 0, t = 0;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				cin >> a[i][j];
			
				if (a[i][j] == '.') {
					dot = 1;
				}
				if (a[i][j] == 'T') {
					t = 1;
					tx = i;
					ty = j;
				}
			}
		}
		int c;
		if (t == 1) {
			a[tx][ty] = 'X';
			c = chk_win (a);
		} else {
			c = chk_win (a);
		}
		if (t == 1 && c == 0) {
			a[tx][ty] = 'O';
			c = chk_win (a);
		} else {
			c = chk_win (a);
		}

		cout << "Case #" << ++cas << ": ";
		if (c == 0 && dot == 1) {
			cout << "Game has not completed\n";
		} else if (c == 0 && dot == 0) {
			cout << "Draw\n";
		} else if (c == 1) {
			cout << "X won\n";
		} else {
			cout << "O won\n";
		}
	}
	return 0;
}
