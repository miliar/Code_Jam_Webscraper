#include <cstdio>
#include <cstring>

using namespace std;

//#define SMALL
#define LARGE

int t, lb, ru, row[5], col[5], Case = 1;
char board[5][5];
bool x_win, o_win, empty;

void check(const int& num) {
	if (num == 40 || num == 35)
		x_win = true;
	if (num == 4 || num == 8)
		o_win = true;
}

int main()
{
#ifdef SMALL
	freopen("A_small.in", "r", stdin);
	freopen("A_small.out", "w", stdout);
#endif

#ifdef LARGE
	freopen("A_large.in", "r", stdin);
	freopen("A_large.out", "w", stdout);
#endif

	scanf("%d", &t);
	while (t--) {
		getchar();
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));
		lb = ru = 0;
		x_win = o_win = empty = false;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%c", &board[i][j]);
				if (board[i][j] == '.') {
					if (i == j)
						lb = -500;
					if (i + j == 3)
						ru = -500;
					row[i] = -500;
					col[j] = -500;
					empty = true;
				} else if (board[i][j] == 'X') {
					if (i == j)
						lb += 10;
					if (i + j == 3)
						ru += 10;
					row[i] += 10;
					col[j] += 10;
				} else if (board[i][j] == 'O') {
					if (i == j)
						lb += 1;
					if (i + j == 3)
						ru += 1;
					row[i] += 1;
					col[j] += 1;
				} else {
					if (i == j)
						lb += 5;
					if (i + j == 3)
						ru += 5;
					row[i] += 5;
					col[j] += 5;
				}
			}
			getchar();
		}
		check(lb);
		check(ru);
		for (int i = 0; i < 4; ++i)
			check(row[i]), check(col[i]);
		printf("Case #%d: ", Case++);
		if (x_win)
			printf("X won\n");
		else if (o_win)
			printf("O won\n");
		else if (!empty)
			printf("Draw\n");
    else
			printf("Game has not completed\n");
	}
	return 0;
}
