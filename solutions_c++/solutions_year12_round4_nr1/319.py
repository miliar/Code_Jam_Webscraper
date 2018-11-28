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

#define maxn 10005

void init()
{

}

int n;
int d[maxn], len[maxn];
int D;
int dp[maxn];

void solvecase()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++) scanf("%d%d", &d[i], &len[i]);
	scanf("%d", &D);
	for (int i = 0; i < n; i++) dp[i] = 0;
	dp[0] = d[0];
	bool ok = false;
	for (int i = 0; i < n; i++)
	{
		for (int j = i+1; j < n && d[j] <= d[i] + dp[i]; j++) 
			dp[j] = max(dp[j], min(len[j], d[j] - d[i]));
		if (dp[i] + d[i] >= D) ok = true;
	}
	printf(ok ? "YES" : "NO");
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