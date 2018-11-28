#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <math.h>
#include <set>
#include <queue>
using namespace std;
typedef long long LL;
#define INF 1000000000000000002ll
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++) 
#define FS first
#define SD second
#define MP make_pair
LL D[100010];
LL C[110];

int main(){
	int TT;scanf("%d",&TT);
	FORE(test,1,TT){
		FOR(i,0,100000) D[i] = INF;
		LL L,n,m=0;
		scanf("%lld%lld",&L,&n);
		FOR(i,0,n){
			scanf("%lld",&C[i]);
			if(C[i]>m) m = C[i];		
		}
		D[0] = L/m;
		priority_queue<pair<LL,LL> > Q;
		Q.push(MP(-(L/m),0));
		while(!Q.empty()){
			pair<LL,LL> p = Q.top();Q.pop();
			LL cost = -p.FS, k = p.SD;
			
			if(D[k]!=cost) continue;
			
			FOR(i,0,n){
				LL A = (k+C[i])%m;
				LL c = cost+1;
				if(k+C[i]>A) c--;
				if(D[A]>c){
					D[A] = c;
					Q.push(MP(-c,A));
				}
			}
		}
		if(D[L%m]>=INF)  printf("Case #%d: IMPOSSIBLE\n",test);
		else printf("Case #%d: %lld\n",test,D[L%m]);
	}
}
