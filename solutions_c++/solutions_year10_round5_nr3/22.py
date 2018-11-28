#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <vector>
#include <algorithm>
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

const int size = 1e7;
int ar[size];
const int shift = 2000000;

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	clr(ar);
	int n;
	scanf("%d", &n);
	ll ans = 0;
	for(int i = 0; i < n; i++)
	{
		int a,b;
		scanf("%d%d", &a, &b);
		ar[a + shift] = b;
	}
	int last = 0;
//	dbg("\n");
	for(int i = 1; i < size; i++)
	{
		if (ar[i] == 0)
		{
			ar[i] = -last;
			last = i;
		}
		else if (ar[i] == 1)
			continue;
		else
		{
			int prevlast = -ar[last];
			while(ar[i] > 1)
			{
//				dbg("i: %d, ar[i]: %d, last :%d\n", i, ar[i], last);

//				for(int j = shift - 5; j <= shift + 5; j++)
//					dbg("%9d ", ar[j]);
//				dbg("\n");
				ans += i - last;
				ar[last] = 1;
				last++;
				if (i != last)
				{
					ar[last] = -prevlast;
					ar[i]++;
				}
				else
				{
					last = prevlast;
					prevlast = -ar[last];
				}
				ar[i] -= 2;
				ar[i+1] ++;
			}			
			if (ar[i] == 0)
			{
				ar[i] = -last;
				last = i;
			}
		}
	}
	printf("%lld\n", ans);

}



int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
