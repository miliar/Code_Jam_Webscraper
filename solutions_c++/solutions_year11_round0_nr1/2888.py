#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int N;
    cin >> N;
    vector<pair<int, int> > Os, Bs;
    for (int j = 0; j < N; ++j) {
      string s;
      int p;
      cin >> s >> p;
      if (s == "O") {
        Os.push_back(make_pair(j, p));
      } else {
        Bs.push_back(make_pair(j, p));
      }
    }
    int k = 0, op = 1, bp = 1, time = 0;
    size_t oi = 0, bi = 0;
    while (k < N) {
      bool pushed = false;
      if (oi < Os.size() && op != Os[oi].second) {
        op += (op < Os[oi].second) ? 1 : -1;
      } else if (oi < Os.size() && k == Os[oi].first) {
        ++k;
        ++oi;
        pushed = true;
      }
      if (bi < Bs.size() && bp != Bs[bi].second) {
        bp += (bp < Bs[bi].second) ? 1 : -1;
      } else if (!pushed && bi < Bs.size() && k == Bs[bi].first) {
        ++k;
        ++bi;
      }
      ++time;
    }
    cout << "Case #" << (i + 1) << ": " << time << endl;
  }
  return 0;
}
