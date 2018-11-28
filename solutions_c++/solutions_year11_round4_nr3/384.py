#include <stdio.h>
#include <assert.h>

int P[80000];

void solve()
{
	long long n, p;
	scanf("%lld", &n);
	int c = n > 1;
	for (int i = 0; (p = (long long)P[i] * P[i]) <= n; i++)
	{
		do
		{
			c++;
			p *= P[i];
		}
		while (p <= n);
	}
	printf("%d\n", c);
}

int main()
{
	static bool T[1000001];
	int pc = 0;
	for (int i = 2; i <= 1000000; i++)
		if (!T[i])
		{
			P[pc++] = i;
			for (int j = 2 * i; j <= 1000000; j += i)
				T[j] = true;
		}
	P[pc++] = 1000001;

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}