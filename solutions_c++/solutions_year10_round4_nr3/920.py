#include <stdio.h>

#define MAX 110
int table[2][MAX][MAX];

int main()
{
	int C;
	scanf("%d", &C);
	for (int cases = 1; cases <=C; cases++) {
		int R;
		for (int i = 0; i<MAX; i++)
			for (int j = 0; j<MAX; j++)
				for (int k = 0; k<2; k++)
					table[k][i][j] = 0;
		scanf("%d", &R);
		int x1, x2, y1, y2;
		int cell = 0;
		int minx = 1000, miny = 1000, maxx = 0, maxy = 0;
		int flag = 0;
		for (int i = 0; i<R; i++) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			if (minx > x1)	minx = x1;
			if (maxx < x2)	maxx = x2;
			if (miny > y1)	miny = y1;
			if (maxy < y2)	maxy = y2;
			for (int x = x1; x<=x2; x++)
				for (int y = y1; y<=y2; y++)
					if (table[flag][x][y] == 0) {
						table[flag][x][y] = 1;
						cell++;
					}
		}
		int day = 0;
		while (cell >0) {
			for (int x = minx; x<=maxx; x++)
				for (int y = miny; y<=maxy; y++)
					if (table[flag][x][y] == 1) {
						if (table[flag][x-1][y] ==0 && table[flag][x][y-1] == 0){
							cell--;
							table[1-flag][x][y] = 0;
						}
						else
							table[1-flag][x][y] = 1;
					}
					else {
						if (table[flag][x-1][y] == 1 && table[flag][x][y-1] == 1) {
							table[1-flag][x][y] = 1;
							cell++;
						}
						else
							table[1-flag][x][y] = 0;
					}
			flag = 1-flag;
			day++;
		}
		printf("Case #%d: %d\n", cases, day);
	}
	return 0;
}
