#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;
#define MAX 1000

long long people[MAX];
int next[MAX];
long long counts[MAX];

int main()
{
	freopen("C.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int R, K, N;
		scanf("%d%d%d", &R, &K, &N);
		long long all = 0;
		for (int i = 0; i < N; i++)
		{
			scanf("%lld", &people[i]);
			all += people[i];
		}
		long long res = 0;
		if (K >= all)
		{
			res = all * R;
		}
		else
		{
			for (int i = 0; i < N; i++)
			{
				int j = i;
				long long cnt = 0;
				while (cnt + people[j % N] <= K)
				{
					cnt += people[j % N];
					j++;
				}
				next[i] = j % N;
				counts[i] = cnt;
			}
			int pos = 0;
			for (int i = 0; i < R; i++)
			{
				res += counts[pos];
				pos = next[pos];
			}
		}
		printf("Case #%d: %lld\n", t+1, res);		
	}
	fclose(stdout);
	return 0;
}
