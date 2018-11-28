#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>


#define clr(a) memset(a, 0, sizeof(a))

typedef std::pair<int, int> pii;
typedef long long ll;

void dbg(const char * fmt, ...)
{
	#if 1
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
		fflush(stdout);
	#endif
}


int len(int x)
{
	int ans = 0;
	while(x)
	{
		ans++;
		x /= 10;
	}
	return ans;
}


int ans[2000002];

void solve(int test_num)
{
	printf("Case #%d: ", test_num);
	int a, b;
	scanf("%d%d", &a, &b);
	int l = len(a);
	int p = 1;
	for(int i = 0; i < l-1; i++)
		p *= 10;
	clr(ans);
	for(int i = a; i <= b; i++)
	{
		int m = i;
		int x = i;
		for(int j = 0; j < l; j++)
		{
			x = x / 10 + x % 10 * p;
			m = std::min(m, x);
		}
		ans[m]++;
	}
	long long sum = 0;
	for(int i = 0; i <= b; i++)
		sum += ans[i] * (ans[i] - 1);
	sum /= 2;
	printf("%lld\n", sum);
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++)
		solve(i+1);


	return 0;
}
