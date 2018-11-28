#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
#define LL long long
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }
#define fo(i, n) for (int i = 0; i < (n); i++)
#define foz(i, a) for (int i = 0; i < (a).size(); i++)

void init()
{
	
}

int c, d, n;
char buf[105];
char combs[256][256];
bool opps[256][256];
int res[105];
int have[256];

void solvecase()
{
	scanf("%d", &c);
	memset(combs, 0, sizeof(combs));
	fo(i, c)
	{
		scanf("%s", buf);
		combs[buf[0]][buf[1]] = buf[2];
		combs[buf[1]][buf[0]] = buf[2];
	}
	scanf("%d", &d);
	memset(opps, 0, sizeof(opps));
	fo(i, d)
	{
		scanf("%s", buf);
		opps[buf[0]][buf[1]] = true;
		opps[buf[1]][buf[0]] = true;
	}
	int cnt = 0;
	scanf("%d%s", &n, buf);
	memset(have, 0, sizeof(have));
	fo(i, n)
	{
		res[cnt++] = buf[i];
		have[buf[i]]++;
		char t = combs[res[cnt-1]][res[cnt-2]];
		if (cnt < 2) continue;
		if (t)
		{
			have[res[cnt-1]]--;
			have[res[cnt-2]]--;
			res[cnt-2] = t;
			cnt--;
		}
		else
		{
			// check if we need to clear everything
			for (char t = 'A'; t <= 'Z'; t++) if (opps[t][buf[i]] && have[t])
			{
				memset(have, 0, sizeof(have));
				cnt = 0;
				break;
			}
		}
	}
	printf("[");
	fo(i, cnt)
	{
		printf("%c", res[i]);
		if (i + 1 < cnt) printf(", ");
	}
	printf("]");
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
}

#define problem_letter "B"
//#define fname "test"
//#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
#define fname problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}