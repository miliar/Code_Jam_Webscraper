#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <cmath>
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

char s[128];

int qq;

bool is_sq(ll x)
{
	ll e = (ll) sqrt((double) x);
	for(int i = -50; i <= 50; i++)
		if ((e+i)*(e+i) == x)
			return true;
	return false;
}

void print (int x)
{
	for(int i = 0; s[i]; i++)
		if (s[i] == '?')
		{
			s[i] = x % 2 + '0';
			x /= 2;
		}
	printf("%s\n", s);
}

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	qq = 0;
	scanf("%s", s);
	for(int i = 0; s[i]; i++)
		if (s[i] == '?')
			qq++;
	for(int i = 0; i < (1<<qq); i++)
	{
		ll x = 0;
		int m = i;
		for(int j = 0; s[j]; j++)
			if (s[j] != '?')
				x = 2*x + s[j] - '0';
			else
			{
				x = 2*x + m % 2;
				m /= 2;
			}
		if (is_sq(x))
		{
			print(i);
			return;
		}
	}

	throw 42;
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
