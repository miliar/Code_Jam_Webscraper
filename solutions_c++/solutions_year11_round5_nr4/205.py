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

bool ok;
char s[1000];

void brute(ll cur, int idx, ll pow2)
{
	if (ok)
		return;

	if (idx == -1)
	{
		ll p = (ll)sqrt(cur + 0.0);
//		dbg("%lld\n", cur);
		if (cur == p * p)
			ok = true;
		return ;
	}
	if (s[idx] == '0')
		brute(cur, idx - 1, pow2 * 2);
	else if (s[idx] == '1')
		brute(cur + pow2, idx - 1, pow2 * 2);
	else
	{
		s[idx] = '0';
		brute(cur, idx - 1, pow2 * 2);
		if (ok)
			return ;
		s[idx] = '1';
		brute(cur + pow2, idx - 1, pow2 * 2);
		if (ok)
			return;
		s[idx] = '?';
	}
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
		scanf("%s", s);
		ok = false;
		brute(0, strlen(s) - 1, 1);
		printf("Case #%d: %s\n", ii, s);
	}

	return 0;
}
