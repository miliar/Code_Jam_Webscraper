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

inline int nextint() {
  int res = 0;
  char c = 0; while (c < '0' || c > '9') c = getchar();
  while (c >= '0' && c <= '9') {
    res = res * 10 + c - '0';
    c = getchar();
  }
  return res;
}

#ifdef _DEBUG
  #define dbg(x) { cerr << #x << " = " << x << endl; }
#else
  #define dbg(x) ;
#endif

#define forn(_i,_n) for (int _i = 0; _i < (int)(_n); ++_i)
#define mp make_pair

int main() {
  int _T; cin >> _T;
  forn (_t, _T) {
    cout << "Case #" << (_t + 1) << ": ";

    int n; cin >> n;
    vector<int> data; data.resize(n);
    forn (i, n) cin >> data[i];

    int v = 0;
    forn (i, n) v ^= data[i];
    if (v) cout << "NO" << endl;
    else {
      sort(data.begin(), data.end());
      int ans = 0;
      forn (i, data.size()) if (i) ans += data[i];
      cout << ans << endl;
    }
  }

  return 0;
}
