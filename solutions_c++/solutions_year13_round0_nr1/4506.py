#include<iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int cas = 1;
	while (n--) {
		string s[4];
		for (int i = 0; i < 4; i++) cin >> s[i];
		char state = 0;
		char cx[4], co[4], dx[2], dio[2], dots;
		dots = 0;
		for (int i = 0; i < 4; i++) cx[i] = co[i] = 0;
		for (int i = 0; i < 2; i++) dx[i] = dio[i] = 0;
		for (int i = 0; i < 4; i++) {
			int ro = 0;
			int rx = 0;
			int rt = 0;
			for (int j = 0; j < 4; j++) {
				if (s[i][j] == 'O') {
					ro++;
					co[j]++;
					if (i == j) dio[0]++;
					else if (i == 3-j) dio[1]++;
				}
				else if (s[i][j] == 'X') {
					rx++;
					cx[j]++;
					if (i == j) dx[0]++;
					else if (i == 3-j) dx[1]++;
				}
				else if (s[i][j] == 'T') {
					rt++;
					co[j]++;
					cx[j]++;
					if (i == j) {
						dio[0]++;
						dx[0]++;
					}
					else if (i == 3-j) {
						dio[1]++;
						dx[1]++;
					}
				}
				else if (s[i][j] == '.') ++dots;
			}
			if (rx == 4 || rx == 3 && rt == 1) {
				state = 'X';
				break;
			}
			else if (ro == 4 || ro == 3 && rt == 1) {
				state = 'O';
				break;
			}
		}
		if (dx[0] == 4 || dx[1] == 4) state = 'X';
		else if (dio[0] == 4 || dio[1] == 4) state = 'O';
		if (state == 0) {
			for (int i = 0; i < 4; i++) {
				if (co[i] == 4) {
					state = 'O';
					break;
				}
				else if (cx[i] == 4) {
					state = 'X';
					break;
				}
			}
		}
		cout << "Case #" << cas++ << ": ";
		if (state == 0) {
			if (dots == 0) cout << "Draw" << endl;
			else cout << "Game has not completed" << endl;
		}
		else cout << state << " won" << endl;
	}
}
