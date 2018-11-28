#include <stdio.h>
#include <math.h>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	long long dec;
	int test, n, k, res, cs=1;

	scanf("%d", &test);

	while(test--)
	{
		scanf("%d %d", &n, &k);

		dec = (long long)pow(2.0, (double)n) - 1;

		res = k%(dec+1);

		if(res==dec)
			printf("Case #%d: ON\n", cs++);
		else
			printf("Case #%d: OFF\n", cs++);

	}
	return 0;
}
