#include <stdio.h>

bool state[40];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int c, l, n, k;
	scanf("%d", &c);
	for (l = 1; l <= c; l++)
	{
		scanf("%d%d", &n, &k);
		if (((k+1)%(1<<n)) == 0)
			printf("Case #%d: ON\n", l);
		else
			printf("Case #%d: OFF\n", l);
	}
	return 0;
}
