#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

int prime[1<<20];

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	ll x;
	int ans = 0;
	scanf("%lld", &x);
	for(ll i = 1; i * i <= x; i++)
	{
		if (!prime[i])
			continue;
		int cur = 0;
		ll temp = x;
		while(temp >= i)
		{
			temp /= i;
			cur++;
		}
		ans += cur - 1;
	}
	printf("%d\n", ans + (x != 1));
}



int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 2; i < (1<<20); i++)
		prime[i] = 1;
	for(int i = 2; i < (1<<20); i++)
	{
		if (prime[i])
			for(int j = 2 * i; j < (1<<20); j += i)
				prime[j] = 0;
	}

	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
