#include <stdio.h>
#include <assert.h>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)
#define FORD(i,a,b) for (int i=a,_n=b; i>=_n; i--)

#define MAXN (1<<12)
#define INF 1000000000

int T,P,M[MAXN],memo[MAXN][11];
int MP[11][MAXN],TP[MAXN];

int rec(int idx, int depth, int has){
	assert(idx<MAXN);
	assert(has<11);

	int &ret = memo[idx][has];
	if (ret!=-1) return ret;

	if (depth==P){
		int need = P-M[idx];
		if (has>=need) return ret = 0;
		return ret = INF;
	}

	int L1 = rec(idx*2+1, depth+1, has) + rec(idx*2+2, depth+1, has);
	int L2 = rec(idx*2+1, depth+1, has+1) + rec(idx*2+2, depth+1, has+1) + TP[idx];

	ret = (L1<?L2);
//	printf("%d %d %d : %d = %d %d\n",idx,depth,has,ret,L1,L2);
	assert(L1>=0);
	assert(L2>=0);
	if (ret > INF) ret = INF;
	return ret;
}

int main(){
	scanf("%d",&T);
	REP(tt,T){
		scanf("%d",&P);
		memset(M,0,sizeof(M));
		REP(i,1<<P){
			scanf("%d",&M[(1<<P)-1+i]);
//			printf("%d = %d\n",(1<<P)-1+i,M[(1<<P)-1+i]);
		}
		FOR(r,1,P){
			int m = 1<<(P-r);
			assert(m<MAXN);
			REP(j,m) scanf("%d",&MP[r][j]);
		}
		int idx = 0;
		FORD(r,P,1){
			int m = 1<<(P-r);
			REP(j,m) TP[idx++] = MP[r][j];
		}
		REP(i,idx*2+1){
//			printf("idx = %d, M = %d, P = %d\n",i,M[i],TP[i]);
		}
		memset(memo,-1,sizeof(memo));
		printf("Case #%d: %d\n",tt+1,rec(0,0,0));
	}
}
