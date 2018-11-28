#include <cstdio>
#include <cstring>

const int MaxN = 101;
int map[MaxN][MaxN], mark[MaxN][MaxN], r, c, ans[MaxN][MaxN], cnt;
int dir[10][10] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int dfs(int a, int b)
{
	int i, dx, dy, min,x, y;
	if(mark[a][b] != -1)
		return mark[a][b];
	min = 0x7fffffff;
	for(i = 0; i < 4; i++)
	{
		dx = a + dir[i][0];
		dy = b + dir[i][1];
		if(dx >= 0 && dx < r && dy >= 0 && dy < c)
		{
			if(map[dx][dy] < map[a][b] && map[dx][dy] < min)
			{
				min = map[dx][dy];
				x = dx; y = dy;
			}
		}
	}
	if(min == 0x7fffffff)
	{
		cnt++;
		mark[a][b] = cnt;
		return cnt;
	}
	mark[a][b] = dfs(x, y);
	return mark[a][b];
}

void OK(int a, int b, int n)
{
	int dx, dy;
	ans[a][b] = n;
	for(int i = 0; i < 4; i++)
	{
		dx = a + dir[i][0];
		dy = b + dir[i][1];
		if(dx >= 0 && dx < r && dy >= 0 && dy < c)
		{
			if(mark[dx][dy] == mark[a][b] && ans[dx][dy] == -1)
			{
				ans[dx][dy] = n;
				OK(dx, dy, n);
			}
		}
	}
}

int main()
{
	int text, i, j, cs = 0;
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	scanf("%d",&text);
	while(text--)
	{
		scanf("%d %d", &r, &c);
		for(i = 0; i < r; i++)
			for(j = 0; j < c; j++)
				scanf("%d", &map[i][j]);
		memset(mark, -1, sizeof(mark));
		for(i = cnt = 0; i < r; i++)
		{
			for(j = 0; j < c; j++)
			{
				if(mark[i][j] == -1)
					int t = dfs(i, j);
			}
		}
		cnt = 0;
		memset(ans, -1, sizeof(ans));
		for(i = 0; i < r; i++)
		{
			for(j = 0; j < c; j++)
			{
				if(ans[i][j] == -1)
				{
					OK(i, j, cnt);
					cnt++;
				}
			}
		}
		printf("Case #%d:\n", ++cs);
		for(i = 0; i < r; i++)
			for(j = 0; j < c; j++)
				printf("%c%c", ans[i][j]+'a', (j == c-1)? '\n' : ' ');
	}
	return 0;
}