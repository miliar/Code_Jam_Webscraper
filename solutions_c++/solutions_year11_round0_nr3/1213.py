#include <stdio.h>

const int inf = (1 << 30);

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int n, nr, t;
	scanf("%d", &t);

	for(int test = 1; test <= t; ++test)
	{
		scanf("%d", &n);
		int m = inf;
		int sum = 0;
		int xorsum = 0;
		for(int i = 0; i < n; ++i)
		{
			scanf("%d", &nr);
			sum += nr;
			xorsum ^= nr;
			if(m > nr)
			{
				m = nr;
			}
		}
		if(xorsum != 0)
		{
			printf("Case #%d: NO\n", test);
		}
		else
		{
			printf("Case #%d: %d\n", test, sum - m);
		}
	}

	return 0;
}
