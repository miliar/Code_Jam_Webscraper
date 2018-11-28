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

#define maxn 555

double d;

int a[maxn], w[maxn];
int n;

vector<int> vendors;

bool check(double dist)
{
	double last = -1e30;
	fo(i, vendors.size())
	{
		double x = max(last + d, vendors[i] - dist);
		if (x > vendors[i] + dist) return false;
		last = x;
	}
	return true;
}

void solvecase()
{
	scanf("%d%lf", &n, &d);
	vendors.clear();
	fo(i, n)
	{
		scanf("%d%d", &a[i], &w[i]);
		fo(j, w[i]) vendors.push_back(a[i]);
	}
	//check(0.9);
	//check(1.1);
	double l = 0, r = 1e13;
	fo(it, 100)
	{
		double mid = (l + r) / 2;
		if (check(mid))
			r = mid;
		else
			l = mid;
	}
	printf("%.7lf", r);
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