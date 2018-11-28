#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>

#define SZ 105

int maze[SZ][SZ];
bool visited[SZ][SZ];
char basin[SZ][SZ];

int k;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

char findbasin(int x, int y)
{
	if(basin[x][y] != 'A')
		return(basin[x][y]);

	int mn, imn, i;
	mn = 100005;
	for(i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if(maze[nx][ny] < maze[x][y])
		{
			if(maze[nx][ny] < mn)
			{
				mn = maze[nx][ny];
				imn = i;
			}
		}
	}
	if(mn > 100000)
	{
		basin[x][y] = 'a' + k;
		k++;
		return(basin[x][y]);
	}
	basin[x][y] = findbasin(x + dx[imn], y + dy[imn]);
	return(basin[x][y]);
}

int main()
{
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);


	int inp, kase, i, j, h, w;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &h, &w);
		for(i = 0; i <= h+1; i++)
		{
			for(j = 0; j <= w+1; j++)
			{
				maze[i][j] = 100005;
			}
		}
		for(i = 1; i <= h; i++)
		{
			for(j = 1; j <= w; j++)
			{
				scanf("%d", &maze[i][j]);
			}
		}
		memset(visited, false, sizeof(visited));
		memset(basin, 'A', sizeof(basin));
		
		k = 0;
		for(i = 1; i <= h; i++)
		{
			for(j = 1; j <= w; j++)
			{
				if(basin[i][j] == 'A')
				{
					basin[i][j] = findbasin(i, j);
				}
			}
		}
		
		printf("Case #%d:\n",kase);
		for(i = 1; i <= h; i++)
		{
			for(j = 1; j <=w; j++)
			{
				printf("%c",basin[i][j]);
				if(j != w)
					printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}
