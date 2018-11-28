#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for(int c = 1; c <= t; c++) {
    int r, k, n;
    int q[1000];
    int f = 0;
    cin >> r >> k >> n;
    for(int g = 0; g < n; g++) {
      cin >> q[g];
    }
    int p = 0;
    for(int i = 0; i < r; i++) {
      int s = 0, j = 0;
      while(s + q[f] <= k && j < n) {
        s += q[f];
        f = (f + 1) % n;
        j++;
      }
      p += s;
    }
    cout << "Case #" << c << ": " << p << endl;
  }
}
