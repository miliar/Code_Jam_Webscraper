#include <algorithm>
#include <stdio.h>

#define MAX 10010

using namespace std;

int testCases;
int nr[MAX];

int main()
{
	freopen("c-small.in", "r", stdin);
	freopen("c-small.out", "w", stdout);

	int t = 0;
	for (scanf("%d", &testCases); testCases; testCases--)
	{
		t++;
		printf("Case #%d: ", t);

		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);

		for (int i = 1; i <= n; i++)
			scanf("%d", &nr[i]);

		int sol = 0;
		for (int r = h; r >= l; r--)
		{
			int ok = 1;
			for (int i = 1; i <= n; i++)
				if (nr[i] % r != 0 && r % nr[i] != 0)
					ok = 0;

			if (ok)
				sol = r;
		}

		if (!sol)
			printf("NO\n");
		else printf("%d\n", sol);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
