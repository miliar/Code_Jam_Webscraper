#include <stdio.h>
#include <algorithm>
using namespace std;

struct St
{
	int k, pos;
	bool operator < (const St &s) const
	{
		return k < s.k;
	}
}a[1000];

int i, n, T, TT, sum;

int main()
{
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
		{
			scanf("%d", &a[i].k);
			a[i].pos = i;
		}
		sort(a, a + n);
		sum = 0;
		for (i = 0; i < n; ++i)
			sum += (i != a[i].pos);
		printf("Case #%d: %d.000000\n", T, sum);
	}
	return 0;
}
