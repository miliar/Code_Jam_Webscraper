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

#define maxn 105

char a[maxn][maxn];
char tmp[maxn], tmp2[maxn];
double res[maxn], owp[maxn];
int n;

double getwp(int idx)
{
	int wins = 0, games = 0;
	fo(i, n) 
	{
		if (a[idx][i] != '.') games++;
		if (a[idx][i] == '1') wins++;
	}
	return (double)wins / games;
}

void solvecase()
{
	scanf("%d", &n);
	fo(i, n) scanf("%s", &a[i]);
	fo(i, n)
	{
		res[i] = 0.25 * getwp(i);
		fo(j, n) tmp[j] = a[i][j], tmp2[j] = a[j][i];
		fo(j, n) a[i][j] = '.', a[j][i] = '.';
		int k = 0;
		double x = 0;
		fo(j, n) if (tmp[j] != '.')
		{
			k++;
			x += getwp(j);
		}
		fo(j, n) a[i][j] = tmp[j], a[j][i] = tmp2[j];
		owp[i] = x / k;
		res[i] += 0.5 * x / k;
	}
	fo(i, n)
	{
		int k = 0;
		double x = 0;
		fo(j, n) if (a[i][j] != '.')
		{
			k++;
			x += owp[j];
		}
		res[i] = res[i] + 0.25 * x / k;
	}
	fo(i, n) printf("\n%.7lf", res[i]);
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