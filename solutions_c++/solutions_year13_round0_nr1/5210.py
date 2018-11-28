#include <iostream>
#include <string>

using namespace std;

string c[11];

bool check(char t) {
	int cnt;
	for (int i = 0; i < 4; ++ i) {
		cnt = 0;
		for (int j = 0; j < 4; ++ j)
			cnt += c[i][j] == t || c[i][j] == 'T';
		if (cnt == 4) return true;
	}
	
	for (int i = 0; i < 4; ++ i) {
		cnt = 0;
		for (int j = 0; j < 4; ++ j)
			cnt += c[j][i] == t || c[j][i] == 'T';;
		if (cnt == 4) return true;
	}

	cnt = 0;
	for (int i = 0; i < 4; ++ i)
		cnt += c[i][i] == t || c[i][i] == 'T';;
	if (cnt == 4) return true;

	cnt = 0;
	for (int i = 0; i < 4; ++ i)
		cnt += c[i][3 - i] == t || c[i][3 - i] == 'T';;
	if (cnt == 4) return true;

	return false;
}

int main() {
	int tn;
	cin >> tn;
	for (int t = 1; t <= tn; ++ t) {
		for (int i = 0; i < 4; ++ i) {
			cin >> c[i];
		}

		if (check('O')) {
			cout << "Case #" << t << ": " << "O won" << endl;
			continue;
		}

		if (check('X')) {
			cout << "Case #" << t << ": " << "X won" << endl;
			continue;
		}

		bool ok = true;
		for (int i = 0; i < 4; ++ i)
			for (int j = 0; j < 4; ++ j)
				ok = ok && c[i][j] != '.';
		if (ok) {
			cout << "Case #" << t << ": " << "Draw" << endl;
			continue;
		}

		cout << "Case #" << t << ": " << "Game has not completed" << endl;

	}
	return 0;
}
