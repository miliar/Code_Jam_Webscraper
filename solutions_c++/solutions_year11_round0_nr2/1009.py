#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

void solve() {
  char f[26][26], x[26][26];
  memset(f, 0, sizeof(f));
  memset(x, 0, sizeof(x));
  int nf, nx, n;
  string t;
  assert(cin >> nf);
  while (nf--) {
    assert(cin >> t);
    assert(t.length() == 3);
    f[t[0] - 'A'][t[1] - 'A'] = t[2];
    f[t[1] - 'A'][t[0] - 'A'] = t[2];
  }
  assert(cin >> nx);
  while (nx--) {
    assert(cin >> t);
    assert(t.length() == 2);
    x[t[0] - 'A'][t[1] - 'A'] = 1;
    x[t[1] - 'A'][t[0] - 'A'] = 1;
  }
  assert(cin >> n);
  assert(cin >> t);
  assert((int)t.length() == n);
  vector <char> res;
  for (unsigned i = 0; i < t.length(); i++) {
    res.push_back(t[i]);
    while (true) {
      if (res.size() < 2) {
        break;
      }
      char a = res[res.size() - 1], b = res[res.size() - 2];
      if (f[a - 'A'][b - 'A'] != 0) {
        char z = f[a - 'A'][b - 'A'];
        res.pop_back();
        res.pop_back();
        res.push_back(z);
        continue;
      }
      for (unsigned j = 0; j < res.size(); j++) {
        if (x[res[j] - 'A'][a - 'A']) {
          res.resize(0);
          break;
        }
      }
      break;
    }
  }
  cout << "[";
  for (unsigned i = 0; i < res.size(); i++) {
    if (i > 0) {
      cout << ", ";
    }
    cout << res[i];
  }
  cout << "]" << endl;
}

int main() {
  int nt;
  assert(cin >> nt);
  for (int tt = 1; tt <= nt; tt++) {
    cout << "Case #" << tt << ": ";
    solve();
  }
  return 0;
}
