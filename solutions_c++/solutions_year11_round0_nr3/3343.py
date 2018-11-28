#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    unsigned int par = 0;
    unsigned int sum = 0;
    unsigned int mini = 1000000000;
    int n;
    cin >> n;
    for (int j = 0; j < n; ++j) {
      unsigned int a;
      cin >> a;
      par ^= a;
      sum += a;
      if (a < mini) mini = a;
    }
    if (0 == par) {
      cout << "Case #" << i << ": " << sum - mini << '\n';
    } else {
      cout << "Case #" << i << ": NO" << '\n';
    }
  }

  return 0;
}
