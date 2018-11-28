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

char s[1000];

int n, k;
LL w[100];

inline bool check(LL x, LL y) // x *x < y
{
	if (y / x < x - 1) return false;
	return x * x < y;
}

bool check(LL x)
{
	LL l = 0, r = x;
	while (l + 1 < r)
	{
		LL m = (l + r) / 2;
		if (check(m, x)) l = m; else r = m;
	}
	return r * r == x;
}

void solvecase()
{
	scanf("%s", s);
	n = strlen(s);
	k = 0;
	LL base = 0;
	fo(i, n) if (s[i] == '?') 
	{		
		w[k] = 1ll << (n - i - 1);
		k++;
	}
	else
	{
		if (s[i] == '1') base += 1ll << (n - i - 1);
	}
	int K = 1<<k;
	fo(i, K)
	{
		LL x = base;
		fo(j, k) if (i & (1<<j)) x += w[j];
		if (check(x))
		{
			string res = "";
			fo(i, n)
			{
				if (x % 2) res += '1'; else res += '0';
				x /= 2;
			}
			reverse(ALL(res));
			printf("%s", res.c_str());
			return;
		}
	}
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

#define problem_letter "D"
//#define fname "test"
#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
//#define fname problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}