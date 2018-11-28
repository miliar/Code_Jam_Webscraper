#include <stdio.h>
int TWO[25];
int main()
{
	int cases;
	scanf("%d", &cases);
	for (int k = 1; k <= cases; ++k)
	{
		printf("Case #%d: ", k);
		long long c, p, l;
		scanf("%lld%lld%lld", &l, &p, &c);
		int ccount = 0;
		do
		{
			l = l * c;
			++ccount;
		}
		while (l < p);
		--ccount;
		TWO[0] = 1;
		for (int i = 1; i < 25; ++i) TWO[i] = TWO[i - 1] * 2;
		for (int i = 0; i < 25; ++i)
			if (TWO[i] > ccount) { printf("%d\n", i); break;}
	}
	return 0;
}
