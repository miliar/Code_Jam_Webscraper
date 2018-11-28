#include <stdio.h>
#include <string.h>
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, n, k, tcnt = 1, i, pow2[50];
	pow2[0] = 1;
	for (i = 1; i <= 31; i++)
		pow2[i] = pow2[i - 1] * 2;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d%d", &n, &k);
		if (k % pow2[n] == pow2[n] - 1)
			printf("Case #%d: ON\n", tcnt);
		else
			printf("Case #%d: OFF\n", tcnt);
		tcnt++;
	}
	return 0;
}
