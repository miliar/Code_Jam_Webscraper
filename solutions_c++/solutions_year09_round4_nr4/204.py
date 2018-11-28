#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
using namespace std;

bool can_cover(vector<int>& x, vector<int>& y, vector<int>& r, double rd) {
  int N = x.size();
  if (N == 1) return rd >= r[0];
  if (N == 2) return rd >= max(r[0], r[1]);

  if (rd < max(r[0], max(r[1], r[2]))) return false;
  for (int i = 0; i <= 1; i++)
    for (int j = i+1; j <= 2; j++) {
      int k;
      if (i == 0 && j == 1) k = 2;
      else if (i == 0) k = 1;
      else k = 0;

      double dij = sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])) + r[i] + r[j];
      if (rd >= max(dij / 2, 1.0*r[k])) return true;
    }
  return false;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int N; cin >> N;
    vector<int> x(N), y(N), r(N);
    for (int i = 0; i < N; i++)
      cin >> x[i] >> y[i] >> r[i];

    double low = 0, hi = 2000;
    while (hi - low > 1e-8) {
      double mid = (low + hi) / 2;
      if (can_cover(x, y, r, mid)) hi = mid;
      else low = mid;
    }

    cout.setf(ios::fixed);
    cout << setprecision(6) << "Case #" << c << ": " << low << endl;
  }
  return 0;
}
