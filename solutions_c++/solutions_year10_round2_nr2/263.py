#include <stdio.h>

void solve()
{
	static int P[50], V[50];
	int n, k, b, t, c = 0, w = 0;
	scanf("%d %d %d %d", &n, &k, &b, &t);
	for (int i = 0; i < n; i++)
		scanf("%d", &P[i]);
	for (int i = 0; i < n; i++)
		scanf("%d", &V[i]);
	for (int i = n - 1; k > 0 && i >= 0; i--)
		if (b - P[i] > V[i] * t)
			c++;
		else
		{
			k--;
			w += c;
		}
	if (k == 0)
		printf("%d\n", w);
	else
		puts("IMPOSSIBLE");
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