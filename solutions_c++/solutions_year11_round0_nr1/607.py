#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <cstdlib>
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
	int last[2], pos[2], time = 0;
	clr(last); clr(pos);
	int n;
	scanf("%d", &n);
	char buf[4]; int d, num;
	for(int i = 0; i < n; i++)
	{
		scanf("%s%d", buf, &d);
		d--;
		num = (buf[0] == 'O');
		time += std::max(0, abs(pos[num] - d) - (time - last[num])) + 1;
		last[num] = time;
		pos[num] = d;
	}
	printf("%d\n", time);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
