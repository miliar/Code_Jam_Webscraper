// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
const int MAXN= 20000;
typedef vector<int> VI; 

int main() {
int ile;
scanf("%d",&ile);
FOR(iile,1,ile) {

int n,expected,wrt;
int tab[MAXN][2], deg[MAXN],c[MAXN],g[MAXN],dd;
bool lisc[MAXN]; 
REP(i,MAXN) { deg[i]=0; c[i]=0; g[i]=0; lisc[i]=false; }
int wz1;

scanf("%d%d",&n,&expected);
queue<int> kolej;
REP(i,MAXN) REP(j,2) tab[i][j]=INF; 

FOR(i,1,(n-1)/2) { scanf("%d%d",&g[i],&c[i]); deg[i]=2; }
FOR(j,(n-1)/2+1,n) { scanf("%d",&wrt); kolej.push(j); lisc[j]=true; tab[j][wrt]=0; }

while (!kolej.empty()) {
    wz1=kolej.front(); kolej.pop();
    
    if (lisc[wz1]==true) {
	    deg[wz1/2]--;
	    if (deg[wz1/2]==0) kolej.push(wz1/2);
	    } else
    
	if (lisc[wz1]!=true) {

		if (g[wz1]==1 || (g[wz1]==0 && c[wz1]==1) ) {
		
			if (g[wz1]==0) dd=1; else dd=0;
			
			tab[wz1][0]=min(tab[wz1][0],tab[wz1*2][0]+tab[wz1*2+1][0]+dd);
			tab[wz1][0]=min(tab[wz1][0],tab[wz1*2][0]+tab[wz1*2+1][1]+dd);
			tab[wz1][0]=min(tab[wz1][0],tab[wz1*2][1]+tab[wz1*2+1][0]+dd);
			
			tab[wz1][1]=min(tab[wz1][1],tab[wz1*2][1]+tab[wz1*2+1][1]+dd);
			}	

	
		if (g[wz1]==0 || (g[wz1]==1 && c[wz1]==1) ) {
			if (g[wz1]==1) dd=1; else dd=0;
			
			tab[wz1][0]=min(tab[wz1][0],tab[wz1*2][0]+tab[wz1*2+1][0]+dd);

			tab[wz1][1]=min(tab[wz1][1],tab[wz1*2][0]+tab[wz1*2+1][1]+dd);
			tab[wz1][1]=min(tab[wz1][1],tab[wz1*2][1]+tab[wz1*2+1][0]+dd);
			tab[wz1][1]=min(tab[wz1][1],tab[wz1*2][1]+tab[wz1*2+1][1]+dd);
			}
	    deg[wz1/2]--; if (deg[wz1/2]==0) kolej.push(wz1/2);
	    }
    }

printf("Case #%d: ",iile);
if (tab[1][expected]!=INF) printf("%d\n",tab[1][expected]); else printf("IMPOSSIBLE\n");
}
return 0;
}

