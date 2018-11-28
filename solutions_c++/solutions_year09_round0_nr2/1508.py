#include <cstdio>

const int MAX_SIZE = 110;
const int MAX_HEIGHT = 100000;
const int DC[] = {0, -1, 1, 0};
const int DR[] = {-1, 0, 0, 1};

int alt[MAX_SIZE][MAX_SIZE];
char flow[MAX_SIZE][MAX_SIZE][4];
char res[MAX_SIZE][MAX_SIZE];

bool DFS(int x, int y, int x_max, int y_max, char lett)
{
	if (res[x][y])
		return false;
	if ((x < 1) || (y < 1) || (x > x_max) || (y > y_max))
		return false;
	res[x][y] = lett;
	for (int i = 0; i < 4; i++)
	{
		if (flow[x][y][i])
			DFS(x + DR[i], y + DC[i], x_max, y_max, lett);
	}
	return true;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	for (int case_num = 0; case_num < t; case_num++)
	{
		for (int i = 0; i < MAX_SIZE; i++)
			for (int j = 0; j < MAX_SIZE; j++)
			{
				alt[i][j] = MAX_HEIGHT;
				res[i][j] = 0;
				for (int k = 0; k < 4; k++)
					flow[i][j][k] = 0;
			}
		
		int h, w;
		scanf("%d%d", &h, &w);
		
		for (int i = 1; i <= h; i++)
			for (int j = 1; j <= w; j++)
			{
				scanf("%d", &(alt[i][j]));
			}
		
		for (int i = 1; i <= h; i++)
			for (int j = 1; j <= w; j++)
			{
				int min = alt[i][j];
				int n_min = -1;
				for (int k = 0; k < 4; k++)
				{
					if (alt[i + DR[k]][j + DC[k]] < min)
					{
						min = alt[i + DR[k]][j + DC[k]];
						n_min = k;
					}
				}
				if (n_min >= 0)
				{
					flow[i][j][n_min] = 1;
					flow[i + DR[n_min]][j + DC[n_min]][3 - n_min] = 1;
				}
			}
		
		char lett = 'a';
		for (int i = 1; i <= h; i++)
			for (int j = 1; j <= w; j++)
			{
				if (DFS(i, j, h, w, lett))
					lett++;
			}
		
		printf("Case #%d:\n", case_num + 1);
		for (int i = 1; i <= h; i++)
		{
			for (int j = 1; j <= w; j++)
			{
				printf("%c ", res[i][j]);
			}
			printf("\n");
		}
	}
	
	return 0;
}