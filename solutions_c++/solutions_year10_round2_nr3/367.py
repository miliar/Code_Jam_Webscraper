#include <cstdio>
// from http://www.research.att.com/~njas/sequences/A007059
int table[] = {0, 1, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 140268, 268066, 513350, 984911, 1892875, 3643570, 7023562, 13557020, 26200182, 50691978, 98182666, 190353370, 369393466, 717457656};

int main()
{
	int T;
	scanf("%d", &T);
	for (int idx = 1; idx <= T; ++idx)
	{
		printf("Case #%d: ", idx);
		int n;
		scanf("%d", &n);
		printf("%d\n", table[n] % 100003);
	}
	return 0;
}