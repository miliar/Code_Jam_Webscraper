#include <iostream>
using namespace std;

int main() {
  int t, n, k, z;
  bool on;
  cin >> t;
  for(int i=1; i<=t; i++) {
    cin >> n >> k;
    z = (1 << n) - 1;
    on = (z & k) == z;
    cout << "Case #" << i << ": " << (on ? "ON" : "OFF") << endl;
  }
  return 0;
}
