
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cassert>
using namespace std;

/*PREWRITTEN CODE BEGINS HERE*/
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define SIZE(x) (int)((x).size())

#define REP(i,n) for(int i=0,_n=(n); i<_n; ++i)
#define ALWAYS(f,p) (({bool _wyn=true;f if(!(p)){_wyn=false;break;}_wyn;})) 
#define EXISTS(f,p) (({bool _wyn=false;f if(p){_wyn=true;break;}_wyn;})) 
#define CT(mask,k) ( ((mask) >> (k)) & 1 )


typedef pair<int,int> PII;
template<class T> inline int BC(T x) {
	int ret = 0;
	for( ; x ; x &= x-1) ++ret;
	return ret;
}
/*PREWRITTEN CODE ENDS HERE*/
inline int RI() { int xx; scanf("%d",&xx); return xx; }
typedef long double LD;
const int INF = 1010000000;
const double EPS = 1e-9;
/*SOLUTION BEGINS HERE*/


const int MAX = 300;
vector<PII> v[MAX];
int N,M;

void brut(void){
	
	int cnt = INF, ret_mask = 0;
	REP(mask, 1<<N) {
		
		if(ALWAYS( REP(j, M), EXISTS( REP(k, SIZE(v[j])),  (v[j][k].S == 1 && CT(mask,v[j][k].F)) || (v[j][k].S == 0 && !CT(mask, v[j][k].F))))) {
			
			if(cnt > BC(mask)) {
				cnt = BC(mask);
				ret_mask = mask;
			}
		}
	}
	
	if(cnt == INF) printf(" IMPOSSIBLE\n");
	else {
		REP(i, N) printf(" %d", (ret_mask>>i) & 1);
		printf("\n");
	}

}
void solve(){
	scanf("%d %d", &N, &M);
	REP(i, M) v[i].clear();
	REP(i, M){
		int k,a,b;
		scanf("%d", &k);
		REP(j,k) {
			scanf("%d %d", &a, &b); v[i].PB( MP(a-1,b));
		}
	}
	brut(); return ;

}

int main(void)
{
	int T, C = 1;
	scanf("%d", &T);
	while(T--) { printf("Case #%d:",C++); solve(); }
	return (0);
}
