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


const int MAX = 40;
const int INF = 1000000001;

char tab[MAX][MAX];

int n;

int w;

void obczaj(int x) {
	if(x == n)
		return;
	FOR(i,x,n-1)
	{
		bool ok = true;
		FOR(j,x+1,n-1)
			if(tab[i][j]) {
				ok = false;
				break;
			}
		if(ok) {
			w += i - x;
			FORD(k,i,x+1)
				REP(j,n)
					swap(tab[k][j], tab[k-1][j]);
			//printf("x %d: %d\n", x, i); REP(i,n) { REP(j,n) printf("%d", tab[i][j]); printf("\n"); } printf("\n");
			obczaj(x+1);
			return;
		}
	}
}

main() {
	int Z;
	scanf("%d\n", &Z);
	FOR(z,1,Z)
	{
		w = 0;
		scanf("%d\n", &n);
		REP(i,n)
		{
			REP(j,n)
				scanf("%c", &tab[i][j]), tab[i][j] -= '0';
			scanf("\n");
		}
		//REP(i,n) { REP(j,n) printf("%d", tab[i][j]); printf("\n"); }
		obczaj(0);
		printf("Case #%d: %d\n", z, w);
	}
	return 0;
}

