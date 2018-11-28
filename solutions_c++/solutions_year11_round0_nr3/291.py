#include <iostream>
using namespace std;

int a[1010];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n, xr = 0; cin >> n;
    for (int i = 0; i < n; i++) {
      cin >> a[i];
      xr = (xr ^ a[i]);
    }
    if (xr != 0) cout << "Case #" << c << ": NO" << endl;
    else {
      sort(a, a+n);
      int res = 0;
      for (int i = 1; i < n; i++)
        res += a[i];
      cout << "Case #" << c << ": " << res << endl;
    }
  }
  return 0;
}
