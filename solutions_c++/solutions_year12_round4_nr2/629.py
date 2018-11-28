// B.cc
// Wentao Han (wentao.han@gmail.com)

#include <algorithm>
#include <iostream>
#include <vector>
#include <stdlib.h>
using namespace std;

bool overlaps(int i, const vector<int>& r, const vector<int>& x, const vector<int>& y) {
  for (int j = 0; j < i; j++) {
    long dx = x[i] - x[j];
    long dy = y[i] - y[j];
    long r2 = r[i] + r[j];
    if (dx * dx + dy * dy <= r2 * r2) {
      return true;
    }
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, W, L;
    cin >> N >> W >> L;
    vector<int> r(N);
    for (int i = 0; i < N; i++) {
      cin >> r[i];
    }
    vector<int> x(N), y(N);
    for (int i = 0; i < N; i++) {
      do {
        x[i] = rand() % (W + 1);
        y[i] = rand() % (L + 1);
      } while (overlaps(i, r, x, y));
    }
    cout << "Case #" << t << ":";
    for (int i = 0; i < N; i++) {
      cout << " " << x[i] << " " << y[i];
    }
    cout << endl;
  }
}
