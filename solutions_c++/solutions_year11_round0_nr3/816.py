#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> Vi;

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int n;
    cin >> n;
    Vi v(n);
    for (int i = 0; i < n; ++i) cin >> v[i];
    
    int x = 0;
    for (int i = 0; i < n; ++i) x ^= v[i];
    
    cout << "Case #" << cas << ": ";
    if (x == 0) {
      int s = 0, m = v[0];
      for (int i = 0; i < n; ++i) {
        s += v[i];
        m = min(m, v[i]);
      }
      cout << s - m << endl;
    }
    else cout << "NO" << endl;
  }
}
