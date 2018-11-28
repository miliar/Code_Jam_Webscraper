#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <functional>
#include <map>
#include <deque>
#include <set>

using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(n);(i)++)

inline bool check(char a, char b, char c, char d, char g)
{
	if (a != g && a != 'T') return false;
	if (b != g && b != 'T') return false;
	if (c != g && c != 'T') return false;
	if (d != g && d != 'T') return false;
	return true;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		string a[4];
		for (int i = 0; i < 4; i++) cin >> a[i];
		bool x_win = false, o_win = false, is_end = true;
		REP(i,4) REP(j,4) { if (a[i][j] == '.') is_end = false; }
		
		REP(i, 4) if (check(a[i][0], a[i][1], a[i][2], a[i][3], 'O')) o_win = true;
		REP(i, 4) if (check(a[0][i], a[1][i], a[2][i], a[3][i], 'O')) o_win = true;
		if (check(a[0][0], a[1][1], a[2][2], a[3][3], 'O')) o_win = true;
		if (check(a[3][0], a[2][1], a[1][2], a[0][3], 'O')) o_win = true;

		REP(i, 4) if (check(a[i][0], a[i][1], a[i][2], a[i][3], 'X')) x_win = true;
		REP(i, 4) if (check(a[0][i], a[1][i], a[2][i], a[3][i], 'X')) x_win = true;
		if (check(a[0][0], a[1][1], a[2][2], a[3][3], 'X')) x_win = true;
		if (check(a[3][0], a[2][1], a[1][2], a[0][3], 'X')) x_win = true;

		if (x_win) {
			printf("Case #%d: X won\n", t+1);
		} else if (o_win) {
			printf("Case #%d: O won\n", t+1);
		} else if (is_end) {
			printf("Case #%d: Draw\n", t+1);
		} else {
			printf("Case #%d: Game has not completed\n", t+1);
		}

	}

	return 0;
}


