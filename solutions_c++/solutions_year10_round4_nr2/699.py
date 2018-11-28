#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

const LG INF = 5000000000LL;

int P, P2;
int M[1111];
LG cost[555][11];
LG T[1111][11][11];

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) {
		scanf("%d", &P); P2 = 1 << P;
		FOR(i,0,P2) scanf("%d", M + i), M[i] = min(P, M[i]);
		FOR(i,0,P) for(int j=0; j<P2/2; j+=1<<i)
			scanf("%lld", &cost[j][i]);
		FOR(i,0,P2) FOR(j,0,P) FOR(k,0,P) T[i][j][k] = INF;
		FOR(i,0,P2/2) {
			int m = min(M[2*i], M[2*i + 1]);
			T[2*i][0][m] = cost[i][0];
			if(m > 0) T[2*i][0][m - 1] = 0;
//	printf("T[%d][0][%d] = %lld\n", 2*i, m, T[2*i][0][m]);
//			if(m > 0)
//	printf("T[%d][0][%d] = %lld\n", 2*i, m - 1, T[2*i][0][m-1]);
		}
		FOR(j,1,P) for(int i=0; i<P2; i+=1<<(j+1)) FOR(k,0,P-j) {
			LG k1 = INF, k2 = INF;
			FOR(v,k+1,P) {
				k1 = min(k1, T[i][j-1][v]);
				k2 = min(k2, T[i + (1<<j)][j-1][v]);
			}
			LG k11 = min(k1, T[i][j-1][k]);
			LG k22 = min(k2, T[i + (1<<j)][j-1][k]);
			T[i][j][k] = min(
				T[i][j-1][k] + cost[i/2][j] + k22, min(
				T[i][j-1][k + 1] + k2, min(
				k11 + cost[i/2][j] + T[i + (1<<j)][j-1][k],
				k1 + T[i + (1<<j)][j-1][k + 1]
				)));
//		printf("**-->  %lld\n", cost[i/2][j]);
		//printf("***** %lld\n", k22);
//		printf("** %lld\n", T[i][j-1][k] + cost[i/2][j] + k22);
		//printf("***** %lld\n", T[i][j-1][k + 1]);
//		printf("** %lld\n", T[i][j-1][k + 1] + k2);
		//printf("***** %lld\n", k11);
//		printf("** %lld\n", k11 + cost[i/2][j] + T[i + (1<<j)][j-1][k]);
		//printf("***** %lld\n", k1);
//		printf("** %lld\n", k1 + T[i + (1<<j)][j-1][k + 1]);
//			printf("T[%d][%d][%d] = %lld\n", i, j, k, T[i][j][k]);
		}
		printf("Case #%d: %lld\n", zzz + 1, T[0][P-1][0]);
	}
	return 0;
}
