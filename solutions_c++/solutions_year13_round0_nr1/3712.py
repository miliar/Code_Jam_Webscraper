#include <stdio.h>
#include <string.h>

int main() {
	int T;
	scanf("%d", &T);
	getchar();
	int temp = T;
	while (T--) {
		int i, j;
		char a[4][4];
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++)
				scanf("%c", &a[i][j]);
			getchar();
		}
		int count1 = 0, count2 = 0;
		//for O
		for (i = 0; i < 4; i++) {
			if ((a[i][0] == 'O' || a[i][0] == 'T')
					&& (a[i][1] == 'O' || a[i][1] == 'T')
					&& (a[i][2] == 'O' || a[i][2] == 'T')
					&& (a[i][3] == 'O' || a[i][3] == 'T'))
				count1 = 1;
			if ((a[0][i] == 'O' || a[0][i] == 'T')
					&& (a[1][i] == 'O' || a[1][i] == 'T')
					&& (a[2][i] == 'O' || a[2][i] == 'T')
					&& (a[3][i] == 'O' || a[3][i] == 'T'))
				count1 = 1;
		}
		if ((a[0][0] == 'O' || a[0][0] == 'T')
				&& (a[1][1] == 'O' || a[1][1] == 'T')
				&& (a[2][2] == 'O' || a[2][2] == 'T')
				&& (a[3][3] == 'O' || a[3][3] == 'T'))
			count1 = 1;
		if ((a[0][3] == 'O' || a[0][3] == 'T')
				&& (a[1][2] == 'O' || a[1][2] == 'T')
				&& (a[2][1] == 'O' || a[2][1] == 'T')
				&& (a[3][0] == 'O' || a[3][0] == 'T'))
			count1 = 1;
		//for X
		for (i = 0; i < 4; i++) {
			if ((a[i][0] == 'X' || a[i][0] == 'T')
					&& (a[i][1] == 'X' || a[i][1] == 'T')
					&& (a[i][2] == 'X' || a[i][2] == 'T')
					&& (a[i][3] == 'X' || a[i][3] == 'T'))
				count2 = 1;
			if ((a[0][i] == 'X' || a[0][i] == 'T')
					&& (a[1][i] == 'X' || a[1][i] == 'T')
					&& (a[2][i] == 'X' || a[2][i] == 'T')
					&& (a[3][i] == 'X' || a[3][i] == 'T'))
				count2 = 1;
		}
		if ((a[0][0] == 'X' || a[0][0] == 'T')
				&& (a[1][1] == 'X' || a[1][1] == 'T')
				&& (a[2][2] == 'X' || a[2][2] == 'T')
				&& (a[3][3] == 'X' || a[3][3] == 'T'))
			count2 = 1;
		if ((a[0][3] == 'X' || a[0][3] == 'T')
				&& (a[1][2] == 'X' || a[1][2] == 'T')
				&& (a[2][1] == 'X' || a[2][1] == 'T')
				&& (a[3][0] == 'X' || a[3][0] == 'T'))
			count2 = 1;
		//judge
		if (count1 == 1 && count2 == 0)
			printf("Case #%d: O won\n", temp - T);
		if (count2 == 1 && count1 == 0)
			printf("Case #%d: X won\n", temp - T);
		if (count1 == count2) {
			int count = 0;
			for (i = 0; i < 4; i++)
				for (j = 0; j < 4; j++)
					if (a[i][j] == '.')
						count++;
			if (count != 0 && count1 == 0)
				printf("Case #%d: Game has not completed\n", temp - T);
			if (count == 0)
				printf("Case #%d: Draw\n", temp - T);
		}
		if (T != 0)
			getchar();
	}
	return 0;
}
