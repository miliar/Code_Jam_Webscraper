#include <cstdio>
#include <cstring>

int level[100][100];
char label[100][100], ch;
int h, w;

int findMin(int r, int c) {
	int min = level[r][c];
	
	if (r > 0 && level[r - 1][c] < min)
		min = level[r - 1][c];
	if (c > 0 && level[r][c - 1] < min)
		min = level[r][c - 1];
	if (c < w - 1 && level[r][c + 1] < min)
		min = level[r][c + 1];
	if (r < h - 1 && level[r + 1][c] < min)
		min = level[r + 1][c];
	
	if (min == level[r][c])
		min = -1;
	
	return min;
}

char dfs(int r, int c) {
	if (label[r][c] != 0)
		return label[r][c];
	
	int min = findMin(r, c);
	
	if (r > 0 && level[r - 1][c] == min)
		return (label[r][c] = dfs(r - 1, c));
	if (c > 0 && level[r][c - 1] == min)
		return (label[r][c] = dfs(r, c - 1));
	if (c < w - 1 && level[r][c + 1] == min)
		return (label[r][c] = dfs(r, c + 1));	
	if (r < h - 1 && level[r + 1][c] == min)
		return (label[r][c] = dfs(r + 1, c));

	return (label[r][c] = ch++);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		memset(label, 0, sizeof(label));
		ch = 'a';
		scanf("%d %d", &h, &w);

		for (int r = 0; r < h; r++)
			for (int c = 0; c < w; c++)
				scanf("%d", &level[r][c]);
		
		for (int r = 0; r < h; r++)
			for (int c = 0; c < w; c++)
				dfs(r, c);
		
		printf("Case #%d:\n", i);
		for (int r = 0; r < h; r++) {
			printf("%c", label[r][0]);
			for (int c = 1; c < w; c++)
				printf(" %c", label[r][c]);
			printf("\n");
		}

	}
	return 0;
}

