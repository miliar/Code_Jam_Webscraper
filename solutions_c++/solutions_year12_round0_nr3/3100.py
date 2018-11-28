#include <stdio.h>
#include <math.h>
struct Pair
{
	int a, b;
} pair[2000000];
bool cmp(Pair arg1, Pair arg2) { return arg1.a != arg2.a ? arg1.a < arg2.a : arg1.b < arg2.b; }
int main()
{
	int t, a, b, l, l2, n, m, i, ans, idx, cnt;
	int pow[8];

	pow[0] = 1;
	for (i = 1; i < 8; i++)
		pow[i] = pow[i-1] * 10;

	cnt = 1;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d %d", &a, &b);
		idx = 0;
		for (n = a; n <= b; n++)
		{
			l = (int)ceil(log10(n+1));
			for (i = 1; i < l; i++)
			{
				m = (n % pow[i]) * pow[l-i] + n / pow[i];
				l2 = (int)ceil(log10(m+1));
				if (m <= b && l == l2 && n < m)
				{
					pair[idx].a = n;
					pair[idx++].b = m;
				}
			}
			
		}
		ans = idx > 0 ? 1 : 0;
		for (i = 1; i < idx; i++)
			if (pair[i-1].a != pair[i].a || pair[i-1].b != pair[i].b)
				ans++;
		printf("Case #%d: %d\n", cnt++, ans);
	}
	return 0;
}
