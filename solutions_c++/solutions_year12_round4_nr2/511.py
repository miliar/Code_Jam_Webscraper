#include <iostream>
#include <cstdio>
#include <algorithm>
#include <complex>
#include <cmath>
#include <cassert>

using namespace std;

#define MAX 1000
#define EPS 1E-10L
#define PI ((long double)(2.0 * acos(0.0)))

typedef complex<long double> pt;
typedef pair<pt, long double> circle;

int n;
int w, l;
circle C[MAX];

bool can_place(int k, pt p) {
  if (real(p) < -EPS || imag(p) < -EPS || real(p) > w + EPS || imag(p) > l + EPS)
    return false;

  for (int i = 0; i < k; i++)
    if (abs(C[i].first - p) < C[i].second + C[k].second - EPS)
      return false;
  return true;
}

void pack() {
  printf(" %.9Lf %.9Lf", real(C[0].first), imag(C[0].first));
  for (int i = 1; i < n; i++) {
    bool good = false;
    for (int j = 0; j < 100000 && !good; j++) {
      int x = rand() % (w + 1);
      int y = rand() % (l + 1);
      if (can_place(i, pt(x, y))) {
        C[i].first = pt(x, y);
        good = true;
      }
    }
    printf(" %.9Lf %.9Lf", real(C[i].first), imag(C[i].first));
    //cout << " " << real(C[i].first) << " " << imag(C[i].first);
  }
}

int main() {
  int ncases;
  long double x, y;

  cin >> ncases;
  for (int caseno = 1; caseno <= ncases; caseno++) {
    cin >> n >> w >> l;
    for (int i = 0; i < n; i++) {
      C[i].first = pt(0.0, 0.0);
      cin >> C[i].second;
    }

    printf("Case #%i:", caseno);
    pack();
    printf("\n");
    for (int i = 0; i < n; i++)
      assert(can_place(i, C[i].first));
  }

  return 0;
}
