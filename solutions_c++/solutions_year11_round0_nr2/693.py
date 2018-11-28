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

    int C; cin >> C;
    vector<string> v; v.resize(C);
    forn (i, C) cin >> v[i];

    int D; cin >> D;
    vector<string> b; b.resize(D);
    forn (i, D) cin >> b[i];

    int n; cin >> n;
    string s; cin >> s;

    string result;
    forn (i, s.size()) {
      result.push_back(s[i]);
      bool ok = true;
      while (ok && result.size() > 1) {
        ok = false;
        char last = result[result.size() - 1];
          char pre = result[result.size() - 2];
        forn (j, v.size())
          if ((last == v[j][0] && pre == v[j][1]) || (last == v[j][1] && pre == v[j][0])) {
            ok = true;
            result.pop_back();
            result.pop_back();
            result.push_back(v[j][2]);
            break;
          }

        forn (j, b.size())
          forn (j1, result.size())
            forn (j2, result.size())
              if (result[j1] == b[j][0] && result[j2] == b[j][1])
                result.clear();
      }
    }

    cout << "[";
    forn (i, result.size()) {
      if (i) cout << ", ";
      cout << result[i];
    }

    cout << "]" << endl;
  }

  return 0;
}
