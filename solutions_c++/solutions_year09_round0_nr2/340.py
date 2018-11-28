#include <stdio.h>
#include <string.h>

int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

char basin[128][128];
int alt[128][128], H, W;

void set(int x, int y, char bas)
{
	int nx = -1, ny = -1, malt = -1;
	basin[x][y] = bas;
	for(int i = 0; i < 4; i++)
	{
		int xx = x+dir[i][0], yy = y+dir[i][1];
		if(xx >= 0 && xx < H && yy >= 0 && yy < W && alt[xx][yy] < alt[x][y] && (alt[xx][yy] < malt || malt == -1))
		{
			malt = alt[xx][yy];
			nx = xx; ny = yy;
		}
	}
	if(nx != -1) set(nx, ny, bas);
}

char detect(int x, int y)
{
	char c;
	int nx = -1, ny = -1, malt = -1;
	if(basin[x][y]) return basin[x][y];
	for(int i = 0; i < 4; i++)
	{
		int xx = x+dir[i][0], yy = y+dir[i][1];
		if(xx >= 0 && xx < H && yy >= 0 && yy < W && alt[xx][yy] < alt[x][y] && (alt[xx][yy] < malt || malt == -1))
		{
			malt = alt[xx][yy];
			nx = xx; ny = yy;
		}
	}
	if(nx != -1 && (c = detect(nx, ny)))
		return basin[x][y] = c;
	return 0;
}

int main()
{
	int t, nt;
	scanf("%d", &nt);
	for(t = 1; t <= nt; t++)
	{
		char bas = 'a';
		scanf("%d%d", &H, &W);
		memset(basin, 0, sizeof(basin));
		for(int i = 0; i < H; i++)
			for(int j = 0; j < W; j++)
				scanf("%d", &alt[i][j]);
		printf("Case #%d:\n", t);
		for(int i = 0; i < H; i++)
		{
			for(int j = 0; j < W; j++)
			{
				if(!basin[i][j] && !detect(i, j))
					set(i, j, bas++);
				printf("%s%c", (j == 0)?"": " ", basin[i][j]);
			}
			printf("\n");
		}
	}
}
