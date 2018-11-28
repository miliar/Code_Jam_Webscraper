#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
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

const int size = 100000;
ll ar[100];

ll maxlen;

class dst
{
public:
	ll count;
	ll length;
	dst (int cnt = 0, int len = 0)
	{
		count = cnt;
		length = len;
	}
	bool operator < (const dst &d) const
	{
		return (count - d.count)*maxlen < length - d.length;
	}
} d[size];

bool use[size];

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	memset(d, -1, sizeof(d));
	clr(use);
	d[0] = dst(0,0);
	int n;
	ll l;
	scanf("%lld%d", &l, &n);
	for(int i = 0; i < n; i++)
	{
		scanf("%lld", &ar[i]);
	}
	std::sort(ar, ar+n);
	maxlen = ar[n-1];
	std::set<std::pair<dst, int> > heap;
	heap.insert(std::make_pair(d[0], 0));
	while(!heap.empty())
	{
		int first = heap.begin()->second;
//		dbg("first: %d\n", first);
		heap.erase(heap.begin());
		if(use[first])
			continue;
		use[first] = 1;
		for(int i = 0; i < n - 1; i++)
		{
			dst nd = dst(d[first].count + 1, d[first].length + ar[i]);
			int ni = (first + ar[i]) % maxlen;
			if (nd < d[ni] || d[ni].count == -1)
			{
				d[ni] = nd;
				heap.insert(std::make_pair(nd, ni));
			}
		}
	}
//	dbg("ans: %lld %lld\n", d[l % maxlen].count, d[l % maxlen].length);
	if (d[l % maxlen].count == -1)
	{
		printf("IMPOSSIBLE\n");
	}
	else
	{
		printf("%lld\n", (l - d[l % maxlen].length) / maxlen + d[l % maxlen].count);
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
