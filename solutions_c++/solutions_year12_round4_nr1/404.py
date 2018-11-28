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

int far[100500];
ll dist[100500];
ll len[100500];


void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n;
	scanf("%d", &n);
	dist[0] = 0;
	for(int i = 1; i <= n; i++)
	{
		scanf("%lld%lld", &dist[i], &len[i]);
		far[i] = -1;
	};
	far[n+1] = -1;
	scanf("%lld", &dist[n+1]);
	far[1] = 0;
	for(int i = 1; i <= n; i++)
	{
		if (far[i] == -1)
			break;
		ll last = dist[i] + std::min(dist[i] - dist[far[i]], len[i]);
		for(int j = i + 1; j <= n + 1; j++)
			if (dist[j] <= last && far[j] == -1)
				far[j] = i;
	}
	printf("%s\n", far[n+1] == -1 ? "NO" : "YES");
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
