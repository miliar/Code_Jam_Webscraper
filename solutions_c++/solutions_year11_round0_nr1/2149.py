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


int sign(int x)
{
	if (x > 0)
		return 1;
	if (x < 0)
		return -1;
	return 0;
}

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
		vector <pii> button[2];
		for (int i = 0; i < n; ++i)
		{
			char ch[2];
			int num;
			scanf("%s %d", ch, &num);
			if (ch[0] == 'O')
				button[0].push_back(pii(num, i));
			else if (ch[0] == 'B')
				button[1].push_back(pii(num, i));
			else
				throw 42;
		}
		button[0].push_back(pii(1, n));
		button[1].push_back(pii(1, n));

		int pos[2] = {1, 1};
		int cur = 0;
		int j1 = 0, j2 = 0;
		int i1 = 0, i2 = 1;
		int _time = 0;
		while (cur < n)
		{
			if (button[i1][j1].second != cur)
			{
				swap(i1, i2);
				swap(j1, j2);
			}

			pos[i2] += sign(button[i2][j2].first - pos[i2]);
			if (pos[i1] == button[i1][j1].first)
			{
				++j1;
				++cur;
			}
			else
				pos[i1] += sign(button[i1][j1].first - pos[i1]);

			++_time;
		}

		printf("Case #%d: %d\n", ii + 1, _time);
	}

	return 0;
}
