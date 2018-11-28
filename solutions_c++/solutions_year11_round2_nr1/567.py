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
const int MAXN = 120;

typedef vector<int> VI; 

int main() {
	int ile;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
    int n;
    int won[MAXN], lost[MAXN];
    double wp[MAXN], owp[MAXN], oowp[MAXN], result[MAXN];
    REP(i, MAXN) {
      wp[i] = 0;
      won[i] = 0;
      lost[i] = 0;
      owp[i] = 0;
      oowp[i] = 0;
      result[i] = 0;
    }

    scanf("%d", &n);
    vector<string> v;
    REP(i, n) {
      char tmp[230];
      scanf("%s", tmp);
      v.push_back(tmp);
    }
    REP(i, n) {
      REP(j, n) {
        if (v[i][j] == '1') won[i]++;
        if (v[i][j] == '0') lost[i]++;
      }
    }
    REP(i, n) wp[i] = (double)won[i]/(won[i] + lost[i]);


    REP(i, n) {
      int il = 0;
      REP(j, n) if (v[i][j] == '0' || v[i][j] == '1') {
        int tmpw = won[j];
        int tmpl = lost[j];
        if (v[i][j] == '0') tmpw--; else tmpl--;

        assert(tmpw+tmpl != 0);
        if (tmpw + tmpl != 0) owp[i] += (double)tmpw/(tmpw+tmpl);
        il++;
      }
      assert(il != 0);
      if (il != 0) owp[i] /= il;
    }
    
    REP(i, n) {
      int il = 0;
      REP(j, n) if (v[i][j] == '1' || v[i][j] == '0') {
        oowp[i] += owp[j];
        il++;
      }
      assert(il != 0);
      if (il != 0) oowp[i] /= il;
    }

    REP(i, n) {
      result[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
    }
    printf("Case #%d: \n",iile);
    REP(i, n) {
      printf("%.9lf\n", result[i]);
    }
	}
	return 0;
}

