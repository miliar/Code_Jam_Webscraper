//* Problem  : 
//* Contest  : Google Code Jam 2008. Online Round 2
//* Date     : 2008.08.02
//* Author   : alt
//* Language : C++
//* Compiler : Microsoft Visual C++ 8.0

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef pair <int,int> PIII;
typedef vector <int> VI;
typedef vector <vector<int> > VVI;
typedef vector <pair<int,int> > VPII;
typedef vector <vector<pair<int,int> > > VVPII;

#define int64 long long
#define PI (2.0 * acos(0.0))
#define MP make_pair
#define PB push_back
#define SZ(a) (int)a.size()
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define FORSZ(i, a) FOR(i, SZ(a))
#define FORE(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define FORR(i, a, b) for (int i = (int)(a); i >= int(b); i--)
#define INF 1000000000
#define INFL 1000000000000000000LL
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()

int it, nt;
inline int si(){int tt; scanf("%d", &tt); return tt;}

int64 n, m, a;

int64 res1_x, res1_y, res2_x, res2_y, res3_x, res3_y, res;


int solve()
{
	for (res2_x = 0; res2_x <= n; res2_x++)
		for (res2_y = 0; res2_y <= m; res2_y++)
			for (res3_x = 0; res3_x <= n; res3_x++)
				for (res3_y = 0; res3_y <= m; res3_y++)
				{
					int64 sq = res1_x * (res2_y - res3_y) + res2_x * (res3_y - res1_y) + res3_x * (res1_y - res2_y);
					if (sq == a)
					{
						res = 1;
						return 1;
					}
				}
	return 0;
}

void result()
{
	printf("Case #%d: ", it);
	if (!res)
		printf("IMPOSSIBLE\n");
	else
		printf("%lld %lld %lld %lld %lld %lld\n", res1_x, res1_y, res2_x, res2_y, res3_x, res3_y);
}


int main()
{
	freopen("1064", "r", stdin);
	freopen("A-small.out", "w", stdout);	
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		n = si(); m = si(); a = si();
		res1_x = 0; res1_y = 0;
		if (solve())
		{
			res = 1;
		}
		else
		{
			res1_x = n/2; res1_y = m/2;
			if (solve()) res = 1;
			else res = 0;
		}
		result();
	}
	return 0;
}

