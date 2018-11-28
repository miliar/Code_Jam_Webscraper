/* by Ashar Fuadi (fushar) */

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>

#include <vector>
#include <string>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

int T;
char grid[10][10];

bool won(char p)
{
	bool found;
	// row
	REP(i, 4)
	{
		found = true;
		REP(j, 4) if (grid[i][j] != p && grid[i][j] != 'T')
			found = false;
		if (found)
			return true;
	}
	
	// column
	REP(j, 4)
	{
		found = true;
		REP(i, 4) if (grid[i][j] != p && grid[i][j] != 'T')
			found = false;
		if (found)
			return true;
	}
	
	// main diagonal
	found = true;
	REP(i, 4) if (grid[i][i] != p && grid[i][i] != 'T')
		found = false;
	if (found)
		return true;

	// other diagonal
	found = true;
	REP(i, 4) if (grid[i][3-i] != p && grid[i][3-i] != 'T')
		found = false;
	if (found)
		return true;
	return false;
}

bool draw()
{
	REP(i, 4) REP(j, 4) if (grid[i][j] == '.')
		return false;
	return true;
}

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		REP(i, 4)
			scanf("%s", grid[i]);
		printf("Case #%d: ", tc+1);
		if (won('O'))
			printf("O won\n");
		else if (won('X'))
			printf("X won\n");
		else if (draw())
			printf("Draw\n");
		else
			printf("Game has not completed\n");
	}
}
