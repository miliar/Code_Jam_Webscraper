#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 1000;

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int x, s, r, tr, n; cin >> x >> s >> r >> tr >> n;
    vector<pair<int, int> > v;
    int tot = 0;
    for (int i = 0; i < n; i++) {
      int b, e, w; cin >> b >> e >> w;
      v.push_back(make_pair(w, e-b));
      tot += e-b;
    }
    int rem = x - tot;
    v.push_back(make_pair(0, rem));
    //sort(v.begin(), v.end(), greater<pair<int, int> >());
    sort(v.begin(), v.end());

    double tRem = tr;
    double res = 0;
    for (int i = 0; i < v.size(); i++) {
      int wr = v[i].first + r;
      int ws = v[i].first + s;
      int len = v[i].second;
      double tIfRunning = len / (double)wr;
      if (tRem >= tIfRunning) {
        res += tIfRunning;
        tRem -= tIfRunning;
      } else {
        res += tRem;
        double lenRemaining = len - tRem * wr;
        tRem = 0;
        res += lenRemaining / ws;
      }
    }

    cout << "Case #" << tt << ": ";
    printf("%.9lf\n", res);
  }
  return 0;
}

