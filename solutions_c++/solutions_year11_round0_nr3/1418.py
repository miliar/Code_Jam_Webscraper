
#include <iostream>
#include <vector>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

using namespace std;

int main() {
  int c, n, t;
  cin >> t;
  for (int z = 1; z <= t; ++z) {
    cin >> n;
    int m = 1000001, s = 0;
    vector<int> v(30, 0);
    for (int i = 0; i < n; ++i) {
      cin >> c;
      m = MIN(m, c);
      s += c;
      for (int j = 0; j < 30; ++j)
	if ((c >> j) & 1) v[j]++;
    }

    bool b = true;
    for (int i = 0; b && i < 30; ++i)
      b = v[i]%2 == 0;
    cout << "Case #" << z << ": ";
    if (!b) cout << "NO\n";
    else cout << s - m << "\n";
  }
}
