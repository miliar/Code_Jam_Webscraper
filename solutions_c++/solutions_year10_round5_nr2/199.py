#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstring>
#include <hash_map>
#include <hash_set>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define REP(i,n) FOR(i,0,(n))
#define FORD(i,a,b) for(int i=(a),_b=(b);i>_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000000000001LL
#define maxn 1100
#define maxp 1100000

LL n, a[1000];
LL cache[maxp];

LL cal(LL k) {
  if (k < 0) return inf;
  if (k == 0) return 0;

  if (k < maxp) {
    LL & ret = cache[k];
    if (ret != -1) return ret;
    ret = inf;
    REP(i, n) {
      ret = min(ret, cal(k-a[i]) + 1);
    }
    return ret;
  }
  
  LL ret = inf;
  REP(i, n) {
    ret = min(ret, cal(k-a[i]) + 1);
  }
  return ret;
}

int main(){
  LL C, k; cin >> C;
  
  for (int T = 1; T <= C; ++T) {
    CLEAR(cache, -1);
    cin >> k >> n;
    LL max_a = 0;
    REP(i, n) {
      cin >> a[i];
      max_a = max(a[i], max_a);
    }
    LL ans = inf;

    if (n == 1) {
      if (k % a[0] == 0) {
	ans = k / a[0];
      }
    } else { 
      LL second_a = 0;
      REP(i, n) {
	if (a[i] < max_a) {
	  second_a = max(second_a, a[i]);
	}
      }
      
      for (LL i = k / max_a, j = 0; i >= 0 && j <= max_a * max_a; --i, ++j) {
	LL tmp = i + (k - i * max_a) / second_a;
	if (tmp >= ans) break;
	ans = min(i + cal(k - i * max_a), ans);
      }
    }

    if (ans != inf) cout << "Case #" << T << ": " << ans << endl;
    else cout << "Case #" << T << ": IMPOSSIBLE" << endl;
  }
}
