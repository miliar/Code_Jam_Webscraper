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

#define MAXN 10011

int nTC,n,v,g[MAXN],c[MAXN],val[MAXN],inter;
int memo[MAXN][2];

int left(int i){ return i*2+1; }
int right(int i){ return i*2+2; }

int rec(int i, int v){
	if (i>=inter) return v==val[i]?0:MAXN;
	int &ret = memo[i][v];
	if (ret!=-1) return ret; else ret = MAXN;

	if (v){
		if (g[i]){
			ret <?= rec(left(i),1) + rec(right(i),1);
		} else {
			ret <?= rec(left(i),1) + rec(right(i),1);
			ret <?= rec(left(i),1) + rec(right(i),0);
			ret <?= rec(left(i),0) + rec(right(i),1);
		}

		if (c[i]){
			if (!g[i]){
				ret <?= 1 + rec(left(i),1) + rec(right(i),1);
			} else {
				ret <?= 1 + rec(left(i),1) + rec(right(i),1);
				ret <?= 1 + rec(left(i),1) + rec(right(i),0);
				ret <?= 1 + rec(left(i),0) + rec(right(i),1);
			}
		}
	} else {
		if (g[i]){
			ret <?= rec(left(i),1) + rec(right(i),0);
			ret <?= rec(left(i),0) + rec(right(i),1);
			ret <?= rec(left(i),0) + rec(right(i),0);
		} else {
			ret <?= rec(left(i),0) + rec(right(i),0);
		}

		if (c[i]){
			if (!g[i]){
				ret <?= 1 + rec(left(i),1) + rec(right(i),0);
				ret <?= 1 + rec(left(i),0) + rec(right(i),1);
				ret <?= 1 + rec(left(i),0) + rec(right(i),0);
			} else {
				ret <?= 1 + rec(left(i),0) + rec(right(i),0);
			}
		}
	}
	return ret;
}

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d: ",TC);
		scanf("%d %d",&n,&v);
		inter = (n-1)/2;
		REP(i,inter) scanf("%d %d",&g[i],&c[i]);
		FOR(i,inter,n-1) scanf("%d",&val[i]);
		
		memset(memo,-1,sizeof(memo));
		if (rec(0,v) == MAXN) puts("IMPOSSIBLE");
		else printf("%d\n",rec(0,v));
	}
}
