#include <stdio.h>

#define H 102
#define W 102

int table[H][W];
int map[H][W];
char ans[H][W];

int N = 1;
int wW = 2;
int E = 3;
int S = 4;
int dh[5] = {0, -1, 0, 0, 1};
int dw[5] = {0, 0, -1, 1, 0};

void go(int h, int w, int idx)
{
	map[h][w] = idx;
	if (map[h-1][w] == S)
		go(h-1, w, idx);
	if (map[h][w-1] == E)
		go(h, w-1, idx);
	if (map[h][w+1] == wW)
		go(h, w+1, idx);
	if (map[h+1][w] == N)
		go(h+1, w, idx);
}

void fill(int h, int w, char c) 
{
	int cur;
	cur = map[h][w];
	map[h][w] = -1;
	ans[h][w] = c;
	for (int k = 1; k<=4; k++) {
		if (map[h+dh[k]][w+dw[k]] == cur)
			fill(h+dh[k], w+dw[k], c);
	}
}

int main()
{
	int T, h, w;
	scanf("%d", &T);
	for (int iter = 1; iter <= T; iter ++) {
		scanf("%d%d", &h, &w);
		for (int i = 1; i<=h; i++) {
			table[i][0] = 99999;
			table[i][w+1] = 99999;
		}
		for (int i = 1; i<=w; i++) {
			table[0][i] = 99999;
			table[h+1][i] = 99999;
		}

		for (int i = 1; i<=h; i++)
			for (int j = 1; j<=w; j++)
				scanf("%d", &table[i][j]);
		
		for (int i = 0; i<=h+1; i++)
			for (int j = 0; j<=w+1; j++)
				map[i][j] = 0;

		for (int i = 1; i<=h; i++) {
			for (int j = 1; j<=w; j++) {
				int min = table[i][j];
				int dir = 0;
				for (int k = 1; k<=4; k++) {
					if (table[i+dh[k]][j+dw[k]]<min) {
						min = table[i+dh[k]][j+dw[k]];
						dir = k;
					}
				}
				map[i][j] = dir;
//				printf("%d ", map[i][j]);
			}
//			printf("\n");
		}
		int counter = 10;
		for (int i = 1; i<=h; i++) {
			for (int j = 1; j<=w; j++) {
				if (map[i][j] == 0) {
					go(i, j, counter++);
				}
			}
		}
//		printf("basins\n");
//		for (int i = 1; i<=h; i++) {
//			for (int j = 1; j<=w; j++) {
//				printf("%d ", map[i][j]);
//			}
//			printf("\n");
//		}
		char current = 'a';
		for (int i = 1; i<=h; i++) {
			for (int j = 1; j<=w; j++) {
				if (map[i][j] > 0) {
					fill(i, j, current++);
				}
			}
		}

		printf("Case #%d:\n", iter);
		for (int i = 1; i<=h; i++) {
			for (int j = 1; j<=w; j++) {
				if (j>1)	printf(" ");
				printf("%c", ans[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
