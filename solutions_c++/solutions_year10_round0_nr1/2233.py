// Problem C
#include <stdio.h>
const int MAXN = 1000;
int weight[MAXN];
int next[MAXN];
int people[MAXN];
int main()
{
	int t;
	scanf("%d", &t);
	for (int c = 1; c <= t; c++)
	{
		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);
		for (int i = 0; i < N; i++)
			scanf("%d", &people[i]);
		for (int i = 0; i < N; i++)
		{
			weight[i] = people[i];
			int j;
			for (j = (i + 1) % N; j != i; j = (j + 1) % N)
			{
				if (weight[i] + people[j] > k) break;
				weight[i] += people[j];
			}
			next[i] = j;
		}
		long long int result = 0;
		int s = 0;
		for (int i = 0; i < R; i++)
		{
			result += weight[s];
			s = next[s];
		}
		printf("Case #%d: %I64d\n", c, result);
	}
}