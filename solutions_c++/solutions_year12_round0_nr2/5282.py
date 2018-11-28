#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <sstream>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;
typedef long long LL;
#define FOR(x, b, e) for (int x = (b); x <= (e); ++x)
#define FORD(x, b, e) for (int x = (b); x >= (e); --x)
#define REP(x, n) for (int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int) (x).size())
#define EACH(i, c) for (VAR(i, (c).begin()); i != (c).end(); ++i)
#define REACH(i, c) for (VAR(i,(c).rbegin()); i != (c).rend(); ++i)
#define UNIQUE(v) do { sort(ALL(v)); (v).resize(unique(ALL(v)) - (v).begin()); } while (0)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define skip continue
const int INF = 1000000001;

#define GET(x)			(scanf("%d", &(x)) == 1)
#define GET2(x, y)		(scanf("%d %d", &(x), &(y)) == 2)
#define GET3(x, y, z)	(scanf("%d %d %d", &(x), &(y), &(z)) == 3)
#define GETS(x)			(scanf("%s", (x)) == 1)
#define DGET(x)			int x; GET(x);

int f1(int x)
{
	x -= x/3;
	return x - x/2;
}

int f2(int x)
{
	if (x < 2 || x > 28) return -1;
	return f1(x) + (x % 3 != 1);
}

int main()
{
	DGET(t);
	FOR (tt, 1, t) {
		int n, s, p;
		GET3(n, s, p);
		
		int res = 0;
		
		REP (i, n) {
			DGET(x);
			
			res += (f1(x) >= p) || (s > 0 && f2(x) >= p && s--);
		}
		
		printf("Case #%d: %d\n", tt, res);
	}
}
