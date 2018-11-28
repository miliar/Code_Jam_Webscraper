#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string  mp[4];

bool IsWon(char symbol) {
	for (int i = 0; i < 4; i++) {
		int j;
		for (j = 0; j < 4; j++) {
			if (mp[i][j] != symbol && mp[i][j] != 'T')
				break;
		}
		if (j == 4) return true;

		for (j = 0; j < 4; j++) {
			if (mp[j][i] != symbol && mp[j][i] != 'T')
				break;
		}
		if (j == 4) return true;
	}

	int i;
	for (i = 0; i < 4; i++) {
		if (mp[i][i] != symbol && mp[i][i] != 'T')
			break;
	}
	if (i == 4) return true;

	for (i = 0; i < 4; i++) {
		if (mp[i][4 - i - 1] != symbol && mp[i][4 - i - 1] != 'T')
			break;
	}
	if (i == 4) return true;

	return false;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	
	for (int cas = 1; cas <= T; cas++) {
		for (int i = 0; i < 4; i++)
			cin >> mp[i];

		if (IsWon('X')) {
			cout << "Case #" << cas << ": X won\n";
		} else if (IsWon('O')) {
			cout << "Case #" << cas << ": O won\n";
		} else {
			bool is_full = true;
			for (int i = 0; is_full && i < 4; i++) for (int j = 0; j < 4; j++) {
				if (mp[i][j] == '.') {
					is_full = false;
					break;
				}
			}

			if (is_full) cout << "Case #" << cas << ": Draw\n";
			else cout << "Case #" << cas << ": Game has not completed\n";
		}
	}

	// system("pause");
	return 0;
}
