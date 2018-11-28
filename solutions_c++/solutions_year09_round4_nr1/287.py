#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include <ext/hash_set>
#include <ext/hash_map>
#include <ext/numeric>
#include <ext/functional>
#include <ext/rope>
#include <ext/rb_tree>
#include <ext/iterator>
#include <ext/slist>

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define REP(i, n) for(int i=0; i<n; ++i)
#define REPD(i, n) for(int i=(n)-1; i>=0; --i)
#define FOR(i, b, e) for(typeof(e) i=b; i!=e; ++i)

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

// BEGIN CUT HERE
#define RUNCASE -1
// END CUT HERE

void go() {
  int n;
  cin >> n;
  VI a;
  REP(i, n) {
    string s;
    cin >> s;
//    cout << s << endl;
    int tmp=0;
    REP(j, n) if(s[j]=='1') tmp=j;
    a.PB(tmp);
  }
  //REP(i, n) cout << a[i] << " "; cout << endl;
  VI t(n,-1);
  REP(i, n) {
    FOR(j, a[i], n) if(t[j]==-1) {t[j]=i; break;}
  }
  //REP(i, n) cout << t[i] << " "; cout << endl;
  int res=0;
  REP(i, n) {
    FOR(j, i+1, n) if(t[j]<t[i]) res++;
  }
  cout << res << endl;
}

int main() {
  int nruns;
  cin >> nruns;
  REP(i, nruns) {
    printf("Case #%d: ", i+1);
    go();
  }
}
