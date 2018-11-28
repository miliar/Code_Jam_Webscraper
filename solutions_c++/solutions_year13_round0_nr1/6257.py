#include <iostream>
using namespace std;

int n;
int cases = 0;

bool check(char pan[4][4], char player)
{
	// vertical
	for (int i=0; i<4; ++i) {
		bool isWin = true;
		for (int j=0; isWin && j<4; ++j) {
			if (pan[i][j] != player && pan[i][j] != 'T')
				isWin = false;
		}

		if (isWin) return true;
	}

	// horizontal
	for (int i=0; i<4; ++i) {
		bool isWin = true;
		for (int j=0; isWin && j<4; ++j) {
			if (pan[j][i] != player && pan[j][i] != 'T')
				isWin = false;
		}

		if (isWin) return true;
	}

	// diagonal
	bool isWin = true;
	for (int i=0; isWin && i<4; ++i) {
		if (pan[i][i] != player && pan[i][i] != 'T')
			isWin = false;
	}
	if (isWin) return true;

	isWin = true;
	for (int i=0; isWin && i<4; ++i) {
		if (pan[3-i][i] != player && pan[3-i][i] != 'T')
			isWin = false;
	}
	if (isWin) return true;

	return false;
}

void solve()
{
	char pan[4][4];
	double not_full = false;

	for (int i=0; i<4; ++i) {
		for (int j=0; j<4; ++j) {
			cin >> pan[i][j];
			if (pan[i][j] == '.')
				not_full = true;
		}
	}

	if (check(pan, 'O'))
		cout << "Case #" << (++cases) << ": O won\n";
	else if (check(pan, 'X'))
		cout << "Case #" << (++cases) << ": X won\n";
	else {
		if (not_full)
			cout << "Case #" << (++cases) << ": Game has not completed\n";
		else
			cout << "Case #" << (++cases) << ": Draw\n";
	}
}

int main()
{
	cin >> n;
	while (n --> 0) {
		solve();
	}
}