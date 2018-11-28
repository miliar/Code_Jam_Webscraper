#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <iomanip>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long LL;
typedef long double ldb;

const int INF = (1 << 30) - 1;
const ldb EPS = 1e-9;
const ldb PI = fabs(atan2(0.0, -1.0));
const int MAXN = 30005;

int n;
pii ledge[MAXN];
void load()
{
	scanf("%d", &n);
	ledge[0] = mp(0, 0);
	for (int i = 1; i <= n; i++)
		scanf("%d%d", &ledge[i].fi, &ledge[i].se);
	scanf("%d", &ledge[n + 1].fi);
	ledge[n + 1].se = 0;
}

inline bool canReach(int s, int p, int t)
{
	int d1 = ledge[t].fi - ledge[s].fi;
	int d2 = ledge[s].fi - ledge[p].fi;
	return min(d2, ledge[s].se) >= d1;
}

bool can[MAXN];
int last[MAXN];
void solve(int test)
{
	memset(can, false, sizeof(can));
	memset(last, -1, sizeof(last));
	can[0] = can[1] = true;
	last[1] = 0;
	for (int i = 1; i <= n; i++)
	{
		if (!can[i]) continue;
		assert(last[i] != -1);
		for (int j = i + 1; j <= n + 1; j++)
		{
			if (!canReach(i, last[i], j)) continue;
			if (!can[j])
			{
				can[j] = true;
				last[j] = i;
			}
		}
	}
	printf("Case #%d: %s\n", test, can[n + 1] ? "YES" : "NO");
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		eprintf("test = %d\n", test);
		load();
		solve(test);
	}	
	return 0;
}
