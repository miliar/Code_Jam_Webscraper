#include <iostream>

using namespace std;

const int N = 1000;

int c[N];

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int n; cin >> n;
    int sum = 0;
    int z = 0;
    int lo = 1000000000;
    for (int i = 0; i < n; i++) {
      cin >> c[i];
      sum += c[i];
      z ^= c[i];
      lo = min(lo, c[i]);
    }

    int gain = -1;
    if (z == 0) gain = sum - lo;

    cout << "Case #" << tt << ": ";
    if (gain >= 0)
      cout << gain << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}

