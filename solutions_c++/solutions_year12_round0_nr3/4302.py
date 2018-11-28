#include <cstdio>
#include <cstdlib>
#include <cstdint>

long mask(long a)
{
	long m = 1;
	while (a > 0)
	{
		a /= 10;
		m *= 10;
	}
	return m / 10;
}

long rotate(long a, long m)
{
	int c = a % 10;
	a /= 10;
	return a + m * c;
}

int main()
{
	long T;
	scanf("%ld", &T);
	for (long t = 1; t <= T; t++)
	{
		long A, B, count = 0;
		scanf("%ld %ld", &A, &B);
		for (long i = A; i <= B; i++)
		{
			long m = mask(i);
			long j = i;
			while (true)
			{
				j = rotate(j, m);
				if (j == i) break;
				if (j > i && j <= B) count++;
			}
		}
		printf("Case #%ld: %ld\n", t, count);
	}
	return 0;
}
