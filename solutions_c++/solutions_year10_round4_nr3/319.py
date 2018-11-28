#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define REP(i,n) for (int i = 1; i <= (n); ++i)
#define FORE(i,c) for (typeof(c.begin()) i = c.begin(); i != c.end(); ++i)
using namespace std;

int T, R;
int grid[101][101], temp[101][101];
int main()
{
	freopen("C-small-attempt0.in", "r", stdin), freopen("C-small.out", "w", stdout);
	//freopen("C-large.in", "r", stdin), freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	REP(t, T)
	{
		scanf("%d", &R);
		REP(i, 100) REP(j, 100) grid[i][j] = 0;
		REP(i, R)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = x1; i <= x2; i++)
			for (int j = y1; j <= y2; j++)
				grid[i][j] = 1;
		}
		int res = 0;
		while (true)
		{
			int cur = 0;
			REP(i, 100) REP(j, 100) cur += grid[i][j];
			if (cur == 0) break;
			res++;
			memcpy(temp, grid, sizeof temp);
			REP(i, 100) REP(j, 100)
				if (temp[i][j] && !temp[i-1][j] && !temp[i][j-1])
					grid[i][j] = 0;
				else if (!temp[i][j] && temp[i-1][j] && temp[i][j-1])
					grid[i][j] = 1;
		}
		
		printf("Case #%d: %d\n", t, res);
	}
}
