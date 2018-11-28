#include <iostream>           
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

int field[310][310];
int r;
int mx, my;

void Load()
{
	memset(field, 0, sizeof(field));
	scanf("%d", &r);
	int i, j, k;
	mx = my = 0;
	for (i = 0; i < r; i++)
	{
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (j = x1; j <= x2; j++)
		{
			for (k = y1; k <= y2; k++)
			{
				field[j][k] = 1;
			}
		}
		mx = max(mx, x2);
		my = max(my, y2);
	}
}

int nfield[310][310];

void Solve()
{
	int f = 1;
	int i, j;
	int ns = 0;
	while (f == 1)
	{
		f = 0;
		memcpy(nfield, field, sizeof(nfield));
		for (i = 1; i <= mx + 1; i++)
		{
			for (j = 1; j <= my + 1; j++)
			{
				if (field[i][j] == 0)
				{
					if (field[i - 1][j] == 1 && field[i][j - 1] == 1)
					{
						nfield[i][j] = 1;
						f = 1;
					}
				}
				else
				{
					if (field[i - 1][j] == 0 && field[i][j - 1] == 0)
					{
						nfield[i][j] = 0;
						f = 1;
					}
				}
			}
		}
		memcpy(field, nfield, sizeof(nfield));
		ns++;
	}
	cout << ns - 1;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}