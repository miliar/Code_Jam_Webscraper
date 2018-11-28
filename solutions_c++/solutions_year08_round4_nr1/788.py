#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i, lo, hi) for(int i = (lo); i < (hi); ++i)
#define MP make_pair
#define PB push_back

typedef long long ll;

#define VAL(v1, v2, g) ((g == 0) ? (v1 | v2) : (v1 & v2))

int M, V, nInt, nLv, v[11000], g[11000], c[11000];

int memo[11000][2];

int rec(int node, int tgt)
{
	int &ret = memo[node][tgt];
	if(ret != -2) return memo[node][tgt];

	if(node > nInt)
	{
		if(v[node] == tgt) return ret = 0;
		return ret = -1;
	}

	int G = g[node], C = c[node], ch1 = 2 * node, ch2 = 2 * node + 1;
	int ans = 100000;
	FOR(vch1, 0, 2)
	{
		FOR(vch2, 0, 2)
		{
			if(VAL(vch1, vch2, G) == tgt)
			{
				if(rec(ch1, vch1) != -1 && rec(ch2, vch2) != -1)
					ans = min(ans, rec(ch1, vch1) + rec(ch2, vch2));
			}
			if(C == 1 && VAL(vch1, vch2, 1 - G) == tgt)
			{
				if(rec(ch1, vch1) != -1 && rec(ch2, vch2) != -1)
					ans = min(ans, rec(ch1, vch1) + rec(ch2, vch2) + 1);
			}
		}
	}

	if(ans == 100000) return ret = -1;
	return ret = ans;
}

int main()
{
	int numCases;
	scanf("%d", &numCases);

	FOR(tc, 1, numCases + 1)
	{
		scanf("%d %d", &M, &V);
		nInt = (M - 1) / 2;
		FOR(i, 1, nInt + 1)
		{
			scanf("%d %d", &g[i], &c[i]);
		}
		nLv = (M + 1) / 2;
		FOR(i, 1, nLv + 1)
		{
			scanf("%d", &v[nInt + i]);
		}

		FOR(i, 0, 11000) FOR(j, 0, 2) memo[i][j] = -2;

		int best = rec(1, V);
		if(best == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else
		{
			printf("Case #%d: %d\n", tc, best);
		}
	}

	return 0;
}
