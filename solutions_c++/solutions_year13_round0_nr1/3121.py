//#include <fstream> 
#include <iostream> 
#include <string> 
#include <list> 
#include <stack>
#include <sstream> 
#include <vector> 
#include <algorithm> 
#include <iomanip> 
#include <cmath>
#include <cstdio>
#include <map>
#include <queue>
#include <deque>
#include <set>
using namespace std;
 
int n;
bool x, o;
char ch;
vector <string> s;

bool check (int i, int j, int ii, int jj) {
	ch = s[i][j];
	if (ch == 'T') {
		ch = s[i + ii][j + jj];
	}
	int cnt = 0;
	while (cnt != 4) {
		if (s[i][j] != ch && s[i][j] != 'T') {
			return false;
		}
		i += ii;
		j += jj;
		cnt++;
	}
	return true;
}

void print () {
	if (x && o) {
		cout << "Draw";
		return;
	}
	if (x && !o) {
		cout << "X won";
		return;
	}
	if (!x && o) {
		cout << "O won";
		return;
	}
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (s[i][j] == '.') {
				cout << "Game has not completed";
				return;
			}
		}
	}
	cout << "Draw";
	return;
}

int main () {
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    //freopen("algo2.in", "r", stdin);freopen("algo2.out", "w", stdout);
	cin >> n;
	s.resize(4);
	for (int k = 1; k <= n; k++) {
		for (int j = 0; j < 4; j++) {
			cin >> s[j];
		}
		for (int i = 0; i < 4; i++) {
			if (check(i, 0, 0, 1)) {
				if (ch == 'X') {
					x = true;
				}
				if (ch == 'O') {
					o = true;
				}
			}
			if (check(0, i, 1, 0)) {
				if (ch == 'X') {
					x = true;
				}
				if (ch == 'O') {
					o = true;
				}
			}
		}
		if (check(0, 0, 1, 1)) {
			if (ch == 'X') {
				x = true;
			}
			if (ch == 'O') {
				o = true;
			}
		}
		if (check(3, 0, -1, 1)) {
			if (ch == 'X') {
				x = true;
			}
			if (ch == 'O') {
				o = true;
			}
		}
		cout << "Case #" << k << ": ";
		print();
		cout << "\n";
		x = false;
		o = false;
	}

    return 0;
}