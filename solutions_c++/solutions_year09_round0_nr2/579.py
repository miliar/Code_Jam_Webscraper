#include <cstdio>

int tests, h, w, a[100][100], bn[100][100], bn_cnt;
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

bool in(int i, int j)
{
	if (i >= 0 && i < h && j >= 0 && j < w)
		return true;
	return false;
}

int go(int i, int j)
{
	if (bn[i][j] != -1)
		return bn[i][j];

	int dir = -1, lastA = -1;
	for (int k = 0; k < 4; k++)
	{
		int ni = i + dx[k], nj = j + dy[k];
		if (in(ni, nj) && a[ni][nj] < a[i][j] && (dir == -1 || lastA > a[ni][nj]))
		{
			dir = k;
			lastA = a[ni][nj];
		}
	}
	
	if (dir == -1)
		return bn[i][j] = bn_cnt++;
	
	return bn[i][j] = go(i + dx[dir], j + dy[dir]);
}

int main()
{
	scanf("%d", &tests);
	for (int tn = 0; tn < tests; tn++)
	{
		scanf("%d %d", &h, &w);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
			{
				scanf("%d", &a[i][j]);
				bn[i][j] = -1;
			}
		
		bn_cnt = 0;
		
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				if (bn[i][j] == -1)
					go(i, j);
		
		printf("Case #%d:\n", tn + 1);
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
				printf("%c ", bn[i][j] + 'a');
			printf("\n");
		}
	}
	return 0;
}
	