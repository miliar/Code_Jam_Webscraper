#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long int big;

big l, t, n, c, a, D[1000], l1, l2;

big dist()
{
	big m = 0.0;
	for (big i = 0; i < n; i++)
	{
		if (i == l1 || i == l2)
		{
			if (m >= t)
			{
				m += D[i];
			}
			else if (m + D[i] >= t)
			{
				m += (t - m) + (D[i] - (t - m) / 2);
			}
			else
			{
				m += D[i] * 2;
			}
		}
		else
		{
			m += D[i] * 2;
		}
	}
	return m;
}

int main()
{
	big ncases;

	cin >> ncases;
	for (big caseno = 1; caseno <= ncases; caseno++)
	{
		cin >> l >> t >> n >> c;
		for (big i = 0; i < c; i++)
		{
			cin >> a;
			for (big k = 0; k * c + i + 1 <= n; k++)
				D[k * c + i] = a;
		}

		big s = -1;
		l1 = l2 = -1;
		if (l == 2)
		{
			for (l1 = 0; l1 < n; l1++)
				for (l2 = l1 + 1; l2 < n; l2++)
				{
					big d = dist();
					if (s < 0 || d < s)
						s = d;
				}
		}
		else if (l == 1)
		{
			for (l1 = 0; l1 < n; l1++)
			{
				big d = dist();
				if (s < 0 || d < s)
					s = d;
			}
		}
		else
			s = dist();

		printf("Case #%lli: %lli\n", caseno, (big)s);
	}
}
