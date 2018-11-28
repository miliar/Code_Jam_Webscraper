using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x){ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x){ stringstream s; s << x; int r; s >> r; return r; }

#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define foreach(x, v) for (typeof (v).begin() x = (v).begin(); x != (v).end(); ++x)
#define D(x) cout << #x " = " << (x) << endl

struct circle {
  int x;
  int y;
  int r;
};

typedef long double ldouble;

ldouble solve(){
  int n;
  cin >> n;
  vector<circle> c(n);
  for (int i=0; i<n; ++i){
    cin >> c[i].x >> c[i].y >> c[i].r;
  }
  if (n == 1) return c[0].r;
  if (n == 2) return max(c[0].r, c[1].r);

  ldouble ans = 1e100;
  for (int i=0; i<n; ++i){
    for (int j=i+1; j<n; ++j){
      int k = 0;
      while (k == i || k == j) k++;

      ldouble maybe = 0.5 * (hypot(c[i].x - c[j].x, c[i].y - c[j].y) + c[i].r + c[j].r);
      //printf("distance between (%d, %d) and (%d, %d) is %lf\n", c[i].x, c[i].y, c[j].x, c[j].y, hypot(c[i].x - c[j].x, c[i].y - c[j].y));
      if (c[k].r > maybe) maybe = c[k].r;
      if (maybe < ans) ans = maybe;
    }
  }
  return ans;
}

int main(){
  int Casos;
  cin >> Casos;
  for (int Caso=1; Caso<=Casos; ++Caso){
    printf("Case #%d: ", Caso);
    printf("%.10lf\n", (double)solve());
  }
  return 0;
}
