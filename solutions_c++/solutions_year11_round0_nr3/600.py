#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
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


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int sum = 0, ans = 0, min = 1e9, n, d;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &d);
		min = std::min(min, d);
		ans += d;
		sum ^= d;
	}
	if (sum != 0)
		printf("NO\n");
	else
		printf("%d\n", ans - min);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
