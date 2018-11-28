//============================================================================
// Name        : cj_A.cpp
// Author      : huangxs139
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

char a[10][10];
bool xwon, owon, ep;

bool ck(int i1, int j1, int i2, int j2, int i3, int j3, int i4, int j4) {
	if (a[i1][j1] == '.' || a[i2][j2] == '.' || a[i3][j3] == '.' || a[i4][j4] == '.') {
		ep = 1;
		return 0;
	} else if ((a[i1][j1] == 'O' || a[i1][j1] == 'T') &&
			(a[i2][j2] == 'O' || a[i2][j2] == 'T') &&
			(a[i3][j3] == 'O' || a[i3][j3] == 'T') &&
			(a[i4][j4] == 'O' || a[i4][j4] == 'T')) {
		owon = 1;
		return 1;
	} else if ((a[i1][j1] == 'X' || a[i1][j1] == 'T') &&
			(a[i2][j2] == 'X' || a[i2][j2] == 'T') &&
			(a[i3][j3] == 'X' || a[i3][j3] == 'T') &&
			(a[i4][j4] == 'X' || a[i4][j4] == 'T')) {
		xwon = 1;
		return 1;
	}
	return 0;
}

int main() {
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("data2.out", "w", stdout);
	while (~scanf("%d", &t)) {
		for (int cas = 1; cas <= t; cas++) {
			for (int i = 0; i < 4; i++)
				scanf("%s", a[i]);
			xwon = owon = ep = 0;
			for (int i = 0; i < 4; i++) {
				if (ck(i, 0, i, 1, i, 2, i, 3)) break;
				if (ck(0, i, 1, i, 2, i, 3, i)) break;
			}
			ck(0, 0, 1, 1, 2, 2, 3, 3);
			ck(0, 3, 1, 2, 2, 1, 3, 0);
			if (xwon)
				printf("Case #%d: X won\n", cas);
			else if (owon)
				printf("Case #%d: O won\n", cas);
			else if (ep)
				printf("Case #%d: Game has not completed\n", cas);
			else
				printf("Case #%d: Draw\n", cas);
		}
	}
	return 0;
}
