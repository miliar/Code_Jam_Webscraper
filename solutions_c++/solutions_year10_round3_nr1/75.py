#include <algorithm>
#include <stdio.h>

using namespace std;

int n;
int x1[1024], x2[1024];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int testCases, t = 1;
	for (scanf("%d", &testCases); testCases; t++, testCases--)
	{
		scanf("%d", &n);

		int sol = 0;
		for (int i = 1; i <= n; i++)
		{
			scanf("%d %d", &x1[i], &x2[i]);

			for (int j = 1; j < i; j++)
				if ((x1[i] < x1[j] && x2[i] > x2[j]) || (x1[i] > x1[j] && x2[i] < x2[j]))
					sol++;
		}

		printf("Case #%d: %d\n", t, sol);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
