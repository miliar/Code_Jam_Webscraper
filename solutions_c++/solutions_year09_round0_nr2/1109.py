#include <iostream>
int H, W, gh[111][111];
char res[111][111];
char now;
char doit(int x, int y)
{
	if (res[x][y] != '*')
	{
		return res[x][y];
	}
	int nt = 0;
	int mn = gh[x][y];
	if (x - 1 >= 1 && gh[x - 1][y] < mn)
	{
		nt = 1;
		mn = gh[x - 1][y];
	}
	if (y - 1 >= 1 && gh[x][y - 1] < mn)
	{
		nt = 2;
		mn = gh[x][y - 1];
	}
	if (y + 1 <= W && gh[x][y + 1] < mn)
	{
		nt = 3;
		mn = gh[x][y + 1];
	}
	if (x + 1 <= H && gh[x + 1][y] < mn)
	{
		nt = 4;
		mn = gh[x + 1][y];
	}
	if (mn == gh[x][y])
	{
		res[x][y] = now;
		++now;
		return res[x][y];
	}
	switch (nt)
	{
	case 1:
		res[x][y] = doit(x - 1, y);
		break;
	case 2:
		res[x][y] = doit(x, y - 1);
		break;
	case 3:
		res[x][y] = doit(x, y + 1);
		break;
	case 4:
		res[x][y] = doit(x + 1, y);
		break;
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, tc = 1;
	int i, j;
	scanf("%d", &t);
	for ( ; tc <= t; ++tc)
	{
		scanf("%d %d", &H, &W);
		for (i = 1; i <= H; ++i)
		{
			for (j = 1; j <= W; ++j)
			{
				scanf("%d", &gh[i][j]);
			}
		}
		memset(res, '*', sizeof(res));
		now = 'a';
		for (i = 1; i <= H; ++i)
		{
			for (j = 1; j <= W; ++j)
			{
				doit(i, j);
			}
		}
		printf("Case #%d:\n", tc);
		for (i = 1; i <= H; ++i)
		{
			for (j = 1; j < W; ++j)
			{
				printf("%c ", res[i][j]);
			}
			printf("%c\n", res[i][j]);
		}
	}
	return 0;
}
