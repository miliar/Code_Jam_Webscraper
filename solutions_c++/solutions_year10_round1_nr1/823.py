#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

#define MAXN 60
char mp[MAXN][MAXN];
char mp1[MAXN][MAXN];

int n, k;
int dir[8][2] = {-1,0, -1,1, 0,1, 1,1, 1,0, 1,-1, 0,-1, -1,-1};

void pr(char m[][MAXN])
{
	int i, j;
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= n; j++)
		{
			printf ("%c", m[i][j]);
		}
		printf ("\n");
	}
	printf ("\n");
}

void rota()
{
	int i, j, r, c;
	c = 1;
	memset(mp1, '.', sizeof(mp1));
	for (i = n; i > 0; i--, c++)
	{
		r = n;
		for (j = n; j > 0; j--)
		{
			if (mp[i][j] == '.') continue;
			mp1[r--][c] = mp[i][j];
		}
	}
}

inline int in(int x, int y)
{
	return x > 0 && x <= n && y > 0 && y <= n;
}

int cal(char m[][MAXN])
{
	int i, j, d, l, x, y, f1 = 0, f2 = 0;
	char t;

	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= n; j++)
		{
			if (m[i][j] == '.') continue;
			t = m[i][j];
			//printf ("i %d j %d\n", i, j);
			for (d = 0; d < 8; d++)
			{
				x = i; y = j;
				for (l = 0; l < k; l++)
				{
					if (in(x, y) && m[x][y] == t)
					{
						x = x + dir[d][0];
						y = y + dir[d][1];
					}
					else break;
				}
				//printf ("l %d d %d\n", l, d);
				if (l >= k)
				{
					if (t == 'R') f1 = 1;
					else f2 = 1;
					//printf ("i %d j %d l %d k %d\n", i, j, l, k);
					break;
				}
				//system("pause");
			}
		}
		if (f1 && f2) break;
	}
	if (f1 && f2)
		printf ("Both\n");
	else if (f1)
		printf ("Red\n");
	else if (f2)
		printf ("Blue\n");
	else
		printf ("Neither\n");
}

int main()
{
	freopen("A-large.in", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int i, j, csnum, cs;
	scanf ("%d", &csnum);
	for (cs = 1; cs <= csnum; cs++)
	{
		scanf ("%d %d%*c", &n, &k);
		for (i = 1; i <= n; i++)
		{
			gets(&mp[i][1]);
		}

		rota();

		//printf ("\n\n");
		//pr(mp);

		//printf ("\n\n");
		//pr(mp1);
		printf ("Case #%d: ", cs);
		cal(mp1);

	}
}
/*
4
6 4
......
......
.R...R
.R..BB
.R.RBR
RB.BBB

*/
