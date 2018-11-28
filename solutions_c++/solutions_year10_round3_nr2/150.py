#include <stdio.h>

int main(void)
{
	int t, test = 0, ans;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	long long a, b, c;
	scanf("%d", &t);
	while(t --)
	{
		scanf("%lld %lld %lld", &a, &b, &c);
		ans = 0;
		while(a * c < b)
		{
			c *= c;
			ans ++;
		}
		printf("Case #%d: %d\n", ++test, ans);
	}
	return 0;
}
