// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>

int pos[2][1000];
char type[1000];
int size0, size1;
int t, n;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		scanf("%d", &n);
		size1 = 0;
		size0 = 0;
		for (int j = 0; j < n; j++)
		{
			char t;
			scanf(" %c ", &t);
			
			if (t == 'O')
			{
				type[j] = 0;
				scanf("%d", &(pos[0][size0++]));
			}
			else
			{
				type[j] = 1;
				scanf("%d", &(pos[1][size1++]));
			}
		}

		int p = 0;
		int d0 = 0;
		int d1 = 0;
		int p0 = 1;
		int p1 = 1;
		int time = 0;
		bool move0, move1;
		while (true)
		{
			move0 = true;
			move1 = true;

			if (type[p] == 0 && p0 == pos[0][d0])
			{
				p++;
				d0++;
				move0 = false;
			}
			else if (type[p] == 1 && p1 == pos[1][d1])
			{
				p++;
				d1++;
				move1 = false;
			}

			time++;

			if (p == n) break;

			if (move0)
			{
				if (p0 < pos[0][d0])
					p0++;
				else if (p0 > pos[0][d0])
					p0--;
			}

			if (move1)
			{
				if (p1 < pos[1][d1])
					p1++;
				else if (p1 > pos[1][d1])
					p1--;
			}
		}

		printf("Case #%d: %d\n", i + 1, time);
	}

	return 0;
}