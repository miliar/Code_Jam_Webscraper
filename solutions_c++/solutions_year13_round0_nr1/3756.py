#include <stdio.h>

int main()
{
	int cases, currentCase = 0;
	scanf("%d", &cases);
	
	while (++currentCase <= cases) {
		char board[4][4];
		bool isFull = true;
		bool isEnd = false;
		int oh[4] = {0, }, ov[4] = {0, };
		int xh[4] = {0, }, xv[4] = {0, };


		for (int i = 0; i < 4; i++) {
			getchar();
			scanf("%c%c%c%c", &board[i][0], &board[i][1], &board[i][2], &board[i][3]);
		}
		getchar();
		
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				switch (board[i][j]) {
				case 'O':
					oh[i]++;
					ov[j]++;
					break;
				case 'X':
					xh[i]++;
					xv[j]++;
					break;
				case 'T':
					oh[i]++;
					ov[j]++;
					xh[i]++;
					xv[j]++;
					break;
				case '.':
					isFull = false;
					break;
				}
			}
		}

		for (int i = 0; i < 4; i++) {
			if (oh[i] >= 4 || ov[i] >= 4) {
				printf("Case #%d: O won\n", currentCase);
				isEnd = true;
				break;
			} else if (xh[i] >= 4 || xv[i] >= 4) {
				printf("Case #%d: X won\n", currentCase);
				isEnd = true;
				break;
			}
		}

		if (isEnd) continue;

		oh[0] = ov[0] = xv[0] = xh[0] = 0;
		for (int i = 0; i < 4; i++) {
			switch (board[i][i]) {
			case 'O':
				oh[0]++;
				break;
			case 'X':
				xh[0]++;
				break;
			case 'T':
				oh[0]++;
				xh[0]++;
				break;
			}

			switch (board[i][3 - i]) {
			case 'O':
				ov[0]++;
				break;
			case 'X':
				xv[0]++;
				break;
			case 'T':
				ov[0]++;
				xv[0]++;
				break;
			}
		}

		if (ov[0] >= 4 || oh[0] >= 4) {
			printf("Case #%d: O won\n", currentCase);
			continue;
		} else if (xh[0] >= 4 || xv[0] >= 4) {
			printf("Case #%d: X won\n", currentCase);
			continue;
		}

		if (isFull) {
			printf("Case #%d: Draw\n", currentCase);
		} else {
			printf("Case #%d: Game has not completed\n", currentCase);
		}
	}

	return 0;
}
