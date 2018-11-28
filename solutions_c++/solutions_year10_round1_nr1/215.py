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


const int MAX = 50;
const int INF = 1000000001;

char tab[MAX][MAX+1];
char T[MAX][MAX];

int n, k;

vector<char> Q;

void skmin(int x) {
	Q.clear();
	REP(i,n)
		if(T[i][x] != '.')
			Q.PB(T[i][x]),
			T[i][x] = '.';
	reverse(ALL(Q));
	REP(i,Q.size())
		T[n-i-1][x] = Q[i];
}

#define war (x >= 0 && x < n && y >= 0 && y < n && T[x][y] == c)

bool jest(char c) {
	REP(i,n)
		REP(j,n)
		 if(T[i][j] == c) {
		 	int x, y;
		 	int tmp;
		 	for(x=i,y=j,tmp=0;war;--x) ++tmp;
		 	if(tmp >= k) return true;
		 	for(x=i,y=j,tmp=0;war;++x) ++tmp;
		 	if(tmp >= k) return true;
		 	for(x=i,y=j,tmp=0;war;--y) ++tmp;
		 	if(tmp >= k) return true;
		 	for(x=i,y=j,tmp=0;war;++y) ++tmp;
		 	if(tmp >= k) return true;
		 	for(x=i,y=j,tmp=0;war;--y,--x) ++tmp;
		 	if(tmp >= k) return true;
		 	for(x=i,y=j,tmp=0;war;--y,++x) ++tmp;
		 	if(tmp >= k) return true;
		 	for(x=i,y=j,tmp=0;war;++y,--x) ++tmp;
		 	if(tmp >= k) return true;
		 	for(x=i,y=j,tmp=0;war;++y,++x) ++tmp;
		 	if(tmp >= k) return true;
		 }
	return false;
}

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d %d", &n, &k);
		REP(i,n)
			scanf("%s", &tab[i]);
		REP(i,n)
			REP(j,n)
				T[j][n-i-1] = tab[i][j];
		REP(i,n)
			skmin(i);
		if(jest('R'))
			if(jest('B'))
				printf("Both\n");
			else
				printf("Red\n");
		else if(jest('B'))
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}

