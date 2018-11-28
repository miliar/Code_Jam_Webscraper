#include <vector>
#include <algorithm>

#include <cstdio>
#include <cstdlib>

using namespace std;

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define INF 1000000000

typedef long long llint;

int gcd(int a, int b)
{
	while (b != 0)
	{
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int idxCase = 0; idxCase < T; ++idxCase)
	{
		llint L;
		int N;
		scanf("%lld%d", &L, &N);
		vector<int> boards(N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &boards[i]);
		sort(boards.rbegin(), boards.rend());
		int bmax = boards[0];
		int g = 0;
		ITERATE (it, boards)
			g = gcd(g, *it);
		llint ans;
		if (L % g != 0)
			ans = -1;
		else
		{
			L /= g;
			bmax /= g;
			ITERATE (it, boards)
				*it /= g;
			vector<int> tablePrev(bmax, INF);
			vector<int> table(bmax);
			table[0] = 0;
			bool good = true;
			for (int i = 1; i < bmax; ++i)
			{
				table[i] = INF;
				bool good1 = false;
				ITERATE (it, boards)
				{
					int prev = i - *it;
					int count;
					if (prev < 0)
						count = tablePrev[prev + bmax] + 1;
					else
						count = table[prev] + 1;
					if (count < table[i])
					{
						good1 = (it == boards.begin());
						table[i] = count;
					}
				}
				if (!good1)
					good = false;
			}
			while (true)
			{
				if (L < bmax)
				{
					if (table[L] == INF)
						ans = -1;
					else
						ans = table[L];
					break;
				}
				if (good)
				{
					ans = table[L % bmax] + L / bmax;
					break;
				}
				swap(table, tablePrev);
				L -= bmax;
				good = true;
				for (int i = 0; i < bmax; ++i)
				{
					table[i] = INF;
					bool good1 = false;
					ITERATE (it, boards)
					{
						int prev = i - *it;
						int count;
						if (prev < 0)
							count = tablePrev[prev + bmax] + 1;
						else
							count = table[prev] + 1;
						if (count < table[i])
						{
							good1 = (it == boards.begin());
							table[i] = count;
						}
					}
					if (!good1)
						good = false;
				}
			}
		}
		printf("Case #%d: ", idxCase + 1);
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%lld\n", ans);
	}
	return 0;
}
