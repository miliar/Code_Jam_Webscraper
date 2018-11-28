#include <iostream>

using namespace std;

int T;
string ttt[4];

int main() {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		bool xwon = false, owon = false, finished = true;
		for (int i = 0; i < 4; i++) {
			cin >> ttt[i];
			for (int j = 0; j < 4; j++) {
				if (ttt[i][j] == '.') {
					finished = false;
				}
			}
		}
		string str3 = "", str4 = "";
		for (int i = 0; i < 4; i++) {
			string str = "";
			string str2 = "";
			if (ttt[i][i] != 'T') {
				str3 += ttt[i][i];
			}
			if (ttt[i][3 - i] != 'T') {
				str4 += ttt[i][3 - i];
			}
			for (int j = 0; j < 4; j++) {
				if (ttt[i][j] != 'T') {
					str += ttt[i][j];
				}
				if (ttt[j][i] != 'T') {
					str2 += ttt[j][i];
				}
			}
			if (str == "OOO" || str2 == "OOO" || str == "OOOO" || str2 == "OOOO") {
				owon = true;
			}
			if (str == "XXX" || str2 == "XXX" || str == "XXXX" || str2 == "XXXX") {
				xwon = true;
			}
		}
		if (str3 == "OOO" || str4 == "OOO" || str3 == "OOOO" || str4 == "OOOO") {
			owon = true;
		}
		if (str3 == "XXX" || str4 == "XXX" || str3 == "XXXX" || str4 == "XXXX") {
			xwon = true;
		}
		if (xwon) {
			puts("X won");
		} else if (owon) {
			puts("O won");
		} else if (finished) {
			puts("Draw");
		} else {
			puts("Game has not completed");
		}
	}
	return 0;
}