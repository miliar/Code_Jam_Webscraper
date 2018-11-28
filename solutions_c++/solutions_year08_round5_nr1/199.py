#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iostream>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))
#define DBG(a) cerr << a << endl;
#define DEBUG 1

#define MAXN 256
#define MAXX 1024

int tc, n;

int tab[MAXN][MAXN]; // 1 = 
char walk[MAXX][32];
int rep[MAXX];
int x, y, d;
int mx, my;
int filly[MAXN][MAXN];
int mark[MAXN][MAXN];

void move(char m, int mark)
{
	if (m == 'L') d = (d + 3) % 4;
	else if (m == 'R') d = (d + 1) % 4;
	else 
	{
			if (d == 0) // up, y +
			{
				if (mark) { tab[x-1][y] += 4; tab[x][y] += 1; }
				(y)++;
			}
			else if (d == 1) // right, x +
			{
				if (mark) { tab[x][y] += 2; tab[x][y - 1] += 8; }
				(x)++;
			}
			else if (d == 2) // down, y -
			{
				(y)--;
				if (mark) { tab[x-1][y] += 4; tab[x][y] += 1; }
			}
			else if (d == 3) // right, x +
			{
				(x)--;
				if (mark) { tab[x][y] += 2; tab[x][y - 1] += 8; }
			}
	}
	if (!mark) 
	{
		if (x < mx) mx = x;
		if (y < my) my = y;
	}
}

int inside(int x, int y) { return x >= 0 && x < MAXN && y >= 0 && y < MAXN; }

int can(int x1, int y1, int x2, int y2)
{
	if (x2 == 1) // right
	{
		if ((tab[x1][y1] & 4) == 0) // no wall
			return 1;
	}
	if (x2 == -1) // left
	{
		if ((tab[x1][y1] & 1) == 0) // no wall
			return 1;
	}
	if (y2 == 1) { if ((tab[x1][y1] & 8) == 0) return 1; }
	if (y2 == -1) { if ((tab[x1][y1] & 2) == 0) return 1; }
	return 0;
}

int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

void dfs(int xx, int yy, int color)
{
	int i;
	queue<pair<int, int> > q;
	q.push(make_pair(xx, yy));
	filly[xx][yy] = color;
	
	while (!q.empty())
	{
		pair<int, int > abc = q.front(); q.pop();
		xx = abc.first; yy = abc.second;
//		printf("%d %d\n", xx, yy);
		FOR(i, 4)
			if (inside(xx + dx[i], yy + dy[i]) && can(xx, yy, dx[i], dy[i])	&& !filly[xx + dx[i]][yy + dy[i]])
			{
				filly[xx + dx[i]][yy + dy[i]] = color;
				q.push(make_pair(xx + dx[i], yy + dy[i]));
			}
	}
}

int main()
{
	int i,j,k,t;

	scanf("%d", &tc);
	FOR(t, tc)
	{
		scanf("%d", &n);
		ZERO(tab);
		ZERO(walk);

		x = y = 0; d = 0; // up
		mx = 0; my = 0;
		
		FOR(i, n) 
		{ 
			scanf("%s %d", walk[i], &rep[i]); 
			FOR(j, rep[i]) 
			{
				FOR(k, strlen(walk[i]))
				{
					move(walk[i][k], 0);
				}
			}
		}

		x = -mx + 1; y = -my + 1; d = 0;
		FOR(i, n) FOR(j, rep[i]) FOR(k, strlen(walk[i])) 
		{
			move(walk[i][k], 1);
//			printf("-- [%d, %d] %d\n", x, y, d);
		}
/*		FOR(i, 10) 
		{
			FOR(j, 10) printf("%4d", tab[9-i][j]);
			printf("\n");
		}*/
//		printf("--------------\n");	

		ZERO(filly);
		dfs(0, 0, 1);
		FOR(i, MAXN) FOR(j, MAXN) if (!filly[i][j]) { dfs(i, j, 2); goto done; }
done:
	
//		FOR(i, 10) { FOR(j, 10) printf("%4d", filly[i][j]); printf("\n"); } 
		
		ZERO(mark);
		int s = -1, e, see = 0;
		// per row
		FOR(i, MAXN) 
		{
			s = -1;
			FOR(j, MAXN)
			{
				if (filly[i][j] == 2) 
				{ 
					if (s != -1) 
						FORI(k, s, j - 1) mark[i][k] = 1;
					see = 1; 
					s = -1;
				}
				if (filly[i][j] == 1 && see) 
				{
					s = j;
					see = 0;
				}
			}
		}
		
		// per col
		FOR(i, MAXN) 
		{
			s = -1;
			FOR(j, MAXN)
			{
				if (filly[j][i] == 2) 
				{ 
					if (s != -1) 
						FORI(k, s, j - 1) mark[k][i] = 1;
					see = 1; 
					s = -1;
				}
				if (filly[j][i] == 1 && see) 
				{
					s = j;
					see = 0;
				}
			}
		}

		int ans = 0;
		FOR(i, MAXN) FOR(j, MAXN) if (mark[i][j]) ans++;
//		printf("");
		printf("Case #%d: ", t+1);
		printf("%d\n", ans);
	}
	return 0;
}

