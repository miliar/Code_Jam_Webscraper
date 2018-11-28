#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long int i, j, t, n, k, m[33], q, fl;
	scanf("%lld", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%lld %lld", &n, &k);
		k %= (long long int) pow(2.0, n + 0.0);
		memset(m, 0, sizeof m);
		q = 0;
		while (k > 0)
		{
			q++;
			m[q] = k % 2;
			k /= 2;
		}
		fl = true;
		for (j = 1; j <= n; j++)
			fl &= m[j];
		if (fl)
		{
			printf("Case #%d: ON\n", i);
		}
		else
		{
			printf("Case #%d: OFF\n", i);
		}
	}
	return 0;
}