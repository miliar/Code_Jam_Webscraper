
#include <stdio.h>

int getPow(int n)
{
	int pow = 1;

	while (n--)
	{
		pow *= 2;
	}

	return pow;
}

int main()
{
	int t, n, k, ca = 1;

	freopen("d:\\2.in", "r", stdin);
	freopen("d:\\A-large.out", "w", stdout);

	scanf("%d", &t);

	while (t--)
	{
		scanf("%d %d", &n, &k);

		int tmp = getPow(n);
		k -= (tmp-1);

		printf("Case #%d: ", ca++);
	
		if (k%tmp)
			printf("OFF\n");
		else
			printf("ON\n");
			
	}

	return 0;
}