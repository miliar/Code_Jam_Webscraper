#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <cmath>

#include <cstdarg>

#pragma comment(linker,"/STACK:128000000")

#define DBG2 1

void dbg(const char * fmt, ...)
{
#ifdef DBG1
#if DBG2
	va_list args;
	va_start(args, fmt);
	vfprintf(stderr, fmt, args);
	va_end(args);
#endif
#endif
}

#ifdef DBG1
#define LL "%I64d"
#else
#define LL "%lld"
#endif


using namespace std;

#define clr(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))

#define TASKNAME ""

typedef long long ll;
typedef unsigned long long ull;

typedef pair<int,int> pii;

const int MAX = 500;

int cnt = 0;

bool a[MAX + 10][MAX + 10];

void set(bool & t, bool v)
{
	if (t)
		--cnt;
	t = v;
	if (t)
		++cnt;
}

int main()
{
	freopen(TASKNAME "input.txt", "r", stdin);
	freopen(TASKNAME "output.txt", "w", stdout);


#ifdef DBG1
#if DBG2

	freopen(TASKNAME ".err", "w", stderr);
#endif
#endif

	clr(a);

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		int k;
		scanf("%d", &k);
		cnt = 0;
		for (int i = 0; i < k; ++i)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
					set(a[x][y], 1);
		}

		int time = 0;
		while (cnt)
		{
/*			dbg("%d\n", cnt);
			for (int i = 0; i < 10; ++i)
			{
				for (int j = 0; j < 10; ++j)
					dbg("%d", int(a[i][j]));
				dbg("\n");
			}*/

			for (int i = MAX; i > 0; --i)
				for (int j = MAX; j > 0; --j)
					if (a[i][j])
					{
						if (!a[i - 1][j] && !a[i][j - 1])
							set(a[i][j], 0);
					}
					else
					{
						if (a[i - 1][j] && a[i][j - 1])
							set(a[i][j], 1);
					}
			++time;
		}

		printf("Case #%d: %d\n", ii, time);
		fflush(stdout);
	}

	return 0;
}