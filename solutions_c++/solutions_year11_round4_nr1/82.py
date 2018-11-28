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

int x, s, r, t, n;

void solvecase()
{
	scanf("%d%d%d", &x, &s, &r);
	scanf("%d%d", &t, &n);
	int len = x;
	vector<pair<int, int> > segs;
	fo(i, n)
	{
		int b, e, w;
		scanf("%d%d%d", &b, &e, &w);
		len -= e - b;
		segs.PB(MP(w, e - b));
	}
	if (len > 0) segs.PB(MP(0, len));
	sort(ALL(segs));
	double res = 0;
	double runtime = t;
	fo(i, segs.size())
	{
		double seglen = segs[i].second;
		double segvel = segs[i].first;
		double tmp = seglen / (segvel + r);
		if (runtime >= tmp)
		{
			runtime -= tmp;
			res += tmp;
		}
		else
		{
			double runlen = runtime * (r + segvel);
			res += runtime;
			runtime = 0;
			seglen -= runlen;
			res += seglen / (segvel + s);			
		}
	}
	printf("%.8le", res);
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

#define problem_letter "A"
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