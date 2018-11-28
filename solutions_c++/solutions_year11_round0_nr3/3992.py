#include <iostream>

using namespace std;

int min(int a, int b)
{
	if (a < b)
	{
		return a;
	}
	else
	{
		return b;
	}
}

int n,t,x;

int main()
{
	scanf("%d", &t);

	freopen("candyout.txt", "wt", stdout);

	for (int j = 1; j <= t; j++)
	{
		scanf("%d", &n);

		int m = 10000000;
		int sum = 0;
		int S = 0;

		for (int i = 0; i < n; i++)
		{
			scanf("%d", &x);

			sum ^= x;
			S += x;

			m = min(m,x);
		}

		printf("Case #%d: ", j);

		if (sum == 0)
		{
			printf("%d\n", S-m);
		}
		else
		{
			printf("NO\n");
		}
	}

	return 0;
}