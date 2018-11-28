// cj3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define T 128

int map[T][T];

int main(int argc, char* argv[])
{
	int n;
	scanf("%d", &n);
	for (int nn = 1; nn <= n; nn++)
	{
		memset(map, 0, sizeof(map));
		int r;
		scanf("%d", &r);
		for (int i = 0; i < r; i++)
		{
			int a, b, c, d;
			scanf("%d %d %d %d", &a, &b, &c, &d);
			for (int x = a; x <= c; x++)
			{
				for (int y = b; y <= d; y++)
				{
					map[y][x] = 1;
				}
			}
		}

		//sim
		int res = 0;
		while(1)
		{
			//check
			if (memchr(map, 1, sizeof(map)) == NULL)
				break;

			//run
			res++;
			for (int y = T-1; y >= 0; y--)
			{
				for (int x = T-1; x >= 0; x--)
				{
					if (map[y][x])
					{
						if ((y > 0 && map[y-1][x]) ||
							(x > 0 && map[y][x-1]))
						{
							//keep
						}
						else
						{
							//die
							map[y][x] = 0;
						}
					}
					else
					{
						if ((y > 0 && map[y-1][x]) &&
							(x > 0 && map[y][x-1]))
						{
							//live
							map[y][x] = 1;
						}
						else
						{
							//keep
						}
					}
				}
			}
		}

		//prin6t
		printf("Case #%d: %d\n", nn, res);
	}
	system("pause");
	return 0;
}

