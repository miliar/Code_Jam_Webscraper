#include <cstdio>
#include <cstring>

typedef unsigned long long ull;

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	int T;
	scanf("%u", &T);
	for (int tc = 0; tc < T; ++tc)
	{
		unsigned R, k, N;	
		scanf("%u%u%u", &R, &k, &N);
		static ull g[1010];
		for (int i = 0; i < (int)N; ++i)
			scanf("%I64u", &g[i]);
		static ull cash[1010];		
		static ull next[1010];
		for (int i = 0; i < (int)N; ++i)
		{
			ull acu = g[i];
			int j;
			for (j = (i + 1) % N; j != i; j = (j + 1) % N)
				if (acu + g[j] <= k)
					acu += g[j];
				else
					break;
			cash[i] = acu;
			next[i] = j;
		}

		ull total = 0;
		int j = 0;
		if (R > 2 * N)	
		{
			static int visited[1010];	
			memset(visited, 0, sizeof visited);
			static int id[2010];
			static int already[2010];
			int nVisited = 0;
			while (!visited[j])
			{
				visited[j] = 1;
				id[j] = nVisited;
				already[j] = total;
				++nVisited;
				total += cash[j];
				j = next[j];
			}

			total = already[j] + (total - already[j]) * ((R - id[j]) / (nVisited - id[j])); 
			R = (R - id[j]) % (nVisited - id[j]);
		}

		for (int i = 0; i < (int)R; ++i) 
		{
			total += cash[j];
			j = next[j];
		}

		printf("Case #%u: %I64u\n", tc + 1, total);
	}

	return 0;
}
