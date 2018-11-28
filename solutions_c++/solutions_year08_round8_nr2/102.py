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
const int MMM=10000;
typedef vector<int> VI; 

int main() {
int ile;
scanf("%d",&ile);
FOR(iile,1,ile) {

map<string,int> mapa;
int kto,pocz,kon,prop,nazwy=-1;
char nz[100];
string NZ;
vector<pair<int,int> > tab[300];

scanf("%d",&prop);

REP(i,prop) {
    scanf("%s%d%d",nz,&pocz,&kon);
    NZ=nz;
    if (mapa.find(NZ)==mapa.end()) {
	    nazwy++;
	    mapa[NZ]=nazwy;
	    }
    kto=mapa[NZ];
    
    tab[kto].push_back(make_pair(pocz,kon));
    }

REP(i,nazwy) sort(tab[i].begin(),tab[i].end()); 

int t[MMM*2];
int wynik=INF;
nazwy++;

REP(W1,nazwy) {

vector<pair<int,int> > chce;
   REP(i,tab[W1].size()) chce.push_back(make_pair(tab[W1][i].first,tab[W1][i].second));
	    sort(chce.begin(),chce.end());
	    FOR(i,1,MMM) t[i]=INF;
	    t[0]=0;
	    REP(i,chce.size()) {
	    if (t[chce[i].first-1]+1<t[chce[i].second]) {
		    t[chce[i].second]=t[chce[i].first-1]+1;
		    FORD(j,chce[i].second-1,0) if (t[j]>t[chce[i].second]) t[j]=t[chce[i].second];
		    }    	    
		}
	if (t[MMM]<wynik) wynik=t[MMM];
}




REP(W1,nazwy) {
FOR(W2,W1+1,nazwy-1) {
vector<pair<int,int> > chce;
   REP(i,tab[W1].size()) chce.push_back(make_pair(tab[W1][i].first,tab[W1][i].second));
   REP(i,tab[W2].size()) chce.push_back(make_pair(tab[W2][i].first,tab[W2][i].second));

	    sort(chce.begin(),chce.end());
	    FOR(i,1,MMM) t[i]=INF;
	    t[0]=0;
	    REP(i,chce.size()) {
	    if (t[chce[i].first-1]+1<t[chce[i].second]) {
		    t[chce[i].second]=t[chce[i].first-1]+1;
		    FORD(j,chce[i].second-1,0) if (t[j]>t[chce[i].second]) t[j]=t[chce[i].second];
		    }    	    
		}
	if (t[MMM]<wynik) wynik=t[MMM];

}
}

REP(W1,nazwy) {
FOR(W2,W1+1,nazwy-1) {
FOR(W3,W2+1,nazwy-1) {
vector<pair<int,int> > chce;
   REP(i,tab[W1].size()) chce.push_back(make_pair(tab[W1][i].first,tab[W1][i].second));
   REP(i,tab[W2].size()) chce.push_back(make_pair(tab[W2][i].first,tab[W2][i].second));
   REP(i,tab[W3].size()) chce.push_back(make_pair(tab[W3][i].first,tab[W3][i].second));

	    sort(chce.begin(),chce.end());
	    FOR(i,1,MMM) t[i]=INF;
	    t[0]=0;
	    REP(i,chce.size()) {
	    if (t[chce[i].first-1]+1<t[chce[i].second]) {
		    t[chce[i].second]=t[chce[i].first-1]+1;
		    FORD(j,chce[i].second-1,0) if (t[j]>t[chce[i].second]) t[j]=t[chce[i].second];
		    }    	    
		}
	if (t[MMM]<wynik) wynik=t[MMM];
}
}
}

	





printf("Case #%d: ",iile);
if (wynik==INF) printf("IMPOSSIBLE\n"); else printf("%d\n",wynik);


}
return 0;
}

