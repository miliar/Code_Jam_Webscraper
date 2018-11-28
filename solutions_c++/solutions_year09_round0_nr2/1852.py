#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int t,h,w;
char index;
int maps[110][110];
char db[110][110];
int dir[4][2] = {-1,0,0,-1,0,1,1,0};
void expand(int row, int col)
{
	int mini, minh;
	minh = 30000;
	for (int i = 0; i <= 3; ++i)
	{
		if (row + dir[i][0] >= 1 && row + dir[i][0] <= h && col + dir[i][1] >= 1 && col + dir[i][1] <= w && maps[row + dir[i][0]][col + dir[i][1]] < maps[row][col] && maps[row + dir[i][0]][col + dir[i][1]] < minh)
		{
			minh = maps[row + dir[i][0]][col + dir[i][1]];
			mini = i;
		}
	}
	if (minh == 30000)
	{
		if (db[row][col] == -1) db[row][col] = index;
		++index;
		return;
	}
	else
	{
		if (db[row + dir[mini][0]][col + dir[mini][1]] == -1)
			expand(row + dir[mini][0], col + dir[mini][1]);
		db[row][col] = db[row + dir[mini][0]][col + dir[mini][1]];
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		memset(db,-1 ,sizeof(db));
		scanf("%d%d",&h, &w);
		for (int j = 1; j <= h; ++j)
			for (int k = 1; k <= w; ++k)
				scanf("%d",&maps[j][k]);
		index = 'a';
		for (int j = 1; j <=h; ++j)
			for (int k = 1; k <= w; ++k)
				if (db[j][k] == -1)
				{
					expand(j,k);
				}
		printf("Case #%d:\n", i);
		for (int j = 1; j <=h; ++j)
		{
			for (int k = 1; k <=w; ++k)
			{
				if (k != w) printf("%c ",db[j][k]);
				else printf("%c\n",db[j][k]);
			}
			
		}

	}
	return 0;
}