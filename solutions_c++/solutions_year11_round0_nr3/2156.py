#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#include <cstdarg>

using namespace std;

#define DBG2 1

#define clr(a) memset(a, 0, sizeof(a))
#define fill(a, b) memset(a, b, sizeof(a))

void dbg(char * fmt, ...)
{
#ifdef DBG1
#if	DBG2
	FILE * file = stdout;

	va_list args;
	va_start(args, fmt);
	vfprintf(file, fmt, args);
	va_end(args);

	fflush(file);
#endif
#endif
}

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> pii;

const int INF = 1 << 30;

int main()
{
#ifdef DBG1
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 0; ii < tt; ++ii)
	{
		int n;
		scanf("%d", &n);
		int _xor = 0;
		int _sum = 0;
		int _min = INF;
		for (int i = 0; i < n; ++i)
		{
			int a;
			scanf("%d", &a);
			_sum += a;
			_xor ^= a;
			_min = min(_min, a);
		}

		printf("Case #%d: ", ii + 1);
		if (_xor != 0)
			printf("NO\n");
		else
			printf("%d\n", _sum - _min);
	}

	return 0;
}
