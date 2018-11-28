#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

// 0: D, 1: R
int n, m;
char a[15][15];

int table[15][15][2];

struct state
{
	int x, y, dir;
	int dpt;

	state(int _x = 0, int _y = 0, int _d = 0, int k = 0) : x(_x), y(_y), dir(_d), dpt(k) {}
	inline bool operator < (const state &a) const
	{
		if (dpt == a.dpt)
		{
			if (x == a.x)
			{
				if (y == a.y)
				{
					return dir < a.dir;
				}
				return y < a.y;
			}
			return x < a.x;
		}
		return dpt < a.dpt;
	}

	bool operator == (const state &a) const
	{
		return (x == a.x) && (y == a.y) && (dir == a.dir);
	}
};

queue< state > Q;

bool check(int x, int y)
{
	if (x < 0 || x >= n || y < 0 || y >= m) return false;
	return (a[x][y] == '.');
}

void update( int x, int y, int d, int k)
{
	if (table[x][y][d] == -1)
	{
		table[x][y][d] = k;
		Q.push( state( x, y, d, k ) );
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn)
	{
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				scanf(" %c", &a[i][j]);
			}
		
		state start;
		state end;

		start.x = -1; start.dpt = 0; start.dir = 2;
		end.x = -1; end.dir = 2;

		printf("Case #%d: ", cn);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if ((a[i][j] == 'o' || a[i][j] == 'w') && start.x == -1)
				{
					start.x = i;
					start.y = j;
					if (a[i][j + 1] == 'o' || a[i][j + 1] == 'w') start.dir = 1;
					if (a[i + 1][j] == 'o' || a[i + 1][j] == 'w') start.dir = 0;
				}
				if ((a[i][j] == 'x' || a[i][j] == 'w') && end.x == -1)
				{
					end.x = i;
					end.y = j;
					if (a[i][j + 1] == 'x' || a[i][j + 1] == 'w') end.dir = 1;
					if (a[i + 1][j] == 'x' || a[i + 1][j] == 'w') end.dir = 0;
				}

				if (a[i][j] == 'o' || a[i][j] == 'w' || a[i][j] == 'x') a[i][j] = '.';
			}
		

		while (!Q.empty()) Q.pop();
		
		Q.push( start );

		memset(table, -1, sizeof(table));
		table[start.x][start.y][start.dir] = start.dpt;

		int ret = -1;
		while ( !Q.empty() )
		{
			state w = Q.front(); Q.pop();
//			cout << w.x << ' ' << w.y << ' ' << w.dir << ' ' << w.dpt << endl;

			if (w == end) 
			{
				ret = w.dpt;
				break;
			}
			if (w.dir == 0)
			{
				if ( check(w.x, w.y-1) && check(w.x-1, w.y-1) && check(w.x+1, w.y-1) && check(w.x, w.y+1) )	update( w.x+1, w.y-1, 1, w.dpt + 2 );
				if ( check(w.x, w.y+1) && check(w.x-1, w.y+1) && check(w.x+1, w.y+1) && check(w.x, w.y-1) )	update( w.x+1, w.y, 1, w.dpt + 2 );

				if ( check(w.x+1, w.y-1) && check(w.x, w.y-1) && check(w.x+2, w.y-1) && check(w.x+1, w.y+1) )	update( w.x, w.y-1, 1, w.dpt + 2 );
				if ( check(w.x+1, w.y+1) && check(w.x, w.y+1) && check(w.x+2, w.y+1) && check(w.x+1, w.y-1) )	update( w.x, w.y, 1, w.dpt + 2 );

				if ( check(w.x, w.y-1) && check(w.x, w.y+1) && check(w.x+2, w.y) ) update( w.x, w.y-1, 1, w.dpt + 2);
				if ( check(w.x, w.y-1) && check(w.x, w.y+1) && check(w.x+2, w.y) ) update( w.x, w.y, 1, w.dpt + 2);
				
				if ( check(w.x+1, w.y-1) && check(w.x+1, w.y+1) && check(w.x-1, w.y) ) update( w.x+1, w.y-1, 1, w.dpt + 2);
				if ( check(w.x+1, w.y-1) && check(w.x+1, w.y+1) && check(w.x-1, w.y) ) update( w.x+1, w.y, 1, w.dpt + 2);
				
				if ( check(w.x, w.y-1) && check(w.x, w.y+1) && check(w.x+1, w.y-1) && check(w.x+1, w.y+1) )	update( w.x, w.y-1, 0, w.dpt + 2 );
				if ( check(w.x, w.y-1) && check(w.x, w.y+1) && check(w.x+1, w.y-1) && check(w.x+1, w.y+1) )	update( w.x, w.y+1, 0, w.dpt + 2 );
			}
			else if (w.dir == 1)
			{
				if ( check(w.x-1, w.y-1) && check(w.x-1, w.y) && check(w.x-1, w.y+1) && check(w.x+1, w.y) )	update( w.x-1, w.y+1, 0, w.dpt + 2 );
				if ( check(w.x-1, w.y) && check(w.x-1, w.y+1) && check(w.x-1, w.y+2) && check(w.x+1, w.y+1) ) update( w.x-1, w.y, 0, w.dpt + 2 );

				if ( check(w.x+1, w.y-1) && check(w.x+1, w.y) && check(w.x+1, w.y+1) && check(w.x-1, w.y) )	update( w.x, w.y+1, 0, w.dpt + 2 );
				if ( check(w.x+1, w.y) && check(w.x+1, w.y+1) && check(w.x+1, w.y+2) && check(w.x-1, w.y+1) ) update( w.x, w.y, 0, w.dpt + 2 );


				if ( check(w.x-1, w.y) && check(w.x+1, w.y) && check(w.x, w.y+2) ) update( w.x-1, w.y, 0, w.dpt + 2);
				if ( check(w.x-1, w.y) && check(w.x+1, w.y) && check(w.x, w.y+2) ) update( w.x, w.y, 0, w.dpt + 2);
				
				if ( check(w.x-1, w.y+1) && check(w.x+1, w.y+1) && check(w.x, w.y-1) ) update( w.x-1, w.y+1, 0, w.dpt + 2);
				if ( check(w.x-1, w.y+1) && check(w.x+1, w.y+1) && check(w.x, w.y-1) ) update( w.x, w.y+1, 0, w.dpt + 2);


				if ( check(w.x-1, w.y) && check(w.x+1, w.y) && check(w.x-1, w.y+1) && check(w.x+1, w.y+1) )	update( w.x-1, w.y, 1, w.dpt + 2 );
				if ( check(w.x-1, w.y) && check(w.x+1, w.y) && check(w.x-1, w.y+1) && check(w.x+1, w.y+1) )	update( w.x+1, w.y, 1, w.dpt + 2 );
			} 
			else if ( w.dir == 2)
			{
				if ( check(w.x-1, w.y) && check(w.x+1, w.y) ) update(w.x-1, w.y, 2, w.dpt+1 );
				if ( check(w.x-1, w.y) && check(w.x+1, w.y) ) update(w.x+1, w.y, 2, w.dpt+1 );
				if ( check(w.x, w.y-1) && check(w.x, w.y+1) ) update(w.x, w.y-1, 2, w.dpt+1 );
				if ( check(w.x, w.y-1) && check(w.x, w.y+1) ) update(w.x, w.y+1, 2, w.dpt+1 );
			}
		}
		cout << ret << endl;
	}
}

