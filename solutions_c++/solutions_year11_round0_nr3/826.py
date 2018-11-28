#include <stdio.h>
#include <algorithm>

void solve()
{
	int n, c, s = 0, x = 0, m = 9000000;
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d", &c);
		m = std::min(m, c);
		s += c;
		x ^= c;
	}
	if (x == 0)
	{
		printf("%d\n", s - m);
	}
	else
		puts("NO");

}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}