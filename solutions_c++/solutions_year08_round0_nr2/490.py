//* Problem  : Train Timetable
//* Date     : 2008.07.17
//* Author   : alt
//* Language : C++
//* Compiler : Microsoft Visual C++ 8.0

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <map>
#include <string>

using namespace std;

#define int64 long long
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define SZ(a) (int)a.size()
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define INF 1000*1000*1000
#define ALL(a) a.begin(), a.end()

#define int64 long long

struct train{
	int start, end, used, type;
}a[256];

int it, nt, res[2], n, na, nb, T;

int cmp_f(const void *a, const void *b)
{
	int k = ((train*)a)->start - ((train*)b)->start;
	if (k) return k;
	return ((train*)a)->end - ((train*)b)->end;
}

void solve()
{
	res[0] = res[1] = 0;
	qsort(a, n, sizeof(a[0]), cmp_f);
	for (int k = 0; k < n; k++)
		if (!a[k].used)
		{
			int t = a[k].end + T;
			int type = a[k].type;
			res[type]++;
			for (int i = k + 1; i < n; i++)
				if (!a[i].used && a[i].type != type && a[i].start >= t)
				{
					t = a[i].end + T;
					a[i].used = 1;
					type ^= 1;
				}
		}
}

void result()
{
	printf("Case #%d: %d %d\n", it, res[0], res[1]);
}

char s[100];

int to_time()
{
	s[2] = ' ';
	int h, m; sscanf(s, "%d %d", &h, &m);
	return h * 60 + m;
}

int main()
{
#ifdef _DEBUG
	freopen("1064", "r", stdin);
	freopen("B-small0.out", "w", stdout);	
#endif
	gets(s); sscanf(s, "%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		memset(a, 0, sizeof(a));
		scanf("%d%d%d", &T, &na, &nb);
		FOR(i, na)
		{
			scanf("%s", s); a[i].start = to_time();
			scanf("%s", s); a[i].end = to_time();
		}
		for (int i = na; i < na + nb; i++)
		{
			scanf("%s", s); a[i].start = to_time();
			scanf("%s", s); a[i].end = to_time();
			a[i].type = 1;
		}
		n = na + nb;
		solve();
		result();
	}
	return 0;
}

