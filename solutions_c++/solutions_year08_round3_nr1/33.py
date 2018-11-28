#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for (int i=(a),_b=(b); i>=_b; i--)
#define REP(i,n) for (int i=0,_n=(n); i<_n; i++)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)
#define FOREACHD(it,arr) for (__typeof((arr).rbegin()) it=(arr).rbegin(); it!=(arr).rend(); it++)

int nTC,P,K,L,F[1001];

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		scanf("%d %d %d",&P,&K,&L);
		REP(i,L) scanf("%d",&F[i]);

		printf("Case #%d: ",TC);
		if (L > K*P) puts("Impossible");
		else {
			long long res = 0, depth = 0;
			sort(F,F+L);
			REP(i,L){
				int j = L-i-1;
				if (i%K==0) depth++;
				res += F[j]*depth;
			}
			printf("%lld\n",res);
		}
	}
}
