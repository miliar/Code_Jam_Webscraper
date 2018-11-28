#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
	freopen("c-small.in", "r", stdin);
	freopen("c-small.out", "w", stdout);

	int t = 1, testCases;
	for (scanf("%d", &testCases); t <= testCases; t++)
	{
		printf("Case #%d: ", t);

		int a, b;
		scanf("%d %d", &a, &b);
		if (a == 1000)
		{
			printf("0\n");

			continue;
		}

		int sol = 0;
		for (int n = a; n <= b; n++)
			for (int m = n + 1; m <= b; m++)
			{
				if (n >= 100)
				{
					if (10 * (n % 100) + (n / 100) == m)
						sol++;
					else if (100 * (n % 10) + (n / 10) == m)
						sol++;
				}
				else if (n >= 10)
				{
					if (10 * (n % 10) + (n / 10) == m)
						sol++;
				}
			}

		printf("%d\n", sol);
	}

	return 0;
}
