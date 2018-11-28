//* Problem  : 
//* Date     : 2010.05.08
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
#pragma comment(linker, "/STACK:16177216")

// to disable Visual C++ secure warnings
#pragma warning(disable : 4996)

///BEGIN CUT HERE
// types
typedef long long int64;
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
#define REP(n) for (int _foo = (int)(n) - 1; _foo >= 0; _foo--)
#define REP2(n) for (int _foo2 = (int)(n) - 1; _foo2 >= 0; _foo2--)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); it++)

//sorting & c
#define ALL(a) a.begin(), a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define REVERSE(a) reverse(ALL(a))
//fill
#define FLA(a, v) memset(a, v, sizeof(a))
#define CLA(a) FLA(a, 0)
//misc
#define MP make_pair
#define PB push_back
#define SZ(a) (int)a.size()
//consts
const int INF = 2000000000;
const int64 INFL = 1000000000000000000LL;
const long double PI = acos(-1.0);
const long double EPS = 1E-7;

//math
template <typename T> inline T gcd(T a, T b)				{ return b ? gcd(b, a % b) : a; }
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
inline double rd(){double tt; ASSERTS(scanf("%lf", &tt) == 1, "ReadInt failed"); return tt;}
inline int64 ri64(){int64 tt; ASSERTS(scanf("%lld", &tt) == 1, "ReadInt64 failed"); return tt;}
inline void rs(char *s){ASSERTS(scanf("%s", s) == 1, "ReadChar* failed");}
//output
inline void pi(int n){printf("%d\n", n);}	
inline void pi64(int64 n){printf("%lld\n", n);}

const int dx4[] = {-1, 1, 0, 0};
const int dy4[] = {0, 0, -1, 1};
///END CUT HERE

int64 groups, load, trips;

int a[1024];

int C[1024];

int64 S[1024];

int64 res;

void solve()
{
	FOR(k, groups)
	{
		int64 sum = 0;
		int p = k;
		int c = 0;
		while (c < groups)
		{
			if (sum + a[p] > load)
				break;
			sum += a[p];
			p = (p + 1) % groups;
			c++;
		}
		S[k] = sum;
		C[k] = c;
		//printf("%d %lld\n", c, sum);
	}
	int p = 0;
	res = 0;
	REP(trips)
	{
		res += S[p];
		p = (p + C[p]) % groups;
	}
}

int main()
{
#ifdef _DEBUG
	freopen("1064", "r", stdin);
	freopen("C-small", "w", stdout);
#endif
	int nt = ri();
	FORE(it, 1, nt)
	{
		trips = ri();
		load = ri();
		groups = ri();
		FOR(i, groups)
			a[i] = a[i+groups] = ri();
		solve();
		printf("Case #%d: %lld\n", it, res);
	}
};