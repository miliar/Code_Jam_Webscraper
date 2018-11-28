#include <iostream>
#include <cstdio>
#include <string>

int a[1001000];


int main()
{
	int N;
	scanf("%d", & N);
	for (int Case = 1; Case <= N; Case++)
	{
		int K, n, d[120];
		scanf("%d", & K);
		scanf("%d", & n);
		for (int i = 0; i < n; i++)
			scanf("%d", & d[i]);
		
		for (int i = 0; i < K; i++)
			a[i] = 0;

		int p = 0;
		for (int i = 1; i <= K; i++)
		{
			int w = (i - 1) % (K - i + 1);
			while (a[p])
				p = (p + 1) % K;
			for (int j = 0; j < w; j++)
			{
				p = (p + 1) % K;
				while (a[p])
					p = (p + 1) % K;
			}
			a[p] = i;
		}

		printf("Case #%d:", Case);
		for (int i = 0; i < n; i++)
			printf(" %d", a[d[i] - 1]);
		printf("\n");
	}

	return 0;
}
