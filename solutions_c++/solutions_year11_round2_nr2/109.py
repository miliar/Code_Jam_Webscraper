#include<algorithm>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof((Z).begin()) x=(Z).begin();x!=(Z).end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) ((int)(X).size())
#define CLR(X,x) memset(X, x, sizeof(X))

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug printf
#else
#define debug(fmt, ...)
#endif


const int MAX = 200;
const LL INF = 1e18;

pair<LL,int> V[MAX];

int n;
LL d;

bool ok(LL x) {
	LL last = -INF;
	REP(i,n)
	{
		REP(foo,V[i].ND)
		{
			LL now = max(last+d, V[i].ST-x);
			if(now - last < d || abs(V[i].ST-now) > x)
				return false;
			last = now;
		}
	}
	return true;
}

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d %lld", &n, &d);
		d *= 2;
		REP(i,n)
			scanf("%lld %d", &V[i].ST, &V[i].ND),
			V[i].ST *= 2;
		LL p = 0, q = INF, r;
		while(p < q)
		{
			r = (p+q)/2;
			if(ok(r))
				q = r;
			else
				p = r + 1;
		}
		printf("%lld.%d\n", p/2, (p&1) ? 5 : 0);
	}
	return 0;
}

