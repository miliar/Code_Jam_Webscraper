#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int T, C = 1, n;
  cin >> T;
  while (T-- && cin >> n) {
    int s = 0, xs = 0, mn = 1000000000, a;
    while (n-- && cin >> a)
      s += a, xs ^= a, mn = min(a, mn);

    cout << "Case #" << C++ << ": ";
    if (xs)
      cout << "NO" << endl;
    else
      cout << s-mn << endl;
  }
}
