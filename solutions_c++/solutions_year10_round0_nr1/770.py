// Problem A: Snapper Chain (Qualification Round, Google Code Jam 2010)
// Author: Su Shi (Carmack.Shi@gmail.com)
// Usage: [execute] < inputfile > outputfile

#include <string>
#include <iostream>
#include <cassert>
using namespace std;

char* LightState[2] = { "OFF", "ON" };

bool IsLightOn(int n, int k) {
  assert(1 <= n && n <= 30 &&
         0 <= k && k <= 100000000);

  // Common Case
  int cycle_count = (1 << n);
  int final_toggle_number = k % cycle_count;
  return final_toggle_number == (cycle_count - 1);
}

int main() {
  int t, n, k;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n >> k;
    cout << "Case #" << i << ": "
         << LightState[static_cast<int>(IsLightOn(n, k))] << endl;
  }

  return 0;
}
