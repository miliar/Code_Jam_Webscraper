#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

template<typename T> ostream& operator<<( ostream &os, const vector<T> &v ) { os << "{"; for ( typename vector<T>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " " << *vi; } os << " }"; return os; }
template<> ostream& operator<<( ostream &os, const vector<string> &v ) { os << "{"; for ( vector<string>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " \"" << *vi << "\""; } os << " }"; return os; }
template<typename T, typename U> ostream& operator<<( ostream &os, const pair<T, U> &P ) { return os << "(" << P.first << ", " << P.second << ")"; }
template<typename T> ostream& operator<<( ostream &os, const set<T> &S ) { return os << vector<T>( S.begin(), S.end() ); }
template<typename T, typename U> ostream& operator<<( ostream &os, const map<T, U> &M ) { for ( typename map<T, U>::const_iterator mi=M.begin(); mi!=M.end(); ++mi ) { os << mi->first << " => " << mi->second << endl; } return os; }

struct Point { int x, y; };

double under(const vector<Point> &pts, double x) {
  int n = pts.size();
  bool done = 0;
  double res = 0;
  for (int i=1; i<n && !done; ++i) {
    double
      x1 = pts[i-1].x, x2 = pts[i].x,
      y1 = pts[i-1].y, y2 = pts[i].y;
    if (x < x2) {
      y2 = y1 + (x-x1)/(x2-x1) * (y2-y1);
      x2 = x;
      done = true;
    }
    res += (x2-x1) * (y2+y1);
  }
  return 0.5*res;
}

int main(void) {
  cin.sync_with_stdio(0);

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    int W, L, U, G;
    cin >> W >> L >> U >> G;
    vector<Point> lower(L), upper(U);
    for (int i=0; i<L; ++i) cin >> lower[i].x >> lower[i].y;
    for (int i=0; i<U; ++i) cin >> upper[i].x >> upper[i].y;

    double total = under(upper, W) - under(lower, W);
    printf("Case #%d:\n", tt);

    for (int i=1; i<G; ++i) {
      double target = total * i/G;
      double lo = 0, hi = W;
      for (int iter=0; iter<100; ++iter) {
        double x = (lo+hi)/2;
        if (under(upper, x) - under(lower, x) < target) {
          lo = x;
        } else {
          hi = x;
        }
      }
      printf("%.9f\n", hi);
    }
  }

  return 0;
}
