#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int C, D;
vector<pair<int, int> > pv;

bool valid(double tm) {
  double last = -1e100;
  for (int i = 0; i < pv.size(); i++)
    for (int j = 0; j < pv[i].second; j++) {
      double next = last + D;
      if (pv[i].first + tm < next) return false;
      last = max(next, pv[i].first - tm);
    }
  return true;
}

double error(double low, double hi) {
  return min(hi - low, (hi - low) / hi);
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> C >> D;
    pv.clear();
    for (int i = 0; i < C; i++) {
      int p, v; cin >> p >> v;
      pv.push_back(make_pair(p, v));
    }
    sort(pv.begin(), pv.end());

    double low = 0, hi = 1e20;
    while (error(low, hi) > 1e-12) {
      // cout << low << " " << hi << endl;
      double mid = (low + hi) / 2;
      if (valid(mid)) hi = mid;
      else low = mid;
    }
    cout.setf(ios::fixed); cout << setprecision(7);
    cout << "Case #" << c << ": " << hi << endl;
  }
  return 0;
}
