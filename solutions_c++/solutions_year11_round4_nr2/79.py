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

#define maxn 505

int a[maxn][maxn];
int xm[maxn][maxn], ym[maxn][maxn];
int w[maxn];

int res;
int n, m, d;
char s[maxn];

void solvecase()
{
	res = -1;
	scanf("%d%d%d", &n, &m, &d);
	fo(i, n) {
		scanf("%s", s);
		fo(j, m)
			a[i][j] = s[j] - '0';
	}
	for (int k = 3; k <= min(n, m); k++)
	{
		// calc w
		if (k % 2 == 1)
		{
			fo(i, k) w[i] = i - k/2;
		}
		else
		{
			fo(i, k) w[i] = 2 * i - (k-1);
		}
		// calc x
		for (int i = 0; i < n; i++)
		{			
			for (int j = 0; j + k <= m; j++)
			{
				xm[i][j] = 0;
				fo(t, k) xm[i][j] += w[t] * a[i][j+t];
			}
		}
		// calc y
		for (int i = 0; i + k <= n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				ym[i][j] = 0;
				fo(t, k) ym[i][j] += w[t] * a[i+t][j];
			}
		}
		// test
		for (int i = 0; i + k <= n; i++)
		{
			for (int j = 0; j + k <= m; j++)
			{
				LL x = 0, y = 0;
				fo(t, k) x += xm[i+t][j];
				fo(t, k) y += ym[i][j+t];
				int kk = k - 1;
				x -= w[0] * a[i][j] + w[kk] * a[i][j+kk] + w[0] * a[i+kk][j] + w[kk] * a[i+kk][j+kk];
				y -= w[0] * a[i][j] + w[0] * a[i][j+kk] + w[kk] * a[i+kk][j] + w[kk] * a[i+kk][j+kk];
				if (x == 0 && y == 0) res = k;
			}
		}
	}
	if (res == -1) cout << "IMPOSSIBLE"; else cout << res;
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