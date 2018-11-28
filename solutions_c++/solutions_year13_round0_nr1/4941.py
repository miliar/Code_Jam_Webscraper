#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <sstream>
#include <numeric>
#include <climits>
#include <string>
#include <cctype>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

#define foreach(e, x) for (__typeof((x).begin()) e = (x).begin(); e != (x).end(); ++e)

char mat[9][9];

bool check(char x) {
	for (int i = 0; i < 4; ++i) {
		bool f1 = true, f2 = true;
		for (int j = 0; j < 4; ++j) {
			f1 &= mat[i][j] == 'T' || mat[i][j] == x;
			f2 &= mat[j][i] == 'T' || mat[j][i] == x;
		}
		if (f1 || f2) {
			return true;
		}
	}
	bool f1 = true, f2 = true;
	for (int i = 0; i < 4; ++i) {
		f1 &= mat[i][i] == 'T' || mat[i][i] == x;
		f2 &= mat[i][3 - i] == 'T' || mat[i][3 - i] == x;
	}
	return f1 || f2;
}

int main() {
	int tests;
	scanf("%d", &tests);
	for (int ctrl = 1; ctrl <= tests; ctrl++) {
		bool full = true;
		for (int i = 0; i < 4; ++i) {
			scanf("%s", mat[i]);
			for (int j = 0; j < 4; ++j) {
				if (mat[i][j] == '.') {
					full = false;
				}
			}
		}
		printf("Case #%d: ", ctrl);
		if (check('X')) {
			puts("X won");
			continue;
		}
		if (check('O')) {
			puts("O won");
			continue;
		}
		puts(full ? "Draw" : "Game has not completed");
	}
}

