#include <iostream>
#include <cmath>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

const int	maxN = 20000;

int		f[maxN][2], kind[maxN], canCh[maxN];
int		M, V;

void	best(int &a, int b)
{
	if (b < 0) return;
	if (a < 0 || a > b) a = b;
}

int	main()
{
	int nCase;
	scanf("%d", &nCase);
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		scanf("%d %d", &M, &V);
		
		for (int i = 1; i <= (M - 1) / 2; ++i) scanf("%d %d", &kind[i], &canCh[i]);
		for (int i = (M + 1) / 2; i <= M; ++i) scanf("%d", &kind[i]);

		for (int u = M; u >= 1; --u)
		{
			if (u * 2 > M)
			{
				f[u][kind[u]] = 0;
				f[u][1 - kind[u]] = -1;
				continue;
			}

			f[u][0] = f[u][1] = -1;
			int cost[2];
			cost[kind[u]] = 0;

			if (canCh[u])
				cost[1 - kind[u]] = 1;
			else
				cost[1 - kind[u]] = - M - 1;

			for (int a = 0; a <= 1; ++a) if (f[u * 2][a] >= 0)
				for (int b = 0; b <= 1; ++b) if (f[u * 2 + 1][b] >= 0)
				{
					best(f[u][a | b], f[u * 2][a] + f[u * 2 + 1][b] + cost[0]);
					best(f[u][a & b], f[u * 2][a] + f[u * 2 + 1][b] + cost[1]);
				}
		}

		if (f[1][V] < 0)
			printf("Case #%d: IMPOSSIBLE\n", nowCase);
		else
			printf("Case #%d: %d\n", nowCase, f[1][V]);
	}
	return 0;
}
