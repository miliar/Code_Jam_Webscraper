#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

const int Max = 10;

bool checkColumn(char a[Max][Max], int col, char sym) {
	bool ok = true;
	for (int i = 0; i < 4; i++) {
		if (a[i][col] != sym && a[i][col] != 'T') {
			ok = false;
		}
	}

	return ok;
}

bool checkRow(char a[Max][Max], int row, char sym) {
	bool ok = true;
	for (int i = 0; i < 4; i++) {
		if (a[row][i] != sym && a[row][i] != 'T') {
			ok = false;
		}
	}

	return ok;
}

bool checkAllRows(char a[Max][Max], char sym) {
	bool ok = false;
	for (int i = 0; i < 4; i++) {
		ok |= checkRow(a, i, sym);
	}
	return ok;
}

bool checkAllCols(char a[Max][Max], char sym) {
	bool ok = false;
	for (int i = 0; i < 4; i++) {
		ok |= checkColumn(a, i, sym);
	}
	return ok;
}

bool checkDiags(char a[Max][Max], char sym) {
	int i = 0, j = 0;
	bool ok = true;
	while (i < 4) {
		if (a[i][j] != sym && a[i][j] != 'T') {
			ok = false;
		}
		i++;
		j++;
	}

	if (ok) {
		return ok;
	}

	i = 3, j = 0;
	ok = true;

	while (j < 4) {
		if (a[i][j] != sym && a[i][j] != 'T') {
			ok = false;
		}
		i--;
		j++;
	}

	return ok;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	char a[Max][Max];
	char input[5];
	int n;

	cin >> n;
	for (int t = 0; t < n; t++) {
		bool full = true;

		for (int i = 0; i < 4; i++) {
			cin >> a[i];
			for (int j = 0; j < 4; j++) {
				if (a[i][j] == '.') {
					full = false;
				}
			}
		}
		//cin >> input;

		if (checkAllRows(a, 'O') || checkAllCols(a, 'O') || checkDiags(a, 'O')) {
			printf("Case #%d: O won\n", t + 1);
		}
		else if (checkAllRows(a, 'X') || checkAllCols(a, 'X') || checkDiags(a, 'X')) {
			printf("Case #%d: X won\n", t + 1);
		}
		else if (full) {
			printf("Case #%d: Draw\n", t + 1);
		}
		else {
			printf("Case #%d: Game has not completed\n", t + 1);
		}
	}
	
	return 0;
}