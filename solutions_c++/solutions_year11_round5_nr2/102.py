// Philip_PV

#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <ctime>
#include <memory.h>
//#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<double, double> pdd;
typedef pair<int, int> pii;

#ifdef _DEBUG
  #define dbg(x) { cerr << #x << " = " << x << endl; }
#else
  #define dbg(x) ;
#endif

#define forn(_i,_n) for (int _i = 0; _i < (int)(_n); ++_i)
#define mp make_pair


int main() {
  cout.precision(15);
  cout << fixed;
  int _T; cin >> _T;
  for (int _t = 1; _t <= _T; ++_t) {
    cout << "Case #" << _t << ": ";


    vector<int> cnt(11000, 0);
    int n; cin >> n;
    forn (i, n) {
      int v; cin >> v;
      cnt[v - 1]++;
    }

    int ans = n;
    int open[11000];
    int m = 0;
    forn (i, 11000) {
      int v = cnt[i];
      if (v >= m) {
        forn (j, m) open[j]++;
        while (m < v) open[m++] = 1;
        
      } else {
        sort(open, open + m);
        ans = min(ans, open[v]);
        forn (j, v) open[j]++;
      }
      m = v;
    }

    cout << ans << endl;
  }

  

  return 0;
}
