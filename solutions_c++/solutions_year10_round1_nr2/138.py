#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i = 0,_n = (n);i < _n;++i)
#define FOR(i,a,b) for(int i = (a),_n = (b);i <= _n;++i)
const int INF = 1000000000;

const int NMAX = 100, ASIZE = 256;
int T[NMAX], insert_dist[ASIZE][ASIZE];

int compute_insert_dist(int a,int b,int I,int M) {
	if (a > b) swap(a,b);
	if (M == 0) return a==b ? 0 : INF;
	int res = 0;
	while (b-a > M) {
		res += I;
		b -= M;
	}
	return res;
}

// dyn[i][j] - T[0..i], konczy sie na T[j-1]
int dyn[NMAX][ASIZE+1];
const int EMPTY = ASIZE;

void testcase(int nr) {
	int D,I,M,N;
	scanf("%d%d%d%d",&D,&I,&M,&N);
	REP(i,N) scanf("%d",T+i);
	
	REP(i,ASIZE) REP(j,ASIZE) insert_dist[i][j] = 
		compute_insert_dist(i,j,I,M);
	
	dyn[0][EMPTY] = D;
	REP(i,ASIZE) dyn[0][i] = abs(T[0]-i);
	REP(i,N-1) {
		dyn[i+1][EMPTY] = dyn[i][EMPTY]+D;
		REP(j,ASIZE) dyn[i+1][j] = dyn[i][j]+D;
		REP(j,ASIZE) REP(k,ASIZE)
			dyn[i+1][k] = min(dyn[i+1][k],dyn[i][j]+abs(T[i+1]-k)+insert_dist[j][k]);
	}
	
	int res = INF;
	REP(i,ASIZE+1) res = min(res,dyn[N-1][i]);
	
	printf("Case #%d: %d\n",nr,res);
}

int main() {
	int T;
	scanf("%d",&T);
	REP(i,T) testcase(i+1);
}
