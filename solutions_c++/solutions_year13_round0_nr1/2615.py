#include <iostream>
#include <stdio.h>
using namespace std;
char a[5][5];
void getinput()
{
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; ++j) {
			cin>>a[i][j];
		}
	}
}
int solve()
{
	int nc = 0;
	//row
	for (int i = 0; i < 4; ++i) {
		int x = 0;
		int o = 0;
		int t = 0;
		for (int j = 0; j < 4; ++j) {
			if (a[i][j] == 'X')
				x++;
			else if (a[i][j] == 'O') {
				o++;
			} else if (a[i][j] == 'T') {
				t++;
			} else if (a[i][j] == '.') {
				nc = 1;
			}
		}
		if (x + t == 4) {
			return 0;
		}
		if (o + t == 4) {
			return 1;
		}
	}
	//column
	for (int i = 0; i < 4; ++i) {
		int x = 0;
		int o = 0;
		int t = 0;
		for (int j = 0; j < 4; ++j) {
			if (a[j][i] == 'X')
				x++;
			else if (a[j][i] == 'O') {
				o++;
			} else if (a[j][i] == 'T') {
				t++;
			}
		}
		if (x + t == 4) {
			return 0;
		}
		if (o + t == 4) {
			return 1;
		}
	}
	int x = 0;
	int o = 0;
	int t = 0;
	for (int i = 0; i < 4; ++i) {
		if (a[i][i] == 'X') {
			x++;
		} else if (a[i][i] == 'O') {
			o++;
		} else if (a[i][i] == 'T') {
			t++;
		}
	}
	if (x + t == 4) {
		return 0;
	}	
	if (o + t == 4) {
		return 1;
	}
	x = 0;
	o = 0;
	t = 0;
	for (int i = 0; i < 4; ++i) {
		if (a[3 - i][i] == 'X') {
			x++;
		} else if (a[3 - i][i] == 'O') {
			o++;
		} else if (a[3 - i][i] == 'T') {
			t++;
		}
	}
	if (x + t == 4)
		return 0;
	if (o + t == 4)
		return 1;
	if (!nc) {
		return 2;
	}
	return 3;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		getinput();
		int ans = solve();
		if (ans == 0) {
			printf("Case #%d: X won\n", i);
		}
		if (ans == 1) {
			printf("Case #%d: O won\n", i);
		}
		if (ans == 2) {
			printf("Case #%d: Draw\n", i);
		}
		if (ans == 3) {
			printf("Case #%d: Game has not completed\n", i);
		}
	}
}