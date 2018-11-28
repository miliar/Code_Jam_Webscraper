#include <algorithm>
#include <stdio.h>

#define MAX 16

using namespace std;

int s[MAX];

int main()
{
	freopen("c-small.in", "r", stdin);
	freopen("c-small.out", "w", stdout);

	int t = 0, testCases;
	for (scanf("%d", &testCases); testCases; testCases--)
	{
		t++;
		int n, sol = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &s[i]);

		for (int conf = 1; conf < (1 << n) - 1; conf++)
		{
			int sp = 0, ss = 0, p = 0;
			for (int i = 0; i < n; i++)
				if (conf & (1 << i))
				{
					sp ^= s[i];

					p += s[i];
				}
				else ss ^= s[i];

			if (sp == ss)
				sol = max(sol, p);
		}

		printf("Case #%d: ", t);
		if (!sol)
			printf("NO\n");
		else printf("%d\n", sol);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
