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

int wynik=0,a,b,c,d,x0,y0,n,m;
vector<pair<int,int> > tab;
scanf("%d%d%d%d%d%d%d%d",&n,&a,&b,&c,&d,&x0,&y0,&m);
LL A=a,B=b,C=c,D=d,X0=x0,Y0=y0,M=m;
LL XX,YY;
int x,y;
tab.push_back(make_pair(x0,y0));
XX=x0; YY=y0;
FOR(i,1,n-1) {
    XX=(A*XX+B)%M;
    YY=(C*YY+D)%M;
    
    x=XX; y=YY;
    tab.push_back(make_pair(x,y));
    }



LL X1,Y1;
FOR(i,0,n-3) FOR(j,i+1,n-2) FOR(k,j+1,n-1) {
    X1=LL(tab[i].first)+LL(tab[j].first)+LL(tab[k].first);
    Y1=LL(tab[i].second)+LL(tab[j].second)+LL(tab[k].second);
    
    if (X1%3==0 && Y1%3==0) wynik++;
    }


printf("Case #%d: %d\n",cas,wynik);
}

return 0;
}
