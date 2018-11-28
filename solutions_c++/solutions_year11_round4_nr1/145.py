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

/*
#define x first
#define y second
//*/

inline int nextint() {
  int res = 0;
  int neg = 1;

  char c = 0; while (c != '-' && (c < '0' || c > '9')) c = getchar();
  if (c == '-') c = '0', neg = -1;
  while (c >= '0' && c <= '9') {
    res = res * 10 + c - '0';
    c = getchar();
  }
  return neg * res;
}

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
  for (int _t = 1; _t <= _T; _t++) {
    cerr << _t << " ";

    cout << "Case #" << _t << ": ";

    vector<pii> data;

    int x, s, r, t, n; cin >> x >> s >> r >> t >> n;
    int len0 = x;
    forn (i, n) {
      int bi, ei, wi;
      cin >> bi >> ei >> wi;
      len0 -= ei - bi;

      data.push_back(mp(wi, ei - bi));
    }
    data.push_back(mp(0, len0));
    //sort(data.begin(), data.end(), greater<pii>());
    sort(data.begin(), data.end());

    double ans = 0;
    double R = t;
    forn (i, data.size()) {
      double need_t_fast = (double)data[i].second / (data[i].first + r);

      if (need_t_fast <= R) {
        R -= need_t_fast;
        ans += need_t_fast;

      } else {
        ans += R;
        double need = data[i].second - (data[i].first + r) * R;
        R = 0;
        ans += need / (data[i].first + s);
      }
    }

    cout << ans << endl;
  }

  return 0;
}
