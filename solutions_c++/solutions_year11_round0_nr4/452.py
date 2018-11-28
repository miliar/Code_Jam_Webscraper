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


#define maxn 1005

int N = 1000;

double e[maxn];

void init()
{
	e[1] = 0;
	for (int n = 2; n <= N; n++)
	{
		double t = e[n-1] + 1;
		for (int i = 2; i < n; i++) t += 1 + e[i] + e[n-i];
		e[n] = t / (n - 1);
	}
	//for (int i = 1; i <= 10; i++) printf("%.5lf\n", e[i]);
}

bool f[maxn];
int a[maxn];
int n;

void solvecase()
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
	for (int i = 1; i <= n; i++) f[i] = false;
	double res = 0;
	for (int i = 1; i <= n; i++) if (!f[i])
	{
		int len = 0, t = i;
		while (!f[t])
		{
			f[t] = true;
			len++;
			t = a[t];
		}
		if (len > 1) res += e[len] + 1;
	}
	printf("%.7lf", res);
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