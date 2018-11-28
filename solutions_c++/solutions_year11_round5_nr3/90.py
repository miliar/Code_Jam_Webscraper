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

int n, m;

int a[105][105], cnt[105][105];
char s[105][105];

int num(char c)
{
	if (c == '-') return 0;
	if (c == '|') return 1;
	if (c == '/') return 2;
	return 3;
}

int di[4][2] = { {0, 0}, {-1, 1}, {-1, 1}, {-1, 1} };
int dj[4][2] = { {-1, 1}, {0, 0}, {1, -1}, {-1, 1} };

void solvecase()
{
	scanf("%d%d", &n, &m);
	fo(i, n) scanf("%s", s[i]);
	fo(i, n) fo(j, m) a[i][j] = num(s[i][j]);

	int res = 0;
	int k = n*m;
	int K = 1<<k;

	fo(mask, K)
	{
		fo(i, n) fo(j, m) cnt[i][j] = 0;
		fo(i, n) fo(j, m)
		{
			int num = i*m + j;
			int bit = mask & (1<<num) ? 1 : 0;
			int ii = (i + di[a[i][j]][bit] + n) % n;
			int jj = (j + dj[a[i][j]][bit] + m) % m;
			cnt[ii][jj]++;
		}
		bool ok = true;
		fo(i, n) fo(j, m) if (cnt[i][j] != 1) ok = false;
		if (ok) res++;
	}
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

#define problem_letter "C"
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