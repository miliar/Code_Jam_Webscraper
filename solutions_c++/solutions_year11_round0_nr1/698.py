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
    int pos1 = 1, pos2 = 1;
    int last1 = 0, last2 = 0;

    int k; cin >> k;
    forn (i, k) {
      char c = 0;
      while (c != 'B' && c != 'O') c = getchar();
      int v; cin >> v;

      if (c == 'B') {
        int dt = abs(v - pos1) + 1;
        pos1 = v;
        last1 = max(last2 + 1, last1 + dt);

      } else {
        int dt = abs(v - pos2) + 1;
        pos2 = v;
        last2 = max(last2 + dt, last1 + 1);
      }
    }

    cout << max(last1, last2) << endl;
  }

  return 0;
}
