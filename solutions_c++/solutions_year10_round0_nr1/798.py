#include <cstdio>

int main()
{
	long long int T, n, k;
	scanf("%lld", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%lld%lld", &n, &k);
		if ((k+1) % (1<<n) == 0)
			printf("Case #%d: ON\n", t);
		else
			printf("Case #%d: OFF\n", t);
	}
	return 0;
}

