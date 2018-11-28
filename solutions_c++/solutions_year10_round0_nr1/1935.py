#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t;
  cin >> t;
  for (int tests = 0; tests < t; ++tests) {
    bool result = true;
    int n, k;
    cin >> n >> k;
    int pow = 1;
    for (int i = 0; i < n; ++i) {
      result &= (k / pow) % 2 != 0;
      pow <<= 1;
    }
    printf("Case #%d: %s\n", tests + 1, result ? "ON" : "OFF");
  }

  return 0;
}