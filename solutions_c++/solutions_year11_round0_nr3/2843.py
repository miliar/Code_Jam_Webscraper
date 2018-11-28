#include <stdio.h>

int main()
{
	int m, n, d, k, T, TT, sum;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d", &n);
		m = 0;
		k = 0x7ffffff;
		sum = 0;
		while (n--)
		{
			scanf("%d", &d);
			if (d < k) k = d;
			sum += d;
			m ^= d;
		}
		printf("Case #%d: ", T);
		if (m) puts("NO"); else printf("%d\n", sum-k);
	}
	return 0;
}
