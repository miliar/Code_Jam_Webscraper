#include <cstdio>
#include <iostream>

using namespace std;

const int N = 200;

int x[N];
int v[N];

bool valid(double t, int n, int d) {
  double l = x[0] - t;
  double r = l + d * (double)(v[0]-1);
  if (r - x[0] > t+1e-10) return false;

  for (int i = 1; i < n; i++) {
    l = r + d;
    if (x[i] >= l) {
      double ll = x[i] - t;
      if (ll < l) ll = l;
      r = ll + d * (double)(v[i]-1);
      if (r - x[i] > t+1e-10) return false;
    } else {
      double dist = l - x[i];
      if (dist > t+1e-10) return false;
      double ll = l;
      r = ll + d * (double)(v[i]-1);
      if (r - x[i] > t) return false;
    }
  }

  return true;
}

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) { 
    int c, d; cin >> c >> d;
    for (int i = 0; i < c; i++) {
      cin >> x[i] >> v[i];
    }

    double lo = 0, hi = 1e9;
    while (lo+1e-10 < hi) {
      double t = (lo+hi) / 2;
      if (valid(t, c, d)) hi = t; else lo = t;
    }
    printf("Case #%d: %.9lf\n", tt, hi);
  }
  return 0;
}

