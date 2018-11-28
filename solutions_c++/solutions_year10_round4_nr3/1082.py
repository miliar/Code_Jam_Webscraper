#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int B[2][50000][2];
int nB[2];
int turn;

int map[2][300][300];

void addB(int x, int y) {

	int j;
	if (x + 150 < 0 || x + 150 >= 300 ||
		y + 150 < 0 || y + 150 >= 300) {
		printf ("larger!\n");
		j = 1 / 0;
	}
	if (map[turn][x+150][y+150] == 1) {
		return;
	}
	map[turn][x+150][y+150] = 1;
	B[turn][nB[turn]][0] = x;
	B[turn][nB[turn]][1] = y;
	nB[turn]++;
}

int main() {

	int T;
	int i, j, k;
	int R;
	int caseid;
	int alive;
	int mask;
	int ans;
	int oldTurn, nextTurn;

	scanf("%d", &T);
	for (caseid = 1; caseid <= T; caseid++) {

		memset(map, 0, sizeof(map));
		scanf("%d", &R);
		nB[0] = 0;
		turn = 0;
		for (i = 0; i < R; i++) {
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (j = x1; j <= x2; j++) {
			for (k = y1; k <= y2; k++) {
				addB(j, k);
			}
			}
		}

		ans = 0;
		alive = (nB[0] > 0);
		while(alive) {

			oldTurn = turn;
			nextTurn = (turn + 1) % 2;

			turn = nextTurn;
			nB[turn] = 0;

			ans++;

			for (i = 0; i < nB[oldTurn]; i++) {
				/* check if this cell die */
				mask = 0;
				if (map[oldTurn][B[oldTurn][i][0]-1+150][B[oldTurn][i][1]  +150] ||
					map[oldTurn][B[oldTurn][i][0]  +150][B[oldTurn][i][1]-1+150]) {
					addB(B[oldTurn][i][0], B[oldTurn][i][1]);
				}

				/* check if this cell gen new cell */
				if (map[oldTurn][B[oldTurn][i][0]+1+150][B[oldTurn][i][1]-1+150]) {
					addB(B[oldTurn][i][0]+1, B[oldTurn][i][1]);
				}

				/* check if this cell gen new cell */
				if (map[oldTurn][B[oldTurn][i][0]-1+150][B[oldTurn][i][1]+1+150]) {
					addB(B[oldTurn][i][0], B[oldTurn][i][1]+1);
				}
			}


			memset(map[oldTurn], 0, sizeof(map[0]));
			/*
					printf ("add %d %d\n", B[oldTurn][i][0], B[oldTurn][i][1]);

			printf ("nB[oldTurn] is %d nNewB is %d\n", nB[oldTurn], nNewB);
			for (i = 0; i < nNewB; i++) {
				printf ("%d %d\n", newB[i][0], newB[i][1]);
			}
			*/

			alive = (nB[turn] > 0);
		}

		printf ("Case #%d: %d\n", caseid, ans);
	}

	return 0;
}
