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

#define SIZE 1250
//#define SIZE 12

double P[SIZE][SIZE];
double dp[SIZE];

int main() {
  cout.precision(15);
  cout << fixed;

  forn (i, SIZE) {
    forn (k, i + 1) {
      double v = 0;

      int m = 1;
      double f = 1;
      forn (j, k + 1) {
        if (j) f *= j;
        v += m / f;
        m *= -1;
      }

      forn (j, i - k) v /= j + 1;

      P[i][k] = v;
    }
  }

  dp[0] = 0;
  forn (i, SIZE) if (i) {
    // dp[i] = 1 + \sum_j dp[j] * P[i][j];
    double lhs = 1 - P[i][i];
    double rhs = 1;
    forn (j, i) rhs += dp[j] * P[i][j];
    dp[i] = rhs / lhs;
  }

  int _T; cin >> _T;
  forn (_t, _T) {
    cout << "Case #" << (_t + 1) << ": ";
    int n; cin >> n;
    int bad = 0;
    forn (i, n) {
      int a; cin >> a;
      if (a != i + 1) bad++;
    }
    cout << dp[bad] << endl;
    
  }

  return 0;
}
