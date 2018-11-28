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

int n;
char data[250][250];

double wp[250];
double owp[250];

double calc(int i, int bad = -1) {
  int total = 0, total_win = 0;

  forn (j, n) if (data[i][j] != '.' && j != bad) {
    total++;
    if (data[i][j] == '1') total_win++;
  }

  double wp = total ? (1. * total_win / total) : 0;
  return wp;
}


int main() {
  int _t; cin >> _t;
  cout.precision(15);
  cout << fixed;

  forn (__t, _t) {
    cout << "Case #" << (__t + 1) << ": ";

    cin >> n;
    forn (i, n) forn (j, n) {
      char c = 0;
      while (c != '.' && c != '1' && c != '0') c = getchar();
      data[i][j] = c;
    }

    forn (i, n) {
      wp[i] = calc(i);

      owp[i] = 0;
      int cnt = 0;
      forn (j, n) if (data[i][j] != '.') {
        cnt++;
        owp[i] += calc(j, i);
      }
      if (cnt) owp[i] /= cnt;
    }

    cout << endl;
    forn (i, n) {
      double oowp = 0;
      int cnt = 0;
      forn (j, n) if (data[i][j] != '.') {
        oowp += owp[j];
        cnt++;
      }
      if (cnt) oowp /= cnt;

      double ans = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp;
      cout << ans << endl;
    }
  }
  

  return 0;
}
