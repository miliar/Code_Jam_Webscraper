#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

const double eps = 1e-11;

int main() {
  int nt;
  cin >> nt;
  for (int tt = 1; tt <= nt; tt++) {
    printf("Case #%d:\n", tt);
    double w;
    int l, u, g;
    cin >> w >> l >> u >> g;
    vector <double> xl(l), yl(l), xu(u), yu(u);
    for (int i = 0; i < l; i++) {
      cin >> xl[i] >> yl[i];
    }
    for (int i = 0; i < u; i++) {
      cin >> xu[i] >> yu[i];
    }
    double sum = 0.0;
    for (int i = 1; i < l; i++) {
      sum -= 0.5 * (xl[i] - xl[i - 1]) * (yl[i] + yl[i - 1]);
    }
    for (int i = 1; i < u; i++) {
      sum += 0.5 * (xu[i] - xu[i - 1]) * (yu[i] + yu[i - 1]);
    }
    double t = sum / g;
    for (int i = 1; i < g; i++) {
      double q = t * i;
      double mi = 0.0, ma = w;
      for (int it = 0; it < 100; it++) {
        double av = (mi + ma) * 0.5;
        double cur = 0.0;
        for (int j = 1; j < l; j++) {
          if (xl[j] < av + eps) {
            cur -= 0.5 * (xl[j] - xl[j - 1]) * (yl[j] + yl[j - 1]);
          } else if (xl[j - 1] < av - eps) {
            double y = (av - xl[j - 1]) * (yl[j] - yl[j - 1]) / (xl[j] - xl[j - 1]) + yl[j - 1];
            cur -= 0.5 * (av - xl[j - 1]) * (y + yl[j - 1]);
          }
        }
        for (int j = 1; j < u; j++) {
          if (xu[j] < av + eps) {
            cur += 0.5 * (xu[j] - xu[j - 1]) * (yu[j] + yu[j - 1]);
          } else if (xu[j - 1] < av - eps) {
            double y = (av - xu[j - 1]) * (yu[j] - yu[j - 1]) / (xu[j] - xu[j - 1]) + yu[j - 1];
            cur += 0.5 * (av - xu[j - 1]) * (y + yu[j - 1]);
          }
        }
        if (cur < q) {
          mi = av;
        } else {
          ma = av;
        }
      }
      printf("%.9lf\n", mi);
    }
  }
  return 0;
}
