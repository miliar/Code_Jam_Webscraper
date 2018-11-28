#include <cstdio>
#include <iostream>

using namespace std;

char a[5][5];

bool is(char x, char y) {
	return x == y || x == 'T';
}

bool check(char c) {
	for(int i = 0; i < 4; ++i) {
		bool win = true;
		for(int j = 0; j < 4; ++j) {
			if(!is(a[i][j], c)) {
				win = false;
			}
		}
		if(win) return true;
	}
	for(int j = 0; j < 4; ++j) {
		bool win = true;
		for(int i = 0; i < 4; ++i) {
			if(!is(a[i][j], c)) {
				win = false;
			}
		}
		if(win) return true;
	}
	bool win = true;
	for(int i = 0; i < 4; ++i) {
		if(!is(a[i][i], c)) {
			win = false;
		}
	}
	if(win) return true;

	win = true;
	for(int i = 0; i < 4; ++i) {
		if(!is(a[i][3 - i], c)) {
			win = false;
		}
	}
	if(win) return true;
	return false;
}

int main(int argc, char **argv) {
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		for(int i = 0; i < 4; ++i) {
			cin >> a[i];
		}
		cout << "Case #" << t << ": ";
		if(check('X')) {
			cout << "X won" << endl;
		} else if(check('O')) {
			cout << "O won" << endl;
		} else {
			bool isend = true;
			for(int i = 0; i < 4; ++i) {
				for(int j = 0; j < 4; ++j) {
					if(a[i][j] == '.') {
						isend = false;
					}
				}
			}
			if(!isend) {
				cout << "Game has not completed" << endl;
			} else {
				cout << "Draw" << endl;
			}
		}
	}
}
