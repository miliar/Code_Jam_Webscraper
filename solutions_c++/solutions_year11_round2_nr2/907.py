#include <iostream>

using namespace std;

struct paris
{
	long long sk;
	long long x;
} mas[200];

int n,d,t;

long long max(long long a, long long b)
{
	if (a > b)
	{
		return a;
	}
	else
	{
		return b;
	}
}

bool check(long long x)
{
	long long currx = -1000000000LL*1000000000LL;

	for (int j = 0; j < n; j++)
	{
		currx = max(currx + d, mas[j].x - x) + (mas[j].sk -1) * d;

		if (currx > mas[j].x + x)
		{
			return false;
		}
	}

	return true;
}

int main()
{
	freopen("B1.in","rt",stdin);
	freopen("B1.out","wt",stdout);

	scanf("%d", &t);

	for (int i = 1; i <= t; i++)
	{
		scanf("%d %d", &n, &d);

		d *= 2;

		for (int j = 0; j < n; j++)
		{
			scanf("%lld %lld", &mas[j].x, &mas[j].sk);
			mas[j].x *= 2;
		}

		long long a = 1000000000LL*1000000000LL;
		long long b = -1;

		while (a -b > 1)
		{
			long long c = (a+b) / 2;

			if (check(c))
			{
				a = c;
			}
			else
			{
				b = c;
			}
		}

		cout << "Case #" << i << ": ";
		cout << ((double) a) / 2 << endl;
	}

	return 0;
}