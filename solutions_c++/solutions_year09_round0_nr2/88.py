#include <stdio.h>
#include <string.h>
int map[100][100];
int color[100][100];
char output[26];
int w, h;
int totalcolor;
void DFS(int r, int c)
{
	if (color[r][c] != -1) return;
	int nextr = -1, nextc = -1, min = map[r][c];
	if (r - 1 >= 0 && map[r - 1][c] < min) {
		nextr = r - 1;
		nextc = c;
		min = map[r - 1][c];
	}
	if (c - 1 >= 0 && map[r][c - 1] < min) {
		nextr = r;
		nextc = c - 1;
		min = map[r][c - 1];
	}
	if (c + 1 < w && map[r][c + 1] < min) {
		nextr = r;
		nextc = c + 1;
		min = map[r][c + 1];
	}
	if (r + 1 < h && map[r + 1][c] < min) {
		nextr = r + 1;
		nextc = c;
		min = map[r + 1][c];
	}
	if (nextr == -1 && nextc == -1) {
		color[r][c] = totalcolor++;
	} else {
		DFS(nextr, nextc);
		color[r][c] = color[nextr][nextc];
	}
}
int main()
{
	int n;
	scanf("%d", &n);
	for (int cases = 1; cases <= n; cases++)
	{
		scanf("%d %d", &h, &w);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &map[i][j]);
				color[i][j] = -1;
			}
		totalcolor = 0;
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (color[i][j] == -1) DFS(i, j);
		for (int i = 0; i < 26; i++) output[i] = ' ';
		char seq = 'a';
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (output[color[i][j]] == ' ') output[color[i][j]] = seq++;
		printf("Case #%d:\n", cases);
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (j) putchar(' ');
				printf("%c", output[color[i][j]]);
			}
			puts("");
		}
	}
}