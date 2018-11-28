#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <string>

#define INFINITY 200000000

using namespace std;

int p;
int players;
int m[1024];
int cost[1024];
int cache[1024][11];

int dp(int game, int missed)
{
	if (game >= players-1)
	{
		if (missed <= m[game-(players-1)])
		{
			return 0;
		}
		else
		{
			return INFINITY;
		}
	}
	if (cache[game][missed])
		return cache[game][missed]-1;
	int s;
	int e;
	for (s = game; s < players-1; s = s*2+1);
	for (e = game; e < players-1; e = e*2+2);
	int i;
	for (i = s - (players-1); i <= e - (players-1); i++)
		if (missed > m[i])
			return INFINITY;
	cache[game][missed] = 1+min(cost[game]+dp(game*2+1, missed)+dp(game*2+2, missed), dp(game*2+1, missed+1) + dp(game*2+2, missed+1));
	return cache[game][missed]-1;
}

void clear()
{
	int i, j;
	for (i = 0; i < 1024; i++)
		for (j = 0; j < 11; j++)
			cache[i][j] = 0;
}

int main() 
{
	int T;
	int T_i;
	scanf("%d", &T);
	for (T_i = 1; T_i <= T; T_i++)
	{
		clear();
		int i;
		scanf("%d", &p);
		players = 1;
		for (i = 0; i < p; i++)
			players*=2;
		for (i = 0; i < players; i++)
			scanf("%d", &m[players-1-i]);
		for (i = 0; i < players-1; i++)
			scanf("%d", &cost[players-2-i]);
		printf("Case #%d: %d\n", T_i, dp(0, 0));
	}
}
