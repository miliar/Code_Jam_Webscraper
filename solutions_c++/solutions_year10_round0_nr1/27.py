
#include <stdlib.h>
#include <stdio.h>

int main()
{
	int t, n, k;
	scanf("%d", &t);

	for (int c = 1; c <= t; c++)
	{
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", c);
		printf((k+1) % (1 << n) == 0 ? "ON\n" : "OFF\n");
	}
}
