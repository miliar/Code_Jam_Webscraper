#include <iostream>

using namespace std;

int _pow[20];

bool check(int n, int m) {
  int p = n, cnt = 0;
  while (p > 9) {
    ++cnt;
    p /= 10;
  }
  for (int i = 1; i <= cnt; ++i) {
    int t = n / _pow[i] + (n % _pow[i]) * _pow[cnt + 1 - i];
    if (t == m) return true;
  }
  return false;
}

void solve() {
  int A, B, ans = 0;
  cin >> A >> B;
  for (int n = A; n <= B; ++n)
    for (int m = n + 1; m <= B; ++m)
      if (check(n, m)) ++ans;
  cout << ans << endl;
}

void init() {
  _pow[0] = 1;
  for (int i = 1; i < 20; ++i)
    _pow[i] = _pow[i - 1] * 10;
}

int main() {
  init();
  int ncs;
  cin >> ncs;
  for (int i = 1; i <= ncs; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
