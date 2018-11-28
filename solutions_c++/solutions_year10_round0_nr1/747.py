#include <stdio.h>

void solve()
{
	int n, k;
	scanf("%d %d", &n, &k);
	puts(~k & ((1 << n) - 1) ? "OFF" : "ON");
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}