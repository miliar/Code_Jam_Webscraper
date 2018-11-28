#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;

int NOTFINISHED, XWON, OWON;
string a[4];

void test(int i1, int j1, int i2, int j2, int i3, int j3, int i4, int j4) {
	int X = 0, O = 0, T = 0;
	if (a[i1][j1] == 'X') X++;
	if (a[i1][j1] == 'O') O++;
	if (a[i1][j1] == 'T') T++;
	if (a[i2][j2] == 'X') X++;
	if (a[i2][j2] == 'O') O++;
	if (a[i2][j2] == 'T') T++;
	if (a[i3][j3] == 'X') X++;
	if (a[i3][j3] == 'O') O++;
	if (a[i3][j3] == 'T') T++;
	if (a[i4][j4] == 'X') X++;
	if (a[i4][j4] == 'O') O++;
	if (a[i4][j4] == 'T') T++;
	if (X + O + T == 4) {
		if (X == 0 && T < 4) OWON = true;
		if (O == 0 && T < 4) XWON = true;
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int task, TT = 0;
	scanf("%d", &task);
	while (task --) {
		NOTFINISHED = false; XWON = false; OWON = false;
		for (int i = 0; i < 4; i++) cin >> a[i];
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (a[i][j] == '.') NOTFINISHED = true;
		for (int i = 0; i < 4; i++) test(i, 0, i, 1, i, 2, i, 3);
		for (int i = 0; i < 4; i++) test(0, i, 1, i, 2, i, 3, i);
		test(0, 0, 1, 1, 2, 2, 3, 3);
		test(3, 0, 2, 1, 1, 2, 0, 3);
		printf("Case #%d: ", ++TT);
		
		if (XWON) printf("X won\n"); else
		if (OWON) printf("O won\n"); else
		if (NOTFINISHED) printf("Game has not completed\n"); else
		printf("Draw\n");
	}
	return 0;
}
