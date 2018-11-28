#include<stdio.h>

int main()
{
	int tc, n, k;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", t);
		int mask = (1 << n) - 1;
		puts(((k & mask) == mask) ? "ON" : "OFF");
	}
	return 0;
}
