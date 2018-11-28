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

#define maxn 105

void init()
{

}


int n;
char buf[100];
int p[maxn];
bool orange[maxn];

int find_target(int idx, bool or)
{
	for (int i = idx; i < n; i++) if (orange[i] == or) return p[i];
	return 1;
}

void adjust(int &pos, int tgt)
{
	if (pos < tgt) pos++;
	if (pos > tgt) pos--;
}

void solvecase()
{
	scanf("%d", &n);
	int pos_o = 1, pos_b = 1;
	fo(i, n)
	{
		scanf("%s%d", buf, &p[i]);
		orange[i] = buf[0] == 'O';
	}
	int tgt_o = find_target(0, true);
	int tgt_b = find_target(0, false);
	int res = 0, i = 0;
	while (i < n)
	{
		res++;
		if (orange[i] && pos_o == p[i])
		{
			i++;
			tgt_o = find_target(i, true);
			adjust(pos_b, tgt_b);
			continue;
		}
		if (!orange[i] && pos_b == p[i])
		{
			i++;
			tgt_b = find_target(i, false);
			adjust(pos_o, tgt_o);
			continue;
		}
		adjust(pos_o, tgt_o);
		adjust(pos_b, tgt_b);
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

//#define fname "test"
//#define fname "A-small-attempt0"
#define fname "A-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}