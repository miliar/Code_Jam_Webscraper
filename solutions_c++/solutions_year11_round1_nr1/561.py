#include <stdio.h>

long long gcd(long long a, long long b)
{
	return (b == 0 ? a : gcd(b, a % b));
}

int main()
{
	int t, z;
	scanf(" %d", &t);
	for(z = 0; z < t; z ++)
	{
		long long n, pd, pg, k = 100, l = 100, g, i = 1;
		bool win = false;
		scanf(" %lld %lld %lld", &n, &pd, &pg);
		g = gcd(k, pd);
		k /= g;
		pd /= g;
		g = gcd(l, pg);
		l /= g;
		pg /= g;
		if (pg == 0 && pd == 0)
			win = true;
		else if (pg == 0)
			win = false;
		else if(pg == l && pd != k)
			win = false;
		else if(k > n)
			win = false;
		else
			win = true;
		if(win == false)
			printf("Case #%d: Broken\n", z + 1);
		else
			printf("Case #%d: Possible\n", z + 1);
	}
}
