#include <iostream>
#include <cstdio>
using namespace std;

const long MOD = 100003;

int main()
{
	long resio[26];
	memset(resio, 0xff, sizeof(resio));

	long t; scanf("%ld", &t);
	for (int test = 1; test <= t; test++)
	{
		long sol = 0;

		long n; scanf("%ld", &n);
		if (resio[n] == -1)
		{
			for (long s = 0; s < (1<<(n-2)); s++)
			{
				int rank[25], rr = 1;
				memset(rank, 0xff, sizeof(rank));

				for (int i = 0; i < n - 2; i++)
				{
					if (s & (1<<i)) rank[i+2] = rr++;
				}

				int p = rr;
				while (p != 1)
				{
					if (rank[p] == -1)
						break;
					else p = rank[p];
				}

				if (p == 1)
				{
					sol++;
					sol %= MOD;
				}
			}

			resio[n] = sol;
		}
		else sol = resio[n];

		printf("Case #%ld: %ld\n", test, sol);
	}
	return 0;
}
