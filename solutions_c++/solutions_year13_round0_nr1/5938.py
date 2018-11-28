// test1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	int num, i, j, k;
	char grid[4][4], ret;
	char w;
	bool O, X, D, TD;
	FILE* fin = fopen("A-large.in", "r");
	fscanf(fin, "%d\n", &num);
	for(k = 1; k <= num; k++) {
		TD = 0;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				fscanf(fin, "%c", &grid[i][j]);
				if (grid[i][j] == '.') {
					TD = 1;
				}
			}
			fscanf(fin, "%c", &ret);
		}
		fscanf(fin, "%c", &ret);
		w = 0;
		//check row
		for (i = 0; i < 4; i++) {
			O = X = D = 0;
			for (j = 0; j < 4; j++) {
				if (grid[i][j] == 'O') {
					O = 1;
					//okay
				} else if (grid[i][j] == 'X') {
					X = 1;
				} else if (grid[i][j] == '.') {
					D = 1;
				}
			}
			if (O == 1 && X == 0 && D == 0) {
				w = 'O';
				goto win;
			} else if (X == 1 && O == 0 && D == 0) {
				w = 'X';
				goto win;
			}

		}
		//check col
		for (j = 0; j < 4; j++) {
			O = X = D = 0;
			for (i = 0; i < 4; i++) {
				if (grid[i][j] == 'O') {
					O = 1;
					//okay
				} else if (grid[i][j] == 'X') {
					X = 1;
				} else if (grid[i][j] == '.') {
					D = 1;
				}  else if (grid[i][j] == '.') {
					D = 1;
				}
			}
			if (O == 1 && X == 0 && D == 0) {
				w = 'O';
				goto win;
			} else if (X == 1 && O == 0 && D == 0) {
				w = 'X';
				goto win;
			}
		}
		//check left-right
		O = X = D = 0;
		for (i = 0, j = 0; i < 4 && j < 4; i++, j++) {
			if (grid[i][j] == 'O') {
				O = 1;
				//okay
			} else if (grid[i][j] == 'X') {
				X = 1;
			} else if (grid[i][j] == '.') {
				D = 1;
			}
		}
		if (O == 1 && X == 0 && D == 0) {
			w = 'O';
			goto win;
		} else if (X == 1 && O == 0 && D == 0) {
			w = 'X';
			goto win;
		}

		//check right-left
		O = X = D = 0;
		for (i = 0, j = 3; i < 4 && j >=0; i++, j--) {
			if (grid[i][j] == 'O') {
				O = 1;
				//okay
			} else if (grid[i][j] == 'X') {
				X = 1;
			} else if (grid[i][j] == '.') {
				D = 1;
			}
		}
		if (O == 1 && X == 0 && D == 0)
			w = 'O';
		else if (X == 1 && O == 0 && D == 0)
			w = 'X';
win:
		if (w == 'O' || w == 'X')
			printf("Case #%d: %c won\n", k, w);
		else if (TD)
			printf("Case #%d: Game has not completed\n", k);
		else
			printf("Case #%d: Draw\n", k); 

	}
	fclose(fin);

	return 0;
}

