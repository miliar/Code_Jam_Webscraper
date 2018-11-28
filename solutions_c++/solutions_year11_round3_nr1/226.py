#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int t, n, m;
char ar[60][60];

void init()
{
	for (int i = 0; i < 60; i++)
	{
		for (int j = 0; j < 60; j++)
		{
			ar[i][j] = '.';
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%d%d\n", &n, &m);
		init();
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				scanf("%c", &ar[i][j]);
			}
			scanf("\n");
		}
		bool good = true;
		for (int i = 0; i < n; i++)
		{
			if (!good)
			{
				break;
			}
			for (int j = 0; j < m; j++)
			{
				if (ar[i][j] == '#')
				{
					if (ar[i][j + 1] == '#' && ar[i + 1][j] == '#' && ar[i + 1][j + 1] == '#')
					{
						ar[i][j] = ar[i + 1][j + 1] = '/';
						ar[i + 1][j] = ar[i][j + 1] = '\\';
					}
					else
					{
						good = false;
						break;
					}
				}
			}
		}
		printf("Case #%d:\n", q + 1);
		if (!good)
		{
			printf("Impossible\n");
			continue;
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				printf("%c", ar[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}