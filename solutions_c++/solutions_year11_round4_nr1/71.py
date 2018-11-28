#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

typedef pair <double, double> pnt;
#define x first
#define y second

int main (void) {
  int tn;
  scanf ("%d", &tn);
  for (int tt = 1; tt <= tn; tt++) {
    int X, S, R, t, N;
    scanf ("%d%d%d%d%d", &X, &S, &R, &t, &N);
    vector <pnt> v;
    for (int i = 0; i < N; i++) {
      int a, b, w;
      scanf ("%d%d%d", &a, &b, &w);
      v.push_back(pnt (S + w, b - a));
      X -= b - a;
    }
    v.push_back(pnt (S, X));

    sort (v.begin(), v.end());
    double have = t, res = 0;
    for (int i = 0; i < (int)v.size(); i++) {
      double all = v[i].y / (R - S + v[i].x);
      if (all < have) {
        res += all;
        have -= all;
      } else {
        v[i].y -= (v[i].x + R - S) * have;
        res += have;
        have = 0;
        res += v[i].y / v[i].x;
      }
    }

    printf ("Case #%d: %.20lf\n", tt, res);
  }
  return 0;
}