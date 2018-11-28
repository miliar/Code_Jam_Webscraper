#include <vector>
#include <algorithm>

#include <cstdio>

using namespace std;

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define INF (100000 * 1024LL)

int main()
{
	int T;
	scanf("%d", &T);
	for (int idxCase = 0; idxCase < T; ++idxCase)
	{
		int P;
		scanf("%d", &P);
		int teams = 1 << P;
		vector<int> M(teams);
		for (int i = 0; i < teams; ++i)
			scanf("%d", &M[i]);
		vector<vector<int> > prices(P);
		for (int level = 0; level < P; ++level)
		{
			prices[level].resize(teams >> (level + 1));
			for (int j = 0; j < (teams >> (level + 1)); ++j)
				scanf("%d", &prices[level][j]);
		}
		vector<vector<long long> > table(P);
		for (int t = 0; t < P; ++t)
		{
			table[t].resize(teams >> 1);
			for (int i = 0; i < (teams >> 1); ++i)
			{
				int m = min(M[i << 1], M[(i << 1) + 1]);
				if (t > m)
					table[t][i] = INF;
				else if (t == m)
					table[t][i] = prices[0][i];
				else
					table[t][i] = 0;
			}
		}
		for (int level = 1; level < P; ++level)
		{
			vector<vector<long long> > newTable(P - level);
			for (int t = 0; t < P - level; ++t)
			{
				newTable[t].resize(teams >> (level + 1));
				for (int i = 0; i < (teams >> (level + 1)); ++i)
					newTable[t][i] = min(table[t + 1][i << 1] + table[t + 1][(i << 1) + 1], prices[level][i] + table[t][i << 1] + table[t][(i << 1) + 1]);
			}
			swap(table, newTable);
		}
    	printf("Case #%d: %lld\n", idxCase + 1, table[0][0]);
	}
	return 0;
}
