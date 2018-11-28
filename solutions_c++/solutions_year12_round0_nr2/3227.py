#include <iostream>
#include <cstdio>

using namespace std;

int
main()
{
	int T, N, S, p;
	int ok_sup, best;
	int tab[100];

	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		cin >> N;
		cin >> S;		
		cin >> p;
		for (int j = 0; j < N; ++j)
		{
			cin >> tab[j];
		}

		ok_sup = 0;
		best = 0;
		for (int j = 0; j < N; ++j)
		{
			int mod = tab[j] % 3;
			int div = tab[j] / 3;

			if (div == 0)
			{
				switch (mod)
				{
					case 0:
						if (0 >= p)
						{
							++best;
						}
						break;
					case 1:
						if (1 >= p)
						{
							++best;
						}
						break;
					case 2:
						if (2 >= p)
						{
							if (1 < p)
								++ok_sup;
							++best;
						}
						break;
				}
			}
			else
			{
				switch (mod)
				{
					case 0:
						if (div + 1 >= p)
						{
							if (div < p)
								++ok_sup;
							++best;
						}
						break;
					case 1:
						if (div + 1 >= p)
						{
							++best;
						}
						break;
					case 2:
						if (div + 2 >= p)
						{
							if (div + 1 < p)
								++ok_sup;
							++best;
						}
						break;
				}
			}
		}

		if (S - ok_sup < 0)
			best = best - (ok_sup - S);

		printf("Case #%d: %d\n", i + 1, best);
	}

	return 0;
}
