#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

double xu[205], yu[205];
double xd[205], yd[205];
int u, d;

double get(double w) {
  int i = 0, j = 0;
  double S = 0.0;
  double xi = xu[0], yi = yu[0], xj = xd[0], yj = yd[0];
  while (xu[i] + 1e-10 < w || xd[j] + 1e-10 < w) {
    if (xu[i+1] < xd[j+1]) {
      double nx = xu[i+1], ny = yu[i+1];
      if (nx > w) {
        double t = (w - xi) / (nx - xi);
        nx = w;
        ny = t * (ny - yi) + yi;
      }
      S -= (xj - nx) * (yj - yi) - (xj - xi) * (yj - ny);
      i++;
      xi = nx;
      yi = ny;
    } else {
      double nx = xd[j+1], ny = yd[j+1];
      if (nx > w) {
        double t = (w - xj) / (nx - xj);
        nx = w;
        ny = t * (ny - yj) + yj;
      }
      S -= (xj - nx) * (yj - yi) - (xj - xi) * (yj - ny);
      j++;
      xj = nx;
      yj = ny;
    }
  }
  return S;
}

int main(void)
{
//  freopen("A-small-attempt0.in", "r", stdin);
//  freopen("A-small-attempt0.out", "w", stdout);
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

  scanf("%d", &nt);
  for (tn=0; tn<nt; tn++)
  {
    fprintf(stderr, "Case #%d: \n", tn+1);

    printf("Case #%d:\n", tn+1);

    int w, g;
    scanf("%d%d%d%d", &w, &u, &d, &g);

    for (int i=0; i<u; i++)
      scanf("%lf%lf", &xu[i], &yu[i]);
    xu[u] = w+1;

    for (int i=0; i<d; i++)
      scanf("%lf%lf", &xd[i], &yd[i]);
    xd[d] = w+1;

    double S = get(w);
    for (int i=1; i<g; i++) {
      double T = S * i / g;

      double l = 0, r = w;
      for (int tt=0; tt<100; tt++) {
        double m = (l + r) / 2;
        if (get(m) > T) {
          r = m;
        } else {
          l = m;
        }
      }
      printf ("%.20lf\n", l);
    }
  }
  return 0;
}
