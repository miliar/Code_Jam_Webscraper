#include <stdio.h>
#include <string.h>
#define N 60

char map[N][N];
char res[N][N];
int r, c;
bool find_map(int &x, int &y)
{
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
		{
			if (map[i][j] == '#' && !res[i][j])
			{
				x = i; 
				y = j;
				return true;
			}
		}
	return false;
}
bool in_map(int x, int y)
{
	if (x >= 0 && x < r && y >= 0 && y <c)
		return true;
	else return false;
}
bool test_map()
{
	int x, y;
	while (find_map(x,y))
	{
		if (in_map(x+1, y) && in_map(x, y+1) && in_map(x+1 , y+ 1))
		{
			if (map[x+1][y] == '#' && map[x][y+1] =='#' && map[x+1][y+1] == '#')
			{
				res[x][y] = res[x+1][y+1] = '/';
				res[x+1][y] = res[x][y+1] = '\\';
			}
			else return false;
		}
		else return false;
	}
	for (int i = 0; i < r; ++i)
		for (int j =0;j < c; ++j)
		{
			if (!res[i][j])
				res[i][j] ='.';
		}
	return true;
}
int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int cas = 1;
	while (t--)
	{

		scanf("%d%d", &r, &c);
		for (int i =0; i < r; ++i)
			scanf("%s", map[i]);

		printf("Case #%d:\n", cas++);
		memset(res, 0 , sizeof(res));
		bool can = test_map();
		if (can)
		{
			for (int i = 0; i < r; ++i)
				printf("%s\n", res[i]);
		}
		else printf("Impossible\n");		



		
	}
	return 0;
}