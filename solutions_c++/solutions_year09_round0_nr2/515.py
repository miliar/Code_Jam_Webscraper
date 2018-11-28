#include <cstdio>

int field[110][110];
int height[110][110];
int found[30];
int sinkcount;

int dir[5][2] = {{0,0},{-1,0},{0,-1},{0,1},{1,0}};

void dfs(int i, int j)
{
	if(field[i][j] != -1)return;
	int dd = 0;
	for(int d = 1; d <= 4; d++)
	{
		if(field[i+dir[d][0]][j+dir[d][1]] != -2
		&& height[i+dir[d][0]][j+dir[d][1]] < height[i][j])
		{
			dfs(i+dir[d][0], j+dir[d][1]);
			if(height[i+dir[d][0]][j+dir[d][1]] < height[i+dir[dd][0]][j+dir[dd][1]])
				dd = d;
		}
	}
	if(dd == 0)
	{
		field[i][j] = sinkcount++;
	}
	else
	{
		field[i][j] = field[i+dir[dd][0]][j+dir[dd][1]];
	}
	//printf(":%d %d %d %d\n", i, j, dd, field[i][j]);
}

int main()
{
	int testIndex, testCount;
	scanf("%d", &testCount);
	for(testIndex = 1; testIndex <= testCount; testIndex++)
	{
		int h, w;
		scanf("%d %d", &h, &w);
		int i, j;
		for(i = 1; i <= h; i++)
			field[i][0] = field[i][w+1] = -2;
		for(j = 1; j <= w; j++)
			field[0][j] = field[h+1][j] = -2;

		for(i = 1; i <= h; i++)
			for(j = 1; j <= w; j++)
			{
				scanf("%d", &height[i][j]);
				field[i][j] = -1;
			}

		sinkcount = 0;
		for(i = 1; i <= h; i++)
			for(j = 1; j <= w; j++)
			{
				dfs(i, j);
			}


		printf("Case #%d:\n", testIndex);
		//for(i = 1; i <= h; i++) { for(j = 1; j <= w; j++) { printf("%d ", field[i][j]); } printf("\n"); }
		int lexcount = 0;
		for(i = 0; i < 30; i++)
			found[i] = -1;
		for(i = 1; i <= h; i++)
		{
			for(j = 1; j <= w; j++)
			{
				if(found[field[i][j]] == -1)
					found[field[i][j]] = lexcount++;

				printf("%c ", 'a' + found[field[i][j]]);
			}
			printf("\n");
		}
	}
	return 0;
}