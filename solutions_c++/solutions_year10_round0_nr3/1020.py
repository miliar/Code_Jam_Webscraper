#include <iostream>

const int maxN = 1000;

int T, K, N, R;
_int64 g[maxN];
_int64 f[maxN];
_int64 gain;
int next[maxN];

void work(void)
{
	int i, j, tot;

	for(i=0; i<N; i++)
	{
		tot = 0;
		j = i;
		while(tot + g[j] <= K)
		{
			tot += g[j];
			j = (j + 1) % N;
		}
		f[i] = tot;
		next[i] = j;
	}
	j = 0;
	for(i=0; i<R; i++)
	{
		gain+=f[j];
		j = next[j];
	}
}

int main()
{
	int i, j;
	_int64 tot;

	freopen("park.in", "r", stdin);
	freopen("park.out", "w", stdout);
	scanf("%d", &T);
	for(i=1; i<=T; i++)
	{
		scanf("%d%d%d", &R, &K, &N);
		tot = 0;
		gain = 0;
		for(j=0; j<N; j++)
		{
			scanf("%d", &g[j]);
			tot+=g[j];
		}
		if(tot <= K)	gain = tot * R;
		else work();
		printf("Case #%d: %I64d\n", i, gain);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}