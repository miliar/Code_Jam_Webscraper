#include <iostream>

using namespace std;

bool on_off(int n, int k) {
  unsigned int x = (1 << n) - 1;

  return (k & x) == x;
}

int main() {
  int n, k, t;

  cin >> t;

  for(int i = 1; i <= t; ++i) {
    cin >> n >> k;

    cout << "Case #" << i << ": " << (on_off(n, k) ? "ON" : "OFF") << endl;
  }

  return 0;
}

/*
 * F F F 1
 * N F F 2
 * F N F 3
 * N N F 4
 * F F N 5
 * N F N 6
 * F N N 7
 * N N N 8
 * F F F 9
 *
 * 0 0 0
 * 1 0 0
 * 0 1 0
 * 1 1 0
 * 0 0 1
 * 1 0 1
 * 0 1 1
 * 1 1 1
 */