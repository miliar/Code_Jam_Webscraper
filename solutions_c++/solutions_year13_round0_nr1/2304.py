#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

string a[4];

void Load()
{
	string s;
	getline(cin, s);
	for (int i = 0; i < 4; i++) {
		getline(cin, a[i]);
	}
}

bool CheckLine(int bx, int by, int dx, int dy, char c)
{
	int i;
	for (i = 0; i < 4; i++) {
		if (a[bx][by] != c && a[bx][by] != 'T') return false;
		bx += dx;
		by += dy;
	}
	return true;
}

void Solve()
{
	int i, j;
	bool dot = false;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++)
			if (a[i][j] == '.') dot = true;
	}
	for (char c = 'O' ; c <= 'X'; c += (int)'X'-(int)'O') {
		bool won = false;
		for (i = 0; i < 4; i++) {
			won |= CheckLine(i, 0, 0, 1, c);
			won |= CheckLine(0, i, 1, 0, c);
		}
		won |= CheckLine(0, 0, 1, 1, c);
		won |= CheckLine(3, 0, -1, 1, c);
		if (won) {
			cout << c << " won\n"; 
			return;
		}
	}
	if (dot) cout << "Game has not completed\n";
	else cout << "Draw\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
