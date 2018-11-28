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

int main() {
int ile;
scanf("%d",&ile);
FOR(cas,1,ile) {
int n,K,xx,tab[5020];
vector <int> v;
scanf("%d",&K);
scanf("%d",&n); REP(i,n) { scanf("%d",&xx); v.push_back(xx); }

FOR(i,1,K) tab[i]=-1;

int poz=0,cnt=0;
FOR(i,1,K) {
    cnt=0;
    while (cnt<i) {
	poz++; if (poz==K+1) poz=1;
	if (tab[poz]==-1) cnt++;
	}
    tab[poz]=i;
    }
printf("Case #%d:",cas);
REP(i,v.size()) printf(" %d",tab[v[i]]); printf("\n");
}

return 0;
}
