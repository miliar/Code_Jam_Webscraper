#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
  freopen("output.txt", "w", stdout);
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int n; 
    cin >> n;
    int sum = 0;
    int xor = 0;
    int m = 10000000;
    for (int i =0; i < n; ++i) {
      int x;
      cin >> x;
      xor ^= x;
      sum += x;
      m = min(x, m);
    }
    if (xor == 0) {
      cout << "Case #" << t << ": " << (sum - m) << endl;
    } else {
      cout << "Case #" << t << ": NO" << endl;
    }
  }
}