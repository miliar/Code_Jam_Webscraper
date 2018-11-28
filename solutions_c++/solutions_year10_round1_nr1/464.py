#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;
#define SZ 55

char maze[SZ][SZ];

void rotatec(int n)
{
	char temp[SZ][SZ];
	int i, j, ni, nj;
	for(i = 0, nj = 0; i < n; i++, nj++)
	{
		for(j = 0, ni = n - 1; j < n; j++, ni--)
		{
			temp[i][j] = maze[ni][nj];
		}
	}
	
	for(j = 0; j < n; j++)
	{
		ni = n - 1;
		for(i = n - 1; i >= 0; i--)
		{
			if(temp[i][j] != '.')
			{
				temp[ni][j] = temp[i][j];
				if(i != ni)
					temp[i][j] = '.';
				ni--;
			}
		}
	}
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < n; j++)
		{
			maze[i][j] = temp[i][j];
		}
	}
}

int main()
{
	//freopen("A-small-attempt0.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int inp, kase, i, j, k;
	int n;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &n, &k);
		for(i = 0; i < n; i++)
		{
			scanf("%s", maze[i]);
		}
		rotatec(n);
		int r, b, ni, nj;
		bool flgr, flgb;
		flgr = flgb = false;
		for(i = 0; i < n; i++)
		{
			r = b = 0;
			for(j = 0; j < n; j++)
			{
				if(maze[i][j] == 'R')
				{
					r++;
				}
				else
				{
					r = 0;
				}
				if(maze[i][j] == 'B')
				{
					b++;
				}
				else
				{
					b = 0;
				}
				if(r >= k)
				{
					flgr = true;
				}
				if(b >= k)
				{
					flgb = true;
				}
			}
			r = b = 0;
			for(j = 0; j < n; j++)
			{
				if(maze[j][i] == 'R')
				{
					r++;
				}
				else
				{
					r = 0;
				}
				if(maze[j][i] == 'B')
				{
					b++;
				}
				else
				{
					b = 0;
				}
				if(r >= k)
				{
					flgr = true;
				}
				if(b >= k)
				{
					flgb = true;
				}
			}
			r = b = 0;
			for(j = 0; j < n; j++)
			{
				ni = n - 1 - j;
				nj = i - j;
				if(ni < 0 || ni >= n|| nj < 0 || nj >= n)
					continue;
				if(maze[ni][nj] == 'R')
				{
					r++;
				}
				else
				{
					r = 0;
				}
				if(maze[ni][nj] == 'B')
				{
					b++;
				}
				else
				{
					b = 0;
				}
				if(r >= k)
				{
					flgr = true;
				}
				if(b >= k)
				{
					flgb = true;
				}
			}
			r = b = 0;
			for(j = 0; j < n; j++)
			{
				ni = n - 1 - j;
				nj = i + j;
				if(ni < 0 || ni >= n|| nj < 0 || nj >= n)
					continue;
				if(maze[ni][nj] == 'R')
				{
					r++;
				}
				else
				{
					r = 0;
				}
				if(maze[ni][nj] == 'B')
				{
					b++;
				}
				else
				{
					b = 0;
				}
				if(r >= k)
				{
					flgr = true;
				}
				if(b >= k)
				{
					flgb = true;
				}
			}
			r = b = 0;
			for(j = 0; j < n; j++)
			{
				ni = i - j;
				nj = 0 + j;
				if(ni < 0 || ni >= n|| nj < 0 || nj >= n)
					continue;
				if(maze[ni][nj] == 'R')
				{
					r++;
				}
				else
				{
					r = 0;
				}
				if(maze[ni][nj] == 'B')
				{
					b++;
				}
				else
				{
					b = 0;
				}
				if(r >= k)
				{
					flgr = true;
				}
				if(b >= k)
				{
					flgb = true;
				}
			}
			r = b = 0;
			for(j = 0; j < n; j++)
			{
				ni = i - j;
				nj = n - 1 - j;
				if(ni < 0 || ni >= n|| nj < 0 || nj >= n)
					continue;
				if(maze[ni][nj] == 'R')
				{
					r++;
				}
				else
				{
					r = 0;
				}
				if(maze[ni][nj] == 'B')
				{
					b++;
				}
				else
				{
					b = 0;
				}
				if(r >= k)
				{
					flgr = true;
				}
				if(b >= k)
				{
					flgb = true;
				}
			}
		}

		printf("Case #%d: ", kase);

		if(flgr == false && flgb == false)
		{
			printf("Neither\n");
			continue;
		}
		if(flgr == true && flgb == true)
		{
			printf("Both\n");
			continue;
		}
		if(flgr == true)
		{
			printf("Red\n");
			continue;
		}
		if(flgb == true)
		{
			printf("Blue\n");
		}

	}
	
	return 0;

}
