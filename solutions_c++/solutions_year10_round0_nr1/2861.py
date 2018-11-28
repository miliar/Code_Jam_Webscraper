#include <cstdio>
#include <cmath>

int main()
{
	unsigned long C;
	scanf("%ld", &C);
	for (unsigned long i = 1; i <= C; i++)
	{
		unsigned long N, K, res;
		scanf("%ld %ld", &N, &K);
		unsigned long full = pow(2, N);
		K %= full;
		if (K == full-1)
			res = true;
		else
			res = false;
		printf("Case #%ld: %s\n", i, (res)?("ON"):("OFF"));
	}
	return 0;
}
