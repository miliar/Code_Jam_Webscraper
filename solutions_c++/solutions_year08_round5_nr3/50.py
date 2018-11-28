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
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

char bufor[20][20];
int tab[2000];
int old[2000];
int n,m;

int main() {
int ile;
scanf("%d",&ile);
FOR(iile,1,ile) {

scanf("%d%d\n",&n,&m);

REP(i,n) {
	gets(bufor[i]);
}

REP(i,(1<<n)) tab[i] = 0;
REP(i,(1<<n)) old[i] = 0;

REP(j,m) {
	int akt_zle = 0;
	REP(i,n) {akt_zle *= 2; if(bufor[i][j]=='x') akt_zle++;}

	REP(nast,(1<<n)) if((nast&akt_zle)==0){
		int ilu = 0;
		REP(i,n) if (nast&(1<<i)) ilu++;
		REP(poprz,(1<<n)) {
			bool ok = true;
			REP(i,n) {
				if ((poprz&(1<<i)) && (nast&(1<<i))) ok = false;
				if ((poprz&(1<<(i+1))) && (nast&(1<<i))) ok = false;
				if ((poprz&(1<<i)) && (nast&(1<<(i+1)))) ok = false;
			}
			if (ok) tab[nast] = max(tab[nast], ilu+ old[poprz]);
		}
	}
	REP(i, (1<<n)) old[i] = tab[i];
	REP(i, (1<<n)) tab[i] = 0;
}

int maxik = 0;
REP(i, (1<<n)) maxik = max(maxik,old[i]);


printf("Case #%d: %d\n",iile, maxik);
}
return 0;
}

