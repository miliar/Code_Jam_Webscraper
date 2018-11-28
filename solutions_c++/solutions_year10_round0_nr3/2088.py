#include <iostream>
#include <vector>

using namespace std;

int main () {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int R, k, N;
    cin >> R >> k >> N;
    vector<int> g;
    g.reserve(N);
    for (int j = 0; j < N; ++j) {
      int gi;
      cin >> gi;
      g.push_back(gi);
    }

    unsigned int profit = 0;
    int idx = 0;
    for (int j = 0; j < R; ++j) {
      int curk = k;
      int first = idx;
      for (;;) {
        if (curk >= g[idx]) {
          profit += g[idx];
          curk -= g[idx];
          idx = (idx + 1) % N;
        } else {
          break;
        }
        if (idx == first) {
          break;
        }
      }
    }
    cout << "Case #" << i + 1 << ": " << profit << endl;
  }
  return 0;
}
