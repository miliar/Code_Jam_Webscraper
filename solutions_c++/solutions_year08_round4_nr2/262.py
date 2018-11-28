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
typedef vector<int> VI; 

int main() {
int ile;
scanf("%d",&ile);
bool done;
FOR(iile,1,ile) {
done=false;
int n,m,area,tmp,dfx1,dfy1,dfx2,dfy2;

scanf("%d%d%d",&n,&m,&area);

printf("Case #%d:",iile);

if (n*m<area) done=false; else {
FOR(x1,0,n) FOR(y1,0,m) {
FOR(x2,0,n) FOR(y2,0,m) {
FOR(x3,0,n) FOR(y3,0,m) {

    dfx1=x2-x1;
    dfy1=y2-y1;
    
    dfx2=x3-x1;
    dfy2=y3-y1;
    
    tmp=abs(dfx1*dfy2-dfx2*dfy1);
if (tmp==area) {
    printf(" %d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);    
    done=true;
    x1=n; x2=n; x3=n;
    y1=m; y2=m; y3=m;
    }
    } } }
}
if (done==false) printf(" IMPOSSIBLE\n");


}
return 0;
}

