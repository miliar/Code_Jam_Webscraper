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

int cnt[11000];
int a[11000];
int last[11000];
int n;

void dec(int * a, int l, int r)
{
	for (int i = l; i <= r; ++i)
		--a[i];
}

bool solve(int minL)
{
	memcpy(a, cnt, sizeof(a));
	clr(last);

	int i = 1;
	while (i <= 10000)
	{
		if (a[i])
		{
			int j = 1;
			while (j < minL && a[i + j] != 0)
				++j;
			if (j == minL)
			{
				last[i + j - 1]++;
				dec(a, i, i + j - 1);
			}
			else
			{
				if (last[i - 1])
				{
					--last[i - 1];
					++last[i + j - 1];
					dec(a, i, i + j - 1);
				}
				else
					return false;
			}
		}
		else
			++i;
	}
	return true;
}

int main()
{
#ifdef DBG1
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		scanf("%d", &n);
		clr(cnt);
		for (int i = 0; i < n; ++i)
		{
			int a;
			scanf("%d", &a);
			cnt[a]++;
		}

		int left = 0;
		int right = n;
		while (left < right)
		{
			int q = (left + right + 1) / 2;
			if (solve(q))
				left = q;
			else
				right = q - 1;
		}

		printf("Case #%d: %d\n", ii, left);
	}

	return 0;
}
