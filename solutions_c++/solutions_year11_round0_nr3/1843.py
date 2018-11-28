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
#include <cassert>

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
	int ile, n, mini, x, res, tot;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
    scanf("%d", &n);
    mini = INF;
    res = 0;
    tot = 0;
    REP(i, n) {
      scanf("%d", &x);
      mini = min(mini, x);
      res ^= x;
      tot += x;
    }
    if (res != 0) {
      printf("Case #%d: NO\n", iile);
    } else {
      printf("Case #%d: %d\n",iile, tot - mini);
    }
	}
	return 0;
}

