#include <cstdio>
#include <algorithm>
using namespace std;

int t, n;
int a[1010];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("outputlarge.txt", "w", stdout);

	int asum, axor, amin;
	int i, j;

	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%d", &n);
		asum = axor = 0;
		amin = 1000000;
		for (j = 0; j < n; ++j)
		{
			scanf("%d", &a[j]);
			asum += a[j];
			axor = axor ^ a[j];
			amin = min(amin, a[j]);
		}
		printf("Case #%d: ", i);
		if (axor == 0)
			printf("%d\n", asum - amin);
		else
			printf("NO\n");
	}
	return 0;
}