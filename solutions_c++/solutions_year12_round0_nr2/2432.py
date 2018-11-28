#include <cstdio>
#include <iostream>
#include <string>

using namespace std;


int main()
{
	int i, j, t, n, s, p, x;


	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int cur = 1; cur <= t; cur++)
	{
		cin >> n >> s >> p;
		int best = 0;
		for(i = 0; i < n; i++)
		{
			cin >> x;
			if (x < 2 || x > 28)
			{
				best += ((x + 2) / 3) >= p;
				continue;
			}
			if (x % 3 == 0)
			{
				if (x / 3 >= p)
					++best;
				else
				if (s > 0 && x / 3 + 1 >= p)
				{
					--s;
					++best;
				}
			}
			if (x % 3 == 1)
			{
				best += (x / 3 + 1) >= p;
			}
			if (x % 3 == 2)
			{
				if (x / 3 + 1 >= p)
					++best;
				else
				if (s > 0 && x / 3 + 2 >= p)
				{
					--s;
					++best;
				}
			}
		}

		printf("Case #%d: %d\n", cur, best);
		
	}

	return 0;
}