#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main () {
	int T, specr = -1, specc;
	char c, player;
	bool diag1, diag2, row, col, empty, res, out;
	vector <int> help (4, -1);
	vector <vector <int> > table (4, help);
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		specr = -1;
		out = false;
//		diag1 = true;
//		diag2 = true;
		empty = false;
		res = false;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf(" %c", &c);
				if (c == 'X') table [j] [k] = 0;
				if (c == 'O') table [j] [k] = 1;
				if (c == 'T') {
					specr = j;
					specc = k;
					table [j] [k] = 0;
				}
				if (c == '.') {
					empty = true;
					table [j] [k] = -1;
				}
//				printf("%d", table [j] [k]);
			}
//			printf("\n");
		}
//		printf("%d %d\n", specr, specc);
		player = 'X';
		for (int mwahaha = 0; mwahaha < 2; mwahaha++) {
			res = false;
			diag1 = true;
			diag2 = true;
			for (int j = 0; j < 4; j++) {
				row = true;
				col = true;
				for (int k = 0; k < 4; k++) {
					if (table [j] [k] != 0) row = false;
					if (table [k] [j] != 0) col = false;
				}
				if (row || col) res = true;
				if (table [j] [j] != 0) diag1 = false;
				if (table [j] [3 - j] != 0) diag2 = false;
			}
			if (diag1 || diag2) res = true;
			if (res) {
				printf("Case #%d: %c won\n", i + 1, player);
				out = true;
			}
			player = 'O';
			for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					table [j] [k] = 1 - table [j] [k];
//					printf("%d", table [j] [k]);
				}
//				printf("\n");
			}
			if (specr != -1) table [specr] [specc] = 0;
	/*		for (int j = 0; j < 4; j++) {
				for (int k = 0; k < 4; k++) {
					printf("%d", table [j] [k]);
				}
				printf("\n");
			}*/
		}
		if (!out) {
			if (empty) printf("Case #%d: Game has not completed\n", i + 1);
			else printf("Case #%d: Draw\n", i + 1);
		}
	}
	return 0;
}