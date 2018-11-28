#include<algorithm>
#include<cstdio>
#include<vector>
#include<cmath>
#include<set>
using namespace std;

typedef long long LL;
typedef long double LD;
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

#define kwa(x) ((x)*(x))

const int MAX = 100000;
const int INF = 1000000001;

PII tab[MAX];
int R[MAX];

int n;

LD obczaj(int x) {
	int i, j;
	if(x == 0)
		i = 1, j = 2;
	else if(x == 1)
		i = 0, j = 2;
	else
		i = 0, j = 1;
	return max((LD)R[x], (LD)(sqrt(kwa(tab[i].ST-tab[j].ST) + kwa(tab[i].ND-tab[j].ND)) + R[i] + R[j])/2.0);
}

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		scanf("%d", &n);
		REP(i,n)
			scanf("%d %d %d", &tab[i].ST, &tab[i].ND, R+i);
		printf("Case #%d: ", z);
		if(n == 1)
			printf("%.6Lf\n", (LD)R[0]);
		else if(n == 2)
			printf("%.6Lf\n", (LD)max(R[0], R[1]));
		else
			printf("%.6Lf\n", min(obczaj(0), min(obczaj(1), obczaj(2))));
	}
	return 0;
}

