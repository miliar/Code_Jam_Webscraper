// short limit: 32767
// int limit  : 2147483647

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <sstream>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <climits>
#include <cassert>
#include <cstring>

using namespace std;

#define FOR(i,n) for(int i=0; i<(n); i++)
#define FORAB(i,a,b) for(int i=(a); i<=(b); i++)
#define RFOR(i,n) for(int i=(n)-1; i>=0; i--)
#define RFORAB(i,a,b) for(int i=(a); i>=(b); i--)

#define FOR64(i,n) for(long long i=0; i<(n); i++)
#define FORAB64(i,a,b) for(long long i=(a); i<=(b); i++)
#define RFOR64(i,n) for(long long i=(n)-1; i>=0; i--)
#define RFORAB64(i,a,b) for(long long i=(a); i>=(b); i--)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REVERSE(c) (reverse(ALL(c)))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define SIZE(c) ((int)(c).size())
#define MP(X,Y) make_pair(X,Y)
#define PB push_back

#define EQ(E, F) (fabs((E)-(F))<=eps)

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long ULL;

const double eps = 1e-11;
const double pi = acos(-1.0);

int N, D;
int d[10000];
int l[10000];

bool step(int holding, int position)
{
	int maxWeCanHold = d[holding] + min(d[holding] - position, l[holding]);

	if (maxWeCanHold >= D)
		return true;

	FORAB(i, holding+1, N-1)
		if (d[i] <= maxWeCanHold)
			if (step(i, d[holding]))
				return true;

	return false;
}

void solve()
{
	CLEAR(d);
	CLEAR(l);
	//assert(scanf("%[a-z ]\n", str) == 1);
	scanf("%d\n", &N);
	FOR(i, N)
		scanf("%d %d\n", d+i, l+i);
	scanf("%d\n", &D);

	printf("%s", step(0,0) ? "YES" : "NO");
}

int main()
{
	//freopen(".in","r",stdin);
	//freopen(__FILE__ ".out","w",stdout);

	int tests;
	assert(scanf("%d\n",&tests) == 1);

	FOR(test, tests)
	{
		printf("Case #%d: ", test+1);
		solve();
		printf("\n");
	}

	return 0;
}

