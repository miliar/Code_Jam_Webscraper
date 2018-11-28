#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>

#define SIZE 4

using namespace std;

char b[SIZE][SIZE];

bool ok(int x, int y, char c) {
	return b[x][y] == c || b[x][y] == 'T';
}

bool check(char c) {
	for (int i = 0; i < SIZE; ++i) {
		bool good = true;
		for (int j = 0; j < SIZE && good; ++j)
			if (!ok(i, j, c))
				good = false;
		if (good)
			return true;
	}
	for (int i = 0; i < SIZE; ++i) {
		bool good = true;
		for (int j = 0; j < SIZE && good; ++j)
			if (!ok(j, i, c))
				good = false;
		if (good)
			return true;
	}
	if ((ok(0, 0, c) && ok(1, 1, c) && ok(2, 2, c) && ok(3, 3, c)) ||
		(ok(3, 0, c) && ok(2, 1, c) && ok(1, 2, c) && ok(0, 3, c)))
		return true;
	return false;
}

bool full() {
	for (int i = 0; i < SIZE; ++i)
		for (int j = 0; j < SIZE; ++j)
			if (b[i][j] == '.')
				return false;
	return true;
}


int main() {
	int t;
	cin >> t;
	for (int tNow = 1; tNow <= t; ++tNow) {
		for (int i = 0; i < SIZE; ++i)
			for (int j = 0; j < SIZE; ++j)
				cin >> b[i][j];
		cout << "Case #" << tNow << ": ";
		if (check('X'))
			cout << "X won";
		else if (check('O'))
			cout << "O won";
		else if (full())
			cout << "Draw";
		else
			cout << "Game has not completed";
		cout << endl;
	}
	return 0;
}
