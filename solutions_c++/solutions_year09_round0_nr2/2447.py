#include <iostream>
using namespace std;

struct cell 
{
	int x, y;
	int altitudes;
}clist[10001];
int cmp( const void *a ,const void *b) 
{
	return (*(cell *)a).altitudes > (*(cell *)b).altitudes ? -1 : 1;  
}

struct anscell
{
	char c;
	int prex, prey;
	int flag;
}ans[101][101];
int inmap[101][101];
int i, j;
int nc, index;
int m, n;
char cnoset;
char ca;

char dfs(int x, int y)
{
	if (ans[x][y].c != cnoset)
	{
		return ans[x][y].c;
	}
	if (ans[x][y].prex != -1)
	{
		ans[x][y].c = dfs(ans[x][y].prex, ans[x][y].prey);
		return ans[x][y].c;
	}
	return cnoset;
}

int main()
{
	freopen("e:\\bin.in", "r", stdin);
	freopen("e:\\bout.out", "w", stdout);
	index = 1;
	scanf("%d", &nc);
	while (nc--)
	{
		char ca = 'a';
		scanf("%d%d", &m, &n);
		for (i=0; i<m; i++)
		{
			for (j=0; j<n; j++)
			{
				scanf("%d", &inmap[i][j]);
				clist[i * n + j].altitudes = inmap[i][j];
				clist[i * n + j].x = i;
				clist[i * n + j].y = j;
			}
		}
		qsort(clist, m*n, sizeof(clist[0]), cmp);
		memset(ans, -1, sizeof(ans));
		cnoset = ans[0][0].c;
		for (i=0; i<m*n; i++)
		{
			int min = 99999999;
			int x = clist[i].x;
			int y = clist[i].y;
			if (x > 0 && clist[i].altitudes > inmap[x-1][y] && inmap[x-1][y] < min)
			{
				min = inmap[x-1][y];
				ans[x][y].prex = x-1;
				ans[x][y].prey = y;
			}
			if (y > 0 && clist[i].altitudes > inmap[x][y-1] && inmap[x][y-1] < min)
			{
				min = inmap[x][y-1];
				ans[x][y].prex = x;
				ans[x][y].prey = y-1;
			}
			if (y < n-1 && clist[i].altitudes > inmap[x][y+1] && inmap[x][y+1] < min)
			{
				min = inmap[x][y+1];
				ans[x][y].prex = x;
				ans[x][y].prey = y+1;
			}
			if (x < m-1 && clist[i].altitudes > inmap[x+1][y] && inmap[x+1][y] < min)
			{
				min = inmap[x+1][y];
				ans[x][y].prex = x+1;
				ans[x][y].prey = y;
			}
		}
		ans[0][0].c = 'a';
		for (i=0; i<m; i++)
		{
			for (j=0; j<n; j++)
			{
				if (ans[i][j].c == cnoset)
				{
					if (ans[i][j].prex != -1)
					{
						ans[i][j].c = dfs(ans[i][j].prex, ans[i][j].prey);
					}
					if (ans[i][j].c == cnoset)
					{
						ans[i][j].c = ++ca;
					}
				}
				if (ans[i][j].c != cnoset && ans[i][j].prex != -1)
				{
					char ct = ans[i][j].c;
					anscell * tmp = & ans[ans[i][j].prex][ans[i][j].prey];
					tmp->c = ct;
					while (tmp->prex != -1)
					{
						tmp = & ans[tmp->prex][tmp->prey];
						tmp->c = ct;
					}
				}
			}
		}
		printf("Case #%d:\n", index++);
		for (i=0; i<m; i++)
		{
			printf("%c", ans[i][0].c);
			for (j=1; j<n; j++)
			{
				printf(" %c", ans[i][j].c);
			}
			printf("\n");
		}
	}
}