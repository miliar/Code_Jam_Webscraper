#include <iostream>
using namespace std;

int main() {
  int t; cin >> t;
  for(int c = 1; c <= t; c++) {
    int n, k; cin >> n >> k;
    k %= (1<<n);
    cout << "Case #" << c << ": " << (k == (1<<n)-1 ? "ON" : "OFF") << endl;
  }
  return 0;
}
