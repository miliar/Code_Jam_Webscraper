#include <stdio.h>
#include <string.h>
#define N 10009

long long a[N];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int cas = 1;
	while (t--)
	{
		long long n;
		long long l, h;
		scanf("%lld%lld%lld", &n, &l, &h);
		for (int i = 0; i < n; ++i)
			scanf("%lld", &a[i]);
		long long res = -1; 
		for (long long i = l; i <= h; ++i)
		{
			int j;
			for (j = 0; j < n; ++j)
			{
				if ((i % a[j] != 0)&&(a[j] % i != 0))
					break;
			}
			if (j == n)
			{
				res = i;
				break;
			}
				
		}

		printf("Case #%d: ", cas++);
		if (res == -1)
			printf("NO\n");
		else printf("%lld\n", res);

		


		
	}
	return 0;
}