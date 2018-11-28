#include <iostream>
#include <string.h>
#define MAXN 103
#define MAX(a, b) ((a) > (b) ? (a) : (b))
using namespace std;

int map[MAXN][MAXN];
int t, f, i, j, k, check, res;
int r, x1, y1, x2, y2;
int mx, my;

int main()
{
	freopen ("C-small.in", "r", stdin);
	freopen ("C-small.out", "w", stdout);
	cin>>t;
	for (f = 1; f <= t; f++)
	{
		cin>>r;
		mx = my = res = 0;
		memset (map, 0, sizeof map);
		for (k = 0; k < r; k++)
		{
			cin>>x1>>y1>>x2>>y2;
			mx = MAX(mx, x2);
			my = MAX(my, y2);
			for (j = x1; j <= x2; j++)
			{
				for (i = y1; i <= y2; i++)
				{
					map[i][j] = 1;
				}
			}
			
		}
		/*
		printf("%d %d\n", mx, my);
		for (i = 1; i <= my; i++)
		{
			for (j = 1; j <= mx; j++)
			{
				printf("%d ", map[i][j]);
			}
			printf("\n");
		}
		printf("\n");
		*/
		while (1)
		{
			check = 0;
			for (j = 1; j <= mx; j++)
			{
				for (i = 1; i <= my; i++)
				{
					if (map[i][j] == 0)
					{
						if (map[i][j - 1] == 1 && map[i - 1][j] == 1)
						{
							map[i][j] = 2;
						}
					}
				}
			}
			for (j = 1; j <= mx; j++)
			{
				for (i = 1; i <= my; i++)
				{
					if (map[i][j] == 1)
					{
						check = 1;
						if (map[i][j - 1] == 0 && map[i - 1][j] == 0)
						{
							map[i][j] = 3;
						}
					}
					else if (map[i][j] == 2)
					{
						check = 1;
						map[i][j] = 1;
					}
				}
			}
			for (j = 1; j <= mx; j++)
			{
				for (i = 1; i <= my; i++)
				{
					if (map[i][j] == 3)
					{
						map[i][j] = 0;
					}
				}
			}
			if (check == 0)
			{
				break;
			}
			res++;
			/*
			printf("%d\n", res);
			for (i = 1; i <= my; i++)
			{
				for (j = 1; j <= mx; j++)
				{
					printf("%d ", map[i][j]);
				}
				printf("\n");
			}
			printf("\n");
			*/
		}
		printf("Case #%d: %d\n", f, res);
	}
	return 0;
}