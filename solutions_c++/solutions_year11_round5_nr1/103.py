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




    int W, G;
    int n1, n2; cin >> W >> n2 >> n1 >> G;
    vector<pii> _v1, _v2;
    _v1.resize(n1); _v2.resize(n2);
    forn (i, n2) cin >> _v2[i].first >> _v2[i].second;
    forn (i, n1) cin >> _v1[i].first >> _v1[i].second;
    

    set<int> _xs; _xs.insert(0); _xs.insert(W);
    forn (i, n1) _xs.insert(_v1[i].first);
    forn (i, n2) _xs.insert(_v2[i].first);

    int n = _xs.size();
    vector<int> xs(_xs.begin(), _xs.end());
    vector<double> y_up, y_down;
    y_up.resize(n), y_down.resize(n);

    forn (i, n) {
      int x = xs[i];
      int j1 = 0; while (j1 + 1 < n1 && _v1[j1 + 1].first < x) j1++;
      int j2 = 0; while (j2 + 1 < n2 && _v2[j2 + 1].first < x) j2++;

      double y1 = _v1[j1].second + (double)(_v1[j1 + 1].second - _v1[j1].second) / (_v1[j1 + 1].first - _v1[j1].first) * (x - _v1[j1].first);
      double y2 = _v2[j2].second + (double)(_v2[j2 + 1].second - _v2[j2].second) / (_v2[j2 + 1].first - _v2[j2].first) * (x - _v2[j2].first);

      y_up[i] = y1;
      y_down[i] = y2;
    }

    double S2 = 0;
    forn (i, n - 1) {
      S2 += (y_up[i + 1] + y_up[i]) * (xs[i + 1] - xs[i]);
      S2 -= (y_down[i + 1] + y_down[i]) * (xs[i + 1] - xs[i]);
    }

    S2 /= G;

    double y1 = y_up[0], y2 = y_down[0];
    double x = 0;
    int i = 1;

    cout << endl;
    forn (_i, G - 1) {

      double A = 0;

      while (true) {
        double area_up = (y1 + y_up[i]) * (xs[i] - x);
        double area_down = (y2 + y_down[i]) * (xs[i] - x);
        double area = area_up - area_down;
        if (A + area < S2) {
          A += area;
          y1 = y_up[i];
          y2 = y_down[i];
          x = xs[i];
          i++;
        } else break;
      }

      double l = x, r = xs[i];
      double _x, _y1, _y2;

      forn (_j, 100) {
        _x = (l + r) / 2;
        _y1 = y_up[i - 1] + (y_up[i] - y_up[i - 1]) / (xs[i] - xs[i - 1]) * (_x - xs[i - 1]);
        _y2 = y_down[i - 1] + (y_down[i] - y_down[i - 1]) / (xs[i] - xs[i - 1]) * (_x - xs[i - 1]);

        double area_up = (y1 + _y1) * (_x - x);
        double area_down = (y2 + _y2) * (_x - x);
        double area = area_up - area_down;
        if (A + area < S2)
          l = _x;
        else
          r = _x;
      }

      x = _x;
      y1 = _y1;
      y2 = _y2;

      cout << x << endl;

    }
  }

  

  return 0;
}
