#include <stdio.h>
#include <algorithm>
using namespace std;
int a[1000];
int main()
{
	int ncase;
	int pcase;
	long long total;
	int p, k, l;
	bool ok;
	int i, j, t;
	scanf("%d", &ncase);
	for (pcase = 1; pcase <= ncase; pcase++)
	{
		ok = true;
		scanf("%d %d %d", &p, &k, &l);
		for (i = 0; i < l; i++)
			scanf("%d", &a[i]);
		sort(a, a + l);
		total = 0;
		if (p * k < l)
		{
			ok = false;
		}else
		{
			t = l - 1;
			for (i = 1; i <= p; i++)
			{
				for (j = 0; j < k; j++)
				{
					if (t < 0) goto lout;
					total += a[t] * i;
					t--;
				}
			}

		}
lout:
		printf("Case #%d: ", pcase);
		if (ok)
		{
			printf("%lld\n", total);
		}else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}
