#include <stdio.h>
#include <string.h>

int main()
{
	int n;
	char table[4][10];
	char xtable[4][5];
	char otable[4][5];
	char line[16];
	int count;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d\n", &n);

	int status;
	for (int m = 0 ; m < n ; ++m) {
		for (int j = 0 ; j < 4 ; ++j) {
			fgets((char *)&table[j], 10, stdin);
			memcpy(&xtable[j], &table[j], 4);
			memcpy(&otable[j], &table[j], 4);

			for (int k = 0 ; k < 4 ; ++k) {
				if (xtable[j][k] == 'T') xtable[j][k] = 'X';
				if (otable[j][k] == 'T') otable[j][k] = 'O';
			}
		}
		fgets(line, 16, stdin);

		for (int i = 0 ; i < 4 ; ++i) {
			if (xtable[i][0] == xtable[i][1] &&
				xtable[i][0] == xtable[i][2] &&
				xtable[i][0] == xtable[i][3] &&
				xtable[i][0] == 'X') {
				status = 0;
				goto done;
			}

			if (otable[i][0] == otable[i][1] &&
				otable[i][0] == otable[i][2] &&
				otable[i][0] == otable[i][3] &&
				otable[i][0] == 'O') {
				status = 1;
				goto done;
			}
		}

		for (int i = 0 ; i < 4 ; ++i) {
			if (xtable[0][i] == xtable[1][i] &&
				xtable[0][i] == xtable[2][i] &&
				xtable[0][i] == xtable[3][i] &&
				xtable[0][i] == 'X') {
				status = 0;
				goto done;
			}

			if (otable[0][i] == otable[1][i] &&
				otable[0][i] == otable[2][i] &&
				otable[0][i] == otable[3][i] &&
				otable[0][i] == 'O') {
				status = 1;
				goto done;
			}
		}

		if (xtable[0][0] == xtable[1][1] &&
			xtable[0][0] == xtable[2][2] &&
			xtable[0][0] == xtable[3][3] && xtable[0][0] == 'X') {
			status = 0;
			goto done;
		}

		if (otable[0][0] == otable[1][1] &&
			otable[0][0] == otable[2][2] &&
			otable[0][0] == otable[3][3] && otable[0][0] == 'O') {
			status = 1;
			goto done;
		}

		if (xtable[0][3] == xtable[1][2] &&
			xtable[0][3] == xtable[2][1] &&
			xtable[0][3] == xtable[3][0] && xtable[0][3] == 'X') {
			status = 0;
			goto done;
		}

		if (otable[0][3] == otable[1][2] &&
			otable[0][3] == otable[2][1] &&
			otable[0][3] == otable[3][0] && otable[0][3] == 'O') {
			status = 1;
			goto done;
		}

		count = 0;
		for (int i = 0 ;i < 4 ; ++i) {
			for (int j = 0 ; j < 4 ; ++j) {
				if (table[i][j] == '.') ++count;
			}
		}
		if (count == 0) status = 2;
		else status = 3;

		done:
		switch (status)
		{
		case 0: printf("Case #%d: X won\n", m+1); break;
		case 1: printf("Case #%d: O won\n", m+1); break;
		case 2: printf("Case #%d: Draw\n", m+1); break;
		default: printf("Case #%d: Game has not completed\n", m+1); break;
		}
	}

	return 0;
}