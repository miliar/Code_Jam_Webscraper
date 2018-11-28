#include <iostream>
#include <algorithm>

using namespace std;

int solve(int l, int p, int c) {
  if ((long long)l * (long long)c >= (long long)p) {
    return 0;
  }

  int a = l, b = p;
  while (a < b) {
    a *= c;
    b /= c;
  }

  int x = (a + b + 1) / 2;
  return 1 + max(solve(l, x, c), solve(x, p, c));
}

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int l, p, c;
    cin >> l >> p >> c;
    int ans = solve(l, p, c);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
