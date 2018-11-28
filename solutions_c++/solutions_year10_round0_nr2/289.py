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
	FOR(iile,1,ile) {
        int n, t[10];
        scanf("%d",&n);
        int mi = INF, wynik, moje, maxio=-1;
        REP(i,n) {
            scanf("%d",&t[i]);
            mi = min(mi, t[i]);
        }
        sort(t, t+n);
        int gc=-1;
        REP(i, n) FOR(j,i+1,n-1) if (t[j]>t[i]) {
            if (gc==-1) gc=t[j]-t[i]; else gc = __gcd(gc, t[j]-t[i]);
        }
		if ((t[0]%gc)!=0) wynik=gc-(t[0]%gc); else wynik=0;
        printf("Case #%d: %d\n",iile,wynik);
	}
	return 0;
}

