#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cmath>
#include <cctype>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define FOR(i, begin, end) for(int i = (begin); i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

#define sqr(x) ((x)*(x))

const double PI = 3.14159265358979323846;

double integral(double r, double x) {
  double t = sqrt(sqr(r)-sqr(x));
  return 0.5*x*t + 0.5*sqr(r)*atan(x/t);
}

int main() {
  int cases;
  cin >> cases;
  for (int cs = 1; cs <= cases; cs++) {
    double R, t, r, g, f;
    cin >> f >> R >> t >> r >> g;

    t += f;
    r += f;
    g -= 2*f;
    t = R-t;

    double p = 1;
    if (g > 0 && r < t) {
      double S = 0;

      vector<double> a, b;
      a.push_back(r);
      b.push_back(r+g);
      while (b.back()+2*r < t) {
        a.push_back(b.back()+2*r);
        b.push_back(a.back()+g);
      }

      int n = a.size();
      FOR(i, 0, n) {
        double c = 0;
        if (b[i] < t) 
          c = sqrt(sqr(t)-sqr(b[i]));
        double d = sqrt(sqr(t)-sqr(a[i]));

        FOR(j, 0, n) if (a[j] < c) {
          double bb = b[j] <? c;
          S += g*(bb-a[j]);
        }

        FOR(j, 0, n) if (a[j] < d && b[j] > c) {
          double aa = a[j] >? c;
          double bb = b[j] <? d;
          S += integral(t, bb) - integral(t, aa) - a[i]*(bb-aa);
        }
      }

      p = 1-4*S/sqr(R)/PI;
    }

    cout.precision(9);
    cout << "Case #" << cs << ": " << p << endl;
  }
}
