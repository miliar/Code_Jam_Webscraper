#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned int uint;

const uint max_xor = 1000001;

int n;
uint num[1000];
uint xsum[1000];

void solve() {
  cin >> n;
  uint sum = 0;
  for (int i = 0; i < n; ++i) {
    cin >> num[i];
    sum += num[i];
  }
  
  sort(num, num + n);

  xsum[n - 1] = num[n - 1];
  for (int i = n - 2; i >= 0; --i)
    xsum[i] = xsum[i + 1] ^ num[i];

  uint x = 0;
  uint s = 0;
  for (int i = 0; i < n - 1; ++i) {
    s += num[i];
    x ^= num[i];

    if (x == xsum[i + 1]) {
      cout << sum - s << endl;
      return;
    }
  }
  
  cout << "NO\n";
}

int main() {
  int tests;
  cin >> tests;

  for (int t = 1; t <= tests; ++t) {
    cout << "Case #" << t << ": ";
    solve();
  }
  
  return 0;
}
