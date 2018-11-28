#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for(int c = 1; c <= t; c++) {
    int n, k;
    cin >> n >> k;
    cout << "Case #" << c << ": ";
    if(k % (1 << n) == (1 << n) - 1) cout << "ON" << endl;
    else cout << "OFF" << endl;
  }
}
