#include <cstdio>

#define MAXN 40

using namespace std;

int main()
{
	int testcases;
	scanf("%d", &testcases);
	for (int idxCase = 0; idxCase < testcases; ++idxCase)
	{
		int n;
		scanf("%d", &n);
		int a[MAXN];
		for (int i = 0; i < n; ++i)
		{
			char line[MAXN + 1];
			scanf("%s", line);
			int lastone;
			for (lastone = n - 1; lastone > 0 && line[lastone] == '0'; --lastone)
				;
			a[i] = lastone;
		}
		int cost = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = i; ; ++j)
			{
				if (j == n)
				{
					fprintf(stderr, "Impossible\n");
					return 1;
				}
				if (a[j] <= i)
				{
					cost += j - i;
					for (; j > i; --j)
						a[j] = a[j - 1];
					break;
				}
			}
		}
		printf("Case #%d: %d\n", idxCase + 1, cost);
	}
	return 0;
}
