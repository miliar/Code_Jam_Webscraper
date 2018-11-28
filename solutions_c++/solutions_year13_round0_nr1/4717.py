#include <cstdio>

bool found;
char outcome;
char g[4][4];
void check(int x, int y, int dx, int dy) {
	if (!found) {
		int xcount = 0, ocount = 0, tcount = 0;
		for (int i = 0; i < 4; i++) {
			if (g[x][y] == 'X') {
				xcount++;
			} else if (g[x][y] == 'O') {
				ocount++;
			} else if (g[x][y] == 'T') {
				tcount++;
			}
			x += dx;
			y += dy;
		}
		if (xcount == 4 || (xcount == 3 && tcount == 1)) {
			found = true;
			outcome = 'X';
		} 
		if (ocount == 4 || (ocount == 3 && tcount == 1)) {
			found = true;
			outcome = 'O';
		}
	}
}

int main() {
	int ncases;
	scanf("%d", &ncases);
	for (int tcase = 1; tcase <= ncases; tcase++) {
		bool hasDot = false;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				do {
					g[i][j] = fgetc(stdin);
				} while (g[i][j] != 'X' && g[i][j] != 'T' && g[i][j] != 'O' && g[i][j] != '.');
				if (g[i][j] == '.') {
					hasDot = true;
				}
			}
		}

		found = false;
		check(0, 0, 0, 1);
		check(1, 0, 0, 1);
		check(2, 0, 0, 1);
		check(3, 0, 0, 1);
		check(0, 0, 1, 0);
		check(0, 1, 1, 0);
		check(0, 2, 1, 0);
		check(0, 3, 1, 0);
		check(0, 0, 1, 1);
		check(0, 3, 1, -1);
		if (found) {
			if (outcome == 'X') {
				printf("Case #%d: X won\n", tcase);
			} else {
				printf("Case #%d: O won\n", tcase);
			}
		} else {
			if (hasDot) {
				printf("Case #%d: Game has not completed\n", tcase);
			} else {
				printf("Case #%d: Draw\n", tcase);
			}
		}
	}
}
