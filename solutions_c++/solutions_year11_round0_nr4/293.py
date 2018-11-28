#include <iostream>
#include <iomanip>
using namespace std;

int a[1010];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n, res = 0; cin >> n;
    for (int i = 0; i < n; i++) {
      cin >> a[i];
      res += (a[i] != i+1);
    }
    cout.setf(ios::fixed);
    cout << setprecision(6) << "Case #" << c << ": " << (double)res << endl;
  }
  return 0;
}
