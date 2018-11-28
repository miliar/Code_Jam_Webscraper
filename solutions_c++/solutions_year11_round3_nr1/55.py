/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair

int T, R, C;
char data[100][100];

bool solve()
{
	REP(i, R) REP(j, C) if (data[i][j] == '#')
	{
		if (i == R-1 || j == C-1) return false;
		if (data[i+1][j] != '#') return false;
		if (data[i][j+1] != '#') return false;
		if (data[i+1][j+1] != '#') return false;
		
		data[i][j] = '/';
		data[i][j+1] = '\\';
		data[i+1][j] = '\\';
		data[i+1][j+1] = '/';
	}
	
	REP(i, R)
		printf("%s\n", data[i]);
	return true;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d%d", &R, &C);
		printf("Case #%d:\n", tc+1);
		REP(i, R)
		{
			scanf("%s", data[i]);
		}
			if (!solve())
				puts("Impossible");
		
	}
}
