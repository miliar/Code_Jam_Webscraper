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

int n;
#define maxn 1005

int a[maxn];
int t[maxn], open[maxn];

bool check(const vector<int> &v, int len)
{
	CLR(t, 0);
	CLR(open, 0);
	int n_open = 0;
	int n = v.size();
	fo(i, n) t[i] = v[i];
	fo(i, n)
	{
		n_open += open[i];
		if (t[i] > n_open)
		{
			while (t[i] > n_open)
			{
				fo(j, len)
				{
					if (t[i+j] == 0) return false;
					t[i+j]--;
				}
				open[i+len]++;
			}
		}
		n_open = min(n_open, t[i]);
	}
	return true;
}

int calc(const vector<int> &v)
{
	int l = 1, r = maxn;
	while (l + 1 < r)
	{
		int m = (l + r) / 2;
		if (check(v, m)) l = m; else r = m;
	}
	return l;
}

void solvecase()
{
	scanf("%d", &n);
	fo(i, n) scanf("%d", &a[i]);
	map<int, int> m;
	fo(i, n) m[a[i]]++;
	if (n == 0)
	{
		printf("0");
		return;
	}
	int res = maxn;
	vector<int> v;
	int last = -1;
	for (map<int, int>::iterator it = m.begin(); it != m.end(); it++)
	{
		if (!v.empty() && it->first != last + 1)
		{
			res = min(calc(v), res);
			v.clear();
		}
		v.push_back(it->second);
		last = it->first;
	}
	res = min(calc(v), res);
	printf("%d", res);
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