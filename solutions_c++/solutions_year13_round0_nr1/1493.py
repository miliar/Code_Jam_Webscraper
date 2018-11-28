#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

int test;
char a[4][4];
bool completed;
const int ci[] = {1, 0, 1, 1};
const int cj[] = {0, 1, 1, -1};

bool check(char c) {
	completed = 1;
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++) {
			if (a[i][j] == '.') completed = 0;
			for(int k = 0; k < 4; k++) {
				int ii = i, jj = j, cnt = 0;	
				while (ii >= 0 && ii < 4 && jj >= 0 && jj < 4 && (a[ii][jj] == 'T' || a[ii][jj] == c)) {
					ii += ci[k];
					jj += cj[k];
					cnt++;
				}
				if (cnt == 4) return 1;
			}
		}
	return 0;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("Tic-Tac-Toe-Tomek.out", "w", stdout);

	scanf("%d", &test);
	for(int tcase = 1; tcase <= test; tcase++) {
		printf("Case #%d: ", tcase);
		for(int i = 0; i < 4; i++) scanf("%s", a[i]);
		if (check('X')) printf("X won\n");
		else if (check('O')) printf("O won\n");
		else if (completed) printf("Draw\n");
		else printf("Game has not completed\n");
	}

	return 0;
}