#include <cstdio>

long long g[1000];
long long s[1000];
long long C[1000];
long long cycleLength, cycleY;

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		long long k, r, n;
		long long y = 0;
		scanf("%lld%lld%lld", &r, &k, &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%lld", &g[i]);
			s[i] = -1;
		}
		int q = 0;
		cycleLength = 0;
		cycleY = 0;
		int aux = 1;
		while (r > 0 && s[q] < 0)
		{
			s[q] = aux++;
			C[q] = y;
			r--;

			int c = 0;
			while (c + g[q] <= k)
			{
				c += g[q++];
				q %= n;
				if (s[q] == aux-1)
					break;
			}
			//printf("Round %d: %d\tstart: %d\n", aux-1, c, k);
			y += c;
		}
		//printf("Rounds %d\n", r);
		if (s[q] > 0)
		{
			cycleLength = aux - s[q];
			cycleY = y - C[q];
			y += cycleY*(r/cycleLength);
			r %= cycleLength;
			
			/*printf("Cycle length %d\n", cycleLength);
			printf("Cycle y %d\n", cycleY);
			printf("y %lld\n", y);*/
			while (r > 0)
			{
				r--;
				int c = 0;
				while (c + g[q] <= k)
				{
					c += g[q++];
					q %= n;
				}
				y += c;
			}
		}
		
		printf("Case #%d: %lld\n", t, y);
	}
	return 0;
}

