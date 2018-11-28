#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#define clr(a) memset(a, 0, sizeof(a))

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
typedef long long ll;

int next[1000];
ll cost[1000];
ll size[1000];

void solve(int test_case)
{
	ll r, k;
	int n;
	scanf("%lld%lld%d", &r, &k, &n);
	ll sum = 0;
	ll ans = 0;
	for(int i = 0; i < n; i++)
	{
		scanf("%lld", &size[i]);
		sum += size[i];
	}
	if (sum <= k)
	{
		ans = sum * r;
	}
	else
	{
		for(int i = 0; i < n; i++)
		{
			sum = 0;
			int j;
			for(j = i;; j = (j + 1) % n)
			{
				if (sum + size[j] <= k)
					sum += size[j];
				else
					break;
			}
			next[i] = j;
			cost[i] = sum;
		}
		int cur = 0;
		for(int i = 0; i < r; i++)
		{
			ans += cost[cur];
			cur = next[cur];
		}
	}


	printf("Case #%d: %lld\n", test_case, ans);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
