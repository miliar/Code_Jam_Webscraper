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

int n, dist, pos, tmp;
VI v;

bool check(double mid) {
  double last = v[0] - mid;
  FOR(i, 1, v.size() - 1) {
    double prop = 0;
    if (last + dist <= v[i] - mid) {
      prop = v[i] - mid;
    } else {
      if (fabs(last + dist - v[i]) <= mid) {
        prop = last + dist;
      } else {
        return false;
      }
    }
    last = prop;
  }
  return true;
}

int main() {
	int ile;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
    v.clear();
    scanf("%d%d", &n, &dist);
    REP(i, n) {
      scanf("%d%d", &pos, &tmp);
      REP(j, tmp) {
        v.push_back(pos);
      }
    }
    sort(v.begin(), v.end());

    double pocz = 0, kon = 1000000000;
    
    REP(ile, 500) {
      double mid = (pocz + kon) / 2;
      if (check(mid)) {
        kon = mid;
      } else {
        pocz = mid;
      }
    }

		printf("Case #%d: %.9lf\n",iile, pocz);
	}
	return 0;
}

