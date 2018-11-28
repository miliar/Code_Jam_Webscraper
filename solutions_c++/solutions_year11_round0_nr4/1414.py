#include<algorithm>
#include<cstdio>
#include<vector>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof(Z.begin()) x=Z.begin();x!=Z.end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) X.begin(),X.end()

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif


const int MAX = 100000;
const int INF = 1000000001;

int n;

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d", &n);
		int ret = n;
		FOR(i,1,n)
		{
			int a;
			scanf("%d", &a);
			ret -= i == a;
		}
		printf("%d.000000\n", ret);
	}
	return 0;
}

