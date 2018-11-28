// {{{
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PI;
typedef pair<LD,LD> PD;

#define VAR(v,n) __typeof(n) v=(n)
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<=(b); i++)
#define FORD(i,a,b) for(int i=(a); i>=(b); i--)
#define FORE(i,c) for(VAR(i,(c).begin()); i!=(c).end(); i++)
#define CLR(A,v) memset((A),v,sizeof((A)))

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define ALL(x) x.begin(),x.end()
#define SIZE(x) ((int)(x).size())
// }}}
//  Bipartiple Matching from our ACM team libary (Piotr Niedzwiedz, Wojciech Tyczynski, Wojciech Smietanka) 

/* maksymalne skojarzenie w grafie dwudzielnym
 * funkcji BipartiteMatching dostaje na wejsciu
 * ilosc wierzcholkow grafu
 * ponadto istnieje globalna tablica lewy, mowiaca
 * po ktorej stronie grafu znajduje sie dany wierzcholek
 * funkcja zwraca wektor, skojarzen */
#define MAX_N 7000

bool lewy[MAX_N];			/* po ktorej stronie jest wierzcholek */
char vis[MAX_N];			/* czy wierzcholek zostal odwiedzony  */
int skoj[MAX_N];			/* z czym dany wierzcholek jest skojarzony */
VI kraw[MAX_N];			/* listy sasiedztwa */ 
char s[100][111]; 
int nm[111][111],N,M,T;  

inline bool dfsMatching(int x) {
	vis[x]=1;
	REP(i,SIZE(kraw[x]))
		if (skoj[kraw[x][i]]==-1 || (!vis[skoj[kraw[x][i]]] && dfsMatching(skoj[kraw[x][i]]))) {
			skoj[x]=kraw[x][i];
			skoj[kraw[x][i]]=x;
			return true;
		}
	return false;
}


inline VI BipartiteMatching(int n) {
	REP(i,n) skoj[i]=-1;

	while (1) {
		bool f=false;
		REP(i,n) vis[i]=0;
		REP(i,n) if (lewy[i] && !vis[i] && skoj[i]==-1 && dfsMatching(i))
			f=true;
		if (!f) break;
	}

	VI res;
	REP(i,n) res.PB(skoj[i]);
	return res;
}

bool gut(int a,int b){ 
   if(a<0 || b<0 || a>=M || b>=N) return 0; 
   return s[a][b]!='x'; 
} 

int main() {
	scanf("%d",&T); 
	FOR(tc,1,T){ 
          scanf("%d%d",&M,&N); 

		  REP(i,M) scanf("%s",s[i]); 
      int   n=0; 

		 REP(i,M) REP(j,N) if(s[i][j]!='x') nm[i][j]=n++;
	      REP(i,n) kraw[i].clear(); 	 
         
	      int dy[4]={0,0,-1,-1},dx[4]={-1,1,-1,1}; 	 

		 REP(i,M) REP(j,N) if(s[i][j]!='x'){ 
			 int a,b; 
			 REP(k,4) if( gut( (a=i+dy[k]),(b=j+dx[k]))){
				 kraw[nm[i][j]].PB(nm[a][b]);
				 kraw[nm[a][b]].PB(nm[i][j]); 
			 } 
			 lewy[nm[i][j]]=(j%2==1); 
		 } 
 
		 VI res=BipartiteMatching(n);
		 int sk=0; 
		 FORE(e,res) if( *e!=-1) ++sk; 
//        printf("%d %d\n",sk,n); 
		  
		printf("Case #%d: %d\n",tc,n-sk/2); 
	} 
	return 0;
}

