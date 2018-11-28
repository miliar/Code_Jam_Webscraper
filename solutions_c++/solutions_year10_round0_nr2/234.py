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


const int MAX = 1000;
const int INF = 1000000001;

LL tab[MAX];

LL nwd(LL a, LL b) {
	return !b ? a : nwd(b, a%b);
}

int n;

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d", &n);
		REP(i,n)
			scanf("%lld", tab+i);
		if(n == 2) {
			LL m = abs(tab[0]-tab[1]);
			printf("%lld\n", (m-(tab[0]%m))%m);
			continue;
		}
		LL m = nwd(abs(tab[0]-tab[1]), nwd(abs(tab[0]-tab[2]), abs(tab[1]-tab[2])));
		printf("%lld\n", (m-(tab[0]%m))%m);
	}
	return 0;
}

