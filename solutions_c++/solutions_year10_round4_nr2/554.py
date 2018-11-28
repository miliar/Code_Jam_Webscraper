#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i = 0,_n = (n);i < _n;++i)
#define FOR(i,a,b) for(int i = (a),_n = (b);i <= _n;++i)
#define FORD(i,a,b) for(int i = (a),_n = (b);i >= _n;--i)
#define FORE(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(c) ((int)(c).size())
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

const int INF = 1000000000;

const int PMAX = 10, NMAX = 1<<PMAX;
int M[NMAX], to_miss[PMAX][NMAX], price[PMAX][NMAX], dyn[PMAX][NMAX][PMAX+1];

int compute_dyn(int ind,int j,int off) {
	int& res = dyn[ind][j][off];
	if (res != -1) return res;
	
	if (ind == 0) {
		int k = to_miss[ind][j]-off;
		if (k < 0) return res = INF;
		else if (k == 0) return res = price[ind][j];
		else return res = 0;
	}
	
	res = price[ind][j] + compute_dyn(ind-1,2*j,off) + compute_dyn(ind-1,2*j+1,off);
	res = min(res,compute_dyn(ind-1,2*j,off+1) + compute_dyn(ind-1,2*j+1,off+1));
	if (res > INF) res = INF;
	return res;
}

void testcase(int zest) {
	int P;
	scanf("%d",&P);
	int N = 1<<P;
	
	REP(i,N) scanf("%d",M+i);
	REP(i,P) REP(j,1<<(P-i-1)) scanf("%d",&price[i][j]);
	REP(i,N/2) to_miss[0][i] = min(M[2*i],M[2*i+1]);
	FOR(i,1,P-1) REP(j,1<<(P-i-1))
		to_miss[i][j] = min(to_miss[i-1][2*j],to_miss[i-1][2*j+1]);
	
	REP(i,P) REP(j,1<<(P-i-1)) FOR(k,0,P) dyn[i][j][k] = -1;
	
	printf("Case #%d: %d\n",zest,compute_dyn(P-1,0,0));
}

int main() {
	int z;
	scanf("%d",&z);
	REP(i,z) testcase(i+1);
}
