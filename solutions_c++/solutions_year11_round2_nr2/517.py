#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <iomanip>


using namespace std;
//#define DBG
int n;
vector <double> a;
double d;
double p;
int v;
int t;

bool can(double time) {
  double x = double (a[0] - time);
  for (int j = 1; j < a.size(); ++j) {
    x += d;
    if (!(abs(x - a[j]) < time + 0.00000000001)) {
      if (a[j] * 1.0 < x) {
        return false;
      } else {
        x = double (a[j] - time);
      }
    }
  }
  return true;
}

int main() {
#ifdef DBG
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
#endif
  cin >> t;
  for (int q = 0; q < t; ++q) {
    cin >> n >> d;
    a.clear();
    for (int i = 0; i < n; ++i) {
      cin >> p >> v;
      for (int j = 0; j < v; ++j) {
        a.push_back(p);
      }
    }
    sort(a.begin(), a.end());
    double l = 0;
    double r = 10000000000;

    while (r - l > 0.0000001) {
      double m = (l + r) / 2;
      if (can(m)) {
        r = m;
      } else {
        l = m;
      }
    }
    cout << "Case #" << q + 1 <<": ";
    cout << fixed << setprecision(6) << r << endl;
  }
  return 0;
}