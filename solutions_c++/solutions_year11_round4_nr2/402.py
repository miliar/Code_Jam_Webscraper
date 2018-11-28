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
#define DEBUG 1
#define PRINT(x...) DEBUG && printf(x)

int T;
int R, C, D;
char w[100][100];

int solve()
{
	int res = -1;
	for (int K = 3; K <= R && K <= C; K++)
	{
		for (int i = 0; i+K-1 < R; i++)
		for (int j = 0; j+K-1 < C; j++)
		{
			int resX = 0, resY = 0;
			int cx = i+K, cy = j+K;
			for (int ki = 0; ki < K; ki++)
			for (int kj = 0; kj < K; kj++)
			{
				if (ki==0 && kj==0) continue;
				if (ki==0 && kj==K-1) continue;
				if (ki==K-1 && kj==0) continue;
				if (ki==K-1 && kj==K-1) continue;
				
				int px = i+ki*2+1, py = j+kj*2+1;
				
				resX += (px-cx)*(D+w[i+ki][j+kj]-'0');
				resY += (py-cy)*(D+w[i+ki][j+kj]-'0');
			}
			if (!resX && !resY)
				res = K;
		}
	}
	return res;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d%d%d", &R, &C, &D);
		REP(i, R) 
			scanf("%s", w[i]);
		
		int res = solve();
		if (res == -1)
			printf("Case #%d: IMPOSSIBLE\n", tc+1);
		else
			printf("Case #%d: %d\n", tc+1, res);
	}
}
