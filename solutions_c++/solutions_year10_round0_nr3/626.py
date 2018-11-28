#include <cstdio>
#include <cstring>

#define MAXN 1005

int R, K, N;
int groups[MAXN];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int cases;
	
	scanf("%d", &cases);
	for (int cas = 0; cas < cases; ++cas)
	{
		__int64 sz = 0;
		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &groups[i]);
			sz += groups[i];
		}

		__int64 ans = 0;
		if (sz <= K)
			ans = sz * R;
		else
		{
			int follow[MAXN];
			__int64 cost[MAXN];
			int pos = 0;

			memset(follow, -1, sizeof(follow));
			while (follow[pos] < 0)
			{
				sz = 0;
				for (int i = 0; i < N; ++i)
				{
					if (sz + groups[(pos + i) % N] > K) 
					{
						cost[pos] = sz;
						follow[pos] = (pos + i) % N;
						pos = follow[pos];
						break;
					}
					sz += groups[(pos + i) % N];
				}
			}

			int pos2 = 0;
			while (R > 0 && pos2 != pos)
			{
				ans += cost[pos2];
				pos2 = follow[pos2];
				--R;
			}

			__int64 costC = 0;
			int lenC = 0;
			do
			{
				costC += cost[pos2];
				++lenC;
				pos2 = follow[pos2];
			} while (pos2 != pos);

			ans += costC * (R / lenC);
			for (int i = 0; i < R % lenC; ++i)
			{
				ans += cost[pos2];
				pos2 = follow[pos2];
			}
		}

		printf("Case #%d: %I64d\n", cas + 1, ans);
	}

	return 0;
}
