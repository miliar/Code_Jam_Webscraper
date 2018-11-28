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


int next[100500];
ll h[100500];
int d[100500];
std::vector<int> s;

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n - 1; i++)
	{
		scanf("%d", &next[i]);
		next[i]--;
	}
	s.clear();
	s.push_back(n-1);
	for(int i = n - 2; i >= 0; i--)	
	{
		while(!s.empty() && s.back() != next[i])
			s.pop_back();
		if (s.empty())
		{
			printf("Impossible\n");
			return;
		}
		else
			s.push_back(i);
	}
	d[n-1] = 0;
	h[n-1] = 1000000000;
	for(int i = n - 2; i >= 0; i--)
	{
		d[i] = d[next[i]] + 1;
		h[i] = h[next[i]] - d[i] - (d[i]) * (next[i] - i) * (d[i] - 1);
	}

	for(int i = 0; i < n; i++)
		printf("%lld ", h[i]);
	printf("\n");
	fflush(stdout);
	for(int i = 0; i < n - 1; i++)
	{
		if (h[i] < 0)
			throw 42;
		int t = next[i];
		for(int j = i + 1; j < n; j++)
		{
			if (j == t)
				continue;
			if ((h[j] - h[i]) * (t - i) >= (h[t] - h[i]) * (j - i))
			{
				dbg("%d %d %d\n", i + 1, j + 1, next[i] + 1);
				throw 42;
			}
		}
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
