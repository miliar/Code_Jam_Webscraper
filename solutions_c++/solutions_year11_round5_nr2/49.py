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


int count[11000];
int start[10000], end[10000];

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	clr(count);
	int n;
	scanf("%d", &n);
	int s = 0, e = 0;
	for(int i = 0; i < n; i++)
	{
		int d;
		scanf("%d", &d);
		count[d] ++;
	}
	for(int i = 1; i <= 10001; i++)
	{
		for(int x = count[i-1]; x < count[i]; x++)
			start[s++] = i;
		for(int x = count[i]; x < count[i-1]; x++)
			end[e++] = i;
	}
	if (s != e)
		throw 42;
	int ans = n;
	for(int i = 0; i < s; i++)
		ans = std::min(ans, end[i] - start[i]);
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
