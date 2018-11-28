#pragma comment(linker, "/stack:256000000")

#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <cassert>
#include <queue>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()

string s[4];

bool check_win(char c) {
	REP(i, 4) {
		bool OK = 1;
		REP(j, 4) {
			if (s[i][j] != c && s[i][j] != 'T') {
				OK = 0;
				break;
			}
		}
		if (OK) return 1;
	}
	REP(j, 4) {
		bool OK = 1;
		REP(i, 4) {
			if (s[i][j] != c && s[i][j] != 'T') {
				OK = 0;
				break;
			}
		}
		if (OK) return 1;
	}
	bool OK = 1;
	REP(i, 4) {
		if (s[i][i] != c && s[i][i] != 'T') {
			OK = 0;
			break;
		}
	}
	if (OK) return 1;
	OK = 1;
	REP(i, 4) {
		if (s[i][3 - i] != c && s[i][3 - i] != 'T') {
			OK = 0;
			break;
		}
	}
	if (OK) return 1;
	return 0;
}

int count_cells() {
	int res = 0;
	REP(i, 4) REP(j, 4) {
		if (s[i][j] != '.') ++res;
	}
	return res;
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long start = clock();
#endif
	int tst;
	cin >> tst;
	for (int test = 1; test <= tst; test++) {
		printf("Case #%d: ", test);
		REP(i, 4) cin >> s[i];
		if (check_win('X')) cout << "X won";
		else if (check_win('O')) cout << "O won";
		else if (count_cells() == 16) cout << "Draw";
		else cout << "Game has not completed";
		printf("\n");
	}
#ifdef LOCAL
	fprintf(stderr, "\n\nTime: %.3lf\n\n", (clock() - start) / 1000.);
#endif
	return 0;
}