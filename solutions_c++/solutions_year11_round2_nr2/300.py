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

vector<pair<ll, int> > data;

bool check(double t, double D) {
  double last_pos = -1e9;
  forn (i, data.size()) {
    /*
    if (fabs(data[i] - last_pos) <= t) last_pos += D;
    else if (data[i] < last_pos) return false;
    else last_pos = data[i] - t + D;
    */

   
    int cnt = data[i].second;
    double first_end = last_pos;
    if (fabs(data[i].first - last_pos) > t) {
      if (data[i].first < last_pos) return false;
      first_end = data[i].first - t;
    } else first_end = last_pos;

    double last_end = data[i].first + t;
    if (last_end - first_end < D * (cnt - 1)) return false;
    last_pos = first_end + D * cnt;
  }

  return true;
}

int main() {
  int _t; cin >> _t;
  cout.precision(15);
  cout << fixed;

  forn (__t, _t) {
    cout << "Case #" << (__t + 1) << ": ";

    ll D;
    int n; cin >> n >> D;
    data.resize(n);
    forn (i, n) cin >> data[i].first >> data[i].second;
    sort(data.begin(), data.end());

    double left = 0, right = 1e10;
    forn (_i, 250) {
      double x = (left + right) / 2;
      if (check(x, D)) right = x;
      else left = x;
    }

    cout << ((left + right) / 2) << endl;
  }
  

  return 0;
}
