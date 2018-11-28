#include <cstdio>

char grid[100][100];

bool replace(int i, int j)
{
	if (grid[i][j] == '#')
		grid[i][j] = '/';
	else
		return false;
	if (grid[i+1][j] == '#')
		grid[i+1][j] = '\\';
	else
		return false;
	if (grid[i][j+1] == '#')
		grid[i][j+1] = '\\';
	else
		return false;
	if (grid[i+1][j+1] == '#')
		grid[i+1][j+1] = '/';
	else
		return false;
	return true;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int T = 1; T <= cases; T++)
	{
		int R, C;
		scanf("%d %d", &R, &C);
		for (int i = 0; i < R; i++)
		{
			scanf("%s", grid[i]);
		}
		bool flag = true;
		for (int i = 0; i < R && flag; i++)
		{
			for (int j = 0; j < C && flag; j++)
			{
				if (grid[i][j] == '#')
					flag = replace(i, j);
			}
		}
		printf("Case #%d:\n", T);
		if (flag)
		{
			for (int i = 0; i < R; i++)
			{
				printf("%s\n", grid[i]);
			}
		}
		else
			printf("Impossible\n");
	}
	return 0;
}