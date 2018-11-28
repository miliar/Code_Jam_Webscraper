#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define NAME "D-small-attempt0"
#define MOD 10007

int h,w,n;
PII a[20];
int d[128][128];
bool bad[128][128];

int main()
{
	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		scanf("%d%d%d",&h,&w,&n);
		CLEAR(bad);
		REP(i,n)
		{
			scanf("%d%d",&a[i].X,&a[i].Y);
			a[i].X--;a[i].Y--;
			bad[a[i].X][a[i].Y] = true;
		}
		CLEAR(d);
		d[0][0]=1;
		REP(i,h) REP(j,w) if (!bad[i][j])
		{
			if (i>=1 && j>=2)
				d[i][j]+=d[i-1][j-2];
			if (i>=2 && j>=1)
				d[i][j]+=d[i-2][j-1];
			d[i][j]%=MOD;
		}

		printf("Case #%d: %d\n",tst+1,d[h-1][w-1]);
	}
	return 0;
}
