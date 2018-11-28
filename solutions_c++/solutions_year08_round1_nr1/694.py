#include <stdio.h>
#include <algorithm>
using namespace std;
int a[800], b[800];
int main()
{
	int ncase;
	scanf("%d\n", &ncase);
	int pcase;
	int n;
	int i;
	long long total;
	for (pcase = 1; pcase <= ncase; pcase++)
	{
		scanf("%d\n", &n);
		for (i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
		}
		for (i = 0; i < n; i++)
		{
			scanf("%d", &b[i]);
		}
		sort(a, a + n);
		sort(b, b + n);
		total = 0;
		for (i = 0; i < n; i++)
		{
			total += a[i] * b[n - i - 1];
		}
		printf("Case #%d: %d\n", pcase, total);
	}
	return 0;
}
