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


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n, d, ans = 0;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &d);
		if (d != i + 1)
			ans++;
	}
	printf("%d\n", ans);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
