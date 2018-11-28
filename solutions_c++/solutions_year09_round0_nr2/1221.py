#include <stdio.h>
#include <string.h>

#define maxn 110

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

int map[maxn][maxn];
char color[maxn][maxn];
int dir[maxn][maxn];
int n,m;
int t;
char curColor;

void fill(int i, int j, char c)
{
	if (color[i][j] != -1)
	{
		return;
	}
	color[i][j] = c;

	int k;

	for (k = 0; k < 4; ++k)
	{
		int nx = i + dx[k];
		int ny = j + dy[k];

		if (nx >=0 && nx < n && ny >=0 && ny < m)
		{
			if (k == dir[i][j])
			{
				fill(nx,ny,c);
			}
			int kk = dir[nx][ny];
			
			if (kk >=0)
			{
				if (nx + dx[kk] == i && ny + dy[kk] == j)
				{
					fill(nx,ny,c);
				}
			}
		}
	}
}


void fillcolor(int i, int j)
{
	if (color[i][j] == -1)
	{
		fill(i,j,curColor);
		curColor++;
	}
}

main() {
	int i,j,k;

	freopen("B-large.in","r",stdin);
	freopen("tmp.out","w",stdout);

	int totalcase, nowcase;
	scanf("%d",&totalcase);

	for (nowcase = 0; nowcase < totalcase; nowcase++)
	{
		scanf("%d%d",&n,&m);
		for (i = 0; i < n; ++i)
		{
			for (j = 0; j < m; ++j)
			{
				scanf("%d",&map[i][j]);
			}
		}

		memset(color, 0xff, sizeof(color));
		for (i = 0; i < n; ++i)
			for (j = 0; j < m; ++j)
			{
				int lowest = map[i][j];
				int lk = -1;
				for (k = 0; k < 4; ++k)
				{
					int nx = i + dx[k];
					int ny = j + dy[k];

					if (nx >=0 && nx < n && ny >=0 && ny < m)
					{
						if (map[nx][ny] < lowest)
						{
							lk = k;
							lowest = map[nx][ny];
						}
					}
				}
				dir[i][j] = lk;
			}

		curColor = 'a';
		for (i = 0; i < n; ++i)
			for (j = 0; j < m; ++j)
				fillcolor(i,j);

		printf("Case #%d:\n", nowcase+1);
		for (i = 0; i < n; ++i)
		{
			putchar(color[i][0]);
			for (j = 1; j < m; ++j)
			{
				putchar(' ');
				putchar(color[i][j]);
			}
			putchar('\n');
		}
	}
	return 0;
}