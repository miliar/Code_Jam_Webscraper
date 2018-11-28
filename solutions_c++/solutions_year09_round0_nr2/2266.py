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


const int MAX = 100;
const int INF = 1000000001;

int M[MAX+2][MAX+2];
char W[MAX+2][MAX+2];

int n, m;
char c;

char pa(int x, int y) {
	if(W[x][y] != -1)
		return W[x][y];
	int mi = INF;
	FOR(i,-1,1)
		FOR(j,-1,1)
			if(abs(i) + abs(j) == 1)
				mi = min(mi, M[x+i][y+j]);
	if(mi >= M[x][y]) {
		W[x][y] = c;
		++c;
		return W[x][y];
	}
	if(M[x-1][y] == mi)
		return W[x][y] = pa(x-1, y);
	if(M[x][y-1] == mi)
		return W[x][y] = pa(x, y-1);
	if(M[x][y+1] == mi)
		return W[x][y] = pa(x, y+1);
	if(M[x+1][y] == mi)
		return W[x][y] = pa(x+1, y);
}

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		scanf("%d %d", &n, &m);
		FOR(i,0,n+1)
			FOR(j,0,m+1)
				M[i][j] = INF, W[i][j] = -1;
		FOR(i,1,n)
			FOR(j,1,m)
				scanf("%d", &M[i][j]);
		
		c = 'a';
		FOR(i,1,n)
			FOR(j,1,m)
				W[i][j] = pa(i, j);
		
		printf("Case #%d:\n", z);
		FOR(i,1,n)
		{
			FOR(j,1,m)
			{
				printf("%c", W[i][j]);
				if(j != m)
					printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}

