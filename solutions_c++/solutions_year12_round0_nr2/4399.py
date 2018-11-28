#include <iostream>

const int MAX = 100;

int main()
{
	int t;
	scanf("%d", &t);

	int points[MAX];
	int caseNum = 1;
	while (t-- > 0)
	{
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);

		int tempS = s;
		int result = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", points + i);

			int x = points[i] / 3;
			int r = points[i] % 3;
			if (r == 0)
			{
				if (x >= p)
					++result;
				else if (tempS > 0 && x + 1 >= p && x - 1 >= 0)
				{
					++result;
					--tempS;
				}
			}
			else if (r == 1)
			{
				if (x + 1 >= p)
					++result;
			}
			else if (r == 2)
			{
				if (x + 1 >= p)
					++result;
				else if (tempS > 0 && x + 2 >= p)
				{
					++result;
					--tempS;
				}
			}
		}

		printf("Case #%d: %d\n", caseNum++, result);
	}

	return 0;
}