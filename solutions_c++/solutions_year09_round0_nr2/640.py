//* Problem  : GCJ-2009: Qualification Round 2009
//* Date     : 2009.09.03
//* Author   : alt
//* Tags     : 

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <numeric>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <string>
#include <vector>
#include <cctype>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

//stack
//#pragma comment(linker, "/STACK:167177216")

// to disable Visual C++ secure warnings
#pragma warning(disable : 4996)

///BEGIN CUT HERE
// types
typedef long long int64;
typedef unsigned long long uint64;
typedef pair <int,int> PII;
typedef vector <int> VI;
typedef vector <int64> VI64;
typedef vector <string> VS;
typedef vector <vector<string> > VVS;
typedef vector <vector<int> > VVI;
typedef vector <pair<int,int> > VPII;
typedef vector <vector<pair<int,int> > > VVPII;
typedef map<int, int > MII;
typedef map<string, int > MSI;
typedef queue<int > QI;
typedef queue<PII > QPII;
//loops
#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define FORR(i, n) for (int i = (int)(n)-1; i >= 0; i--)
#define FORE(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define FORER(i, a, b) for (int i = (int)(a); i >= (int)(b); i--)
#define FORSZ(i, a) FOR(i, SZ(a))
#define FORSZR(i, a) FORR(i, SZ(a))
#define FORO(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOROR(i, x) for (typeof((x).end()) i = (x).end(); i != (x).begin(); i--)
#define REP(n) for (int _foo = (int)(n) - 1; _foo >= 0; _foo--)
#define REP2(n) for (int _foo2 = (int)(n) - 1; _foo2 >= 0; _foo2--)

#define VAR(a, b) typeof(b) a=(b)
#define FOREACH(it, c) for(VAR(it,(c).begin()); it!=(c).end(); it++)
//sorting & c
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()
#define SORT(a) sort(ALL(a))
#define RSORT(a) sort(RALL(a))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define REVERSE(a) reverse(ALL(a))
//filling
#define FLA(a,val) memset(a, val, sizeof(a))
#define FLO(o,val) memset(&o, val, sizeof(o))
#define CLA(a) FLA(a, 0)
#define CLO(a) FLO(a, 0)
//misc
#define _x first
#define _y second
#define MP make_pair
#define PB push_back
#define SZ(a) (int)a.size()
#define POP(a) a.top(), a.pop()
#define FRONT(a) a.front(), a.pop()
//const
const int INF = 1000000000;
const int64 INFL = 1000000000000000000LL;
const long double PI = acos(-1.0);
const long double EPS = 1E-9;

//some math
template <typename T> inline T gcd(T a, T b)				{ return b ? gcd(b, a % b) : a; }
template <typename T> inline T gcd2(T a, T b)				{ while (a && b) (a > b) ? a %= b : b %= a; return a + b;}
template <typename T> inline T abs(T a)					{ return a < 0 ? -a : a; }
template <typename T> inline T sqr(T a)					{ return a * a; }
template <typename T> inline double hypot(T a, T b)		{ return sqrt(1.0 * a * a + b * b);}
template <typename T> inline T hypot2(T a, T b)			{ return a * a + b * b;}

//assertions
#ifdef _DEBUG
#define ASSERT(f) if (!(f)) printf("%s\n", "ASSERTION FAILED!");
#define ASSERTS(f, s) if (!(f)) printf("%s [%s]\n", "ASSERTION FAILED!", s);
#else
#define ASSERT(f) f
#define ASSERTS(f, s) f
#endif

//input
inline int ri(){int tt; ASSERTS(scanf("%d", &tt) == 1, "ReadInt failed"); return tt;}
inline int64 ri64(){int64 tt; ASSERTS(scanf("%lld", &tt) == 1, "ReadInt64 failed"); return tt;}
inline void rs(char *s){ASSERTS(scanf("%s", s) == 1, "ReadChar* failed");}
//output
inline void pvi(int *a, int n){FOR(i, n) printf("%d%c", a[i], i == n - 1 ? '\n' : ' ');}
//inline void pvi(VI a){FORSZ(i,a) printf("%d%c", a[i], i == a.size() - 1 ? '\n' : ' ');}
inline void pi(int n){printf("%d\n", n);}
inline void pi64(int64 n){printf("%lld\n", n);}

inline void _pi64(int64 n)
{
	if (n < 0) {putchar('-'); n = -n;}
	if (!n) {putchar('0'); return;}
	char stack[30]; int istack = 0;
	while (n)
	{
		stack[istack++] = (n % 10) + '0'; n /= 10;
	}
	while (istack > 0)
		putchar(stack[--istack]);
}
///END CUT HERE

int n, m, res, k;

int a[128][128];

char r[128][128];

int cc[128][128], cc_count;

const int dx4[] = {-1, 0, 0, 1};
const int dy4[] = {0, -1, 1, 0};

int get_min(int x, int y)
{
	int res = INF;
	FOR(k, 4)
	{
		int xx = x + dx4[k];
		int yy = y + dy4[k];
		if (xx < 0 || xx >= n || yy < 0 || yy >= m) continue;
		res = min(res, a[xx][yy]);
	}
	return res;
}

int fill(int x, int y)
{
	if (cc[x][y])
		return cc[x][y];
	int mn = get_min(x, y);
	if (mn >= a[x][y])
	{
		return cc[x][y] = ++cc_count;
	}
	FOR(k, 4)
	{
		int xx = x + dx4[k];
		int yy = y + dy4[k];
		if (xx < 0 || xx >= n || yy < 0 || yy >= m) continue;
		if (a[xx][yy] == mn)
			return cc[x][y] = fill(xx, yy);
	}		
}

int cc_letter[256];

int letter;

void solve()
{
	CLA(r); CLA(cc); cc_count = 0;
	CLA(cc_letter); letter = 'a';
	FOR(i,n) FOR(j, m)
		fill(i, j);
	FOR(i,n) FOR(j, m)
	{
		int res = cc_letter[cc[i][j]];
		if (!res)
		{
			res = cc_letter[cc[i][j]] = letter++;
		}
		r[i][j] = res;
	}

}

int main()
{
#ifdef _DEBUG
	freopen("1064", "r", stdin);
	freopen("b.easy", "w", stdout);
#endif
	int nt = ri();
	FORE(it, 1, nt)
	{
		n = ri();
		m = ri();
		FOR(i,n) FOR(j, m) a[i][j] = ri();
		solve();
		printf("Case #%d:\n", it);
		FOR(i,n) FOR(j, m) putchar(r[i][j]), putchar(j == m - 1 ? '\n' : ' ');
	}
}



