#include <iostream>
using namespace std;

int digits(int a)
{
	int n = 1;	

	while (a / 10 != 0)
	{
		++n;
		a /= 10;
	}
	return n;
}

int z[] = {0, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int main()
{
	int a, b, m, n, t, i, x, j, k, r, s;
	int w[32];
	int u, p;

	cin >> t;

	for (i = 1; i <=t ; ++i)
	{
		cin >> a >> b;

		cout << "Case #" << i << ": ";

		if (a >= b || b < 10)
		{
			cout << 0 << endl;
			continue;
		}				

		x = 0;
		k = digits(a);
		for (n = a; n < b; ++n)
		{
			r = 10;
			s = z[k] / r;
			u = 0;
			for (j = 1; j < k; ++j)
			{
				m = n % r * s + n / r; 
				if (n < m && m <= b)
				{
					for (p = 0; p < u; ++p)
						if (w[p] == m)
							break;

					if (p == u)
					{
						++x;
						w[u++] = m;
					}
				}
				r *= 10;
				s /= 10;
			}
		}

		cout << x << endl;
	}

	return 0;
}

