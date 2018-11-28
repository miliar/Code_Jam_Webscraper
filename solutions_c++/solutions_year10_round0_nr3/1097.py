#include <stdio.h>


int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int t, r, k, n, *g, *s, *used, *castig, head, round, total;

	scanf("%d", &t);

	for(int test = 1; test <= t; ++test)
	{
		scanf("%d %d %d", &r, &k, &n);
		g = new int[n + 1];
		s = new int[n + 1];
		castig = new int[n + 1];
		used = new int[n + 1];
		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &g[i]);
			used[i] = 0;
		}
		s[0] = g[0];
		for(int i = 1; i < n; ++i)
		{
			s[i] = s[i - 1] + g[i];
		}
		round = 1;
		head = 0;
		total = 0;
		while(round <= r && !used[head])
		{
			used[head] = round;
			castig[round] = 0;
			int nr = 1;
			while(castig[round] + g[head] <= k && nr <= n)
			{
				castig[round] += g[head];
				head = (head + 1) % n;
				++nr;
			}
			total += castig[round];
			++round;
			//printf("head = %d round = %d used[head] = %d\n ", head, round, used[head]);
		}
		if(round > r)
		{
			printf("Case #%d: %d\n", test, total);
		}
		else
		{
		//	printf("total vechi %d\n", total);
			int times = round - used[head];
			int norepeat = 0;
			for(int i = 1; i < used[head]; ++i)
			{
				norepeat += castig[i];
			}
		//	printf("norepeat %d\n", norepeat);
			total += (total - norepeat) * ((r - round + 1) / times);
			int inplus = (r - round + 1) % times;
		//	printf("inplus = %d\n", inplus);
			for(int i = 0; i < inplus; ++i)
			{
				total += castig[used[head] + i];
			}
			printf("Case #%d: %d\n", test, total);
		}
	}

	return 0;
}
