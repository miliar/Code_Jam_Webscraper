// By mirosuaf
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
#include <queue>
#include <set>
#include <map>


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
typedef vector<int> VI; 

bool tab[1020][1020];
bool used[1020];
int pocz,kon,wanted,wynik;

bool prime(int x) {
    FOR(i,2,x-1) if (x%i==0) return false;
    return true;
    }


void dfs(int x) {
    used[x]=true;
    FOR(xx,pocz,kon) if (used[xx]==false && tab[x][xx]) dfs(xx);
    }


int main() {
int ile;
scanf("%d",&ile);
FOR(cas,1,ile) {

REP(i,1020) REP(j,1020) tab[i][j]=false;
REP(i,1020) used[i]=false;
wynik=0;
scanf("%d%d%d",&pocz,&kon,&wanted);
vector<int> pp;
int _w;
FOR(i,2,1000) if (prime(i)) pp.push_back(i);
int ile=0;


FOR(i,pocz,kon) { 
FOR(j,i+1,kon) {
	_w=-1;
	REP(k,pp.size()) if (i%pp[k]==0 && j%pp[k]==0) _w=pp[k];
	    
	if (_w>=wanted) { tab[i][j]=true; tab[j][i]=true; }
	}
}

FOR(i,pocz,kon) used[i]=false;

FOR(i,pocz,kon) if (used[i]==false) {
    wynik++;
    dfs(i);
    }
printf("Case #%d: %d\n",cas,wynik);
}

return 0;
}
