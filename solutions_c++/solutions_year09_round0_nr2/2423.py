#include<stdio.h>
#include<string.h>
#include<memory.h>
#define MAXN 310
int T, m, n;
int g[MAXN][MAXN];
bool vst[MAXN][MAXN];
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
char idx;
char label[MAXN][MAXN];
char dfs(int x, int y)
{
	vst[x][y] = true;
	int xx, yy, i;
	int min, tx, ty;
	min = g[x][y];
	tx = x;
	ty = y;
	for(i = 0; i < 4; i++)
	{
		xx = x + dx[i];
		yy = y + dy[i];
		if(xx >= 0 && xx < n && yy >= 0 && yy < m && g[xx][yy] < min)
		{
			min = g[xx][yy];
			tx = xx;
			ty = yy;
		}
	}
	if(min == g[x][y])
	{
		label[x][y] = idx++;	
	}
	else if(vst[tx][ty])
	{
		label[x][y] = label[tx][ty];
	}
	else
	{
		label[x][y] = dfs(tx, ty);
	}
	return label[x][y];
}
int main()
{
	int i, j;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int tt = 1; tt <= T; tt++)
	{
		scanf("%d%d",&n,&m);
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < m; j++)
			{
				scanf("%d",&g[i][j]);
			}
		}
		memset(vst, false, sizeof(vst));
		memset(label, 0, sizeof(label));
		idx = 'a';
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < m; j++)
			{
				if(!vst[i][j])
				{
					dfs(i, j);
				}
			}
		}
		printf("Case #%d:\n",tt);
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < m - 1; j++)
			{
				printf("%c ",label[i][j]);
			}
			printf("%c\n",label[i][j]);
		}
	}
	return 0;
}
