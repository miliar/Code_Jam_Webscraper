#include <iostream>

using namespace std;

int main() {
  int tt, n, k;

  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cin >> n >> k;
    int x = 1 << n;
    if (k % x == (x - 1)) {
      cout << "Case #" << t << ": ON\n";
    } else {
      cout << "Case #" << t << ": OFF\n";
    }
  }
  return 0;
}
