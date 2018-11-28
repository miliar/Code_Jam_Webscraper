#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define xwon "X won"
#define owon "O won"
#define draw "Draw"
#define nc "Game has not completed"

string a[10];

bool isx(int i, int j) {
	return a[i][j] == 'X' || a[i][j] == 'T';
}

bool iso(int i, int j) {
	return a[i][j] == 'O' || a[i][j] == 'T';
}

bool isdot(int i, int j) {
	return a[i][j] == '.';
}

string doit() {
	bool over = true;

	for (int i = 0; i < 4; ++i) {
		int cntx = 0, cnto = 0;
		for (int j = 0; j < 4; ++j) {
			if (isdot(i, j)) over = false;
			if (isx(i, j)) ++cntx;
			if (iso(i, j)) ++cnto;
		}
		if (cntx == 4) return xwon;
		if (cnto == 4) return owon;
	}

	for (int j = 0; j < 4; ++j) {
		int cntx = 0, cnto = 0;
		for (int i = 0; i < 4; ++i) {
			if (isdot(i, j)) over = false;
			if (isx(i, j)) ++cntx;
			if (iso(i, j)) ++cnto;
		}
		if (cntx == 4) return xwon;
		if (cnto == 4) return owon;
	}

	int cntx = 0, cnto = 0;
	for (int i = 0; i < 4; ++i) {
		if (isx(i, i)) ++cntx;
		if (iso(i, i)) ++cnto;
	}
	if (cntx == 4) return xwon;
	if (cnto == 4) return owon;

	cntx = 0, cnto = 0;
	for (int i = 0; i < 4; ++i) {
		if (isx(i, 3-i)) ++cntx;
		if (iso(i, 3-i)) ++cnto;
	}
	if (cntx == 4) return xwon;
	if (cnto == 4) return owon;

	if (over) return draw;
	return nc;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int ntest;
	cin >> ntest;

	for (int test = 1; test <= ntest; ++test) {
		for (int i = 0; i < 4; ++i) cin >> a[i];
		cout << "Case #" << test << ": " << doit() << endl;
	}

	return 0;
}
