#include <iostream>
using namespace std;

typedef long long ll;

int main() {
  int t;
  cin >> t;
  for (int casenum = 1; casenum <= t; ++casenum) {
    ll l, p, c;
    cin >> l;
    cin >> p;
    cin >> c;
    
    ll ccount = 0;
    ll b = l * c;

    while (b < p) {
      b = b * c;
      ccount += 1;
    }

    // 1 -> 1
    // 2 -> 2
    // 3 -> 2
    // 4 -> 3
    // 7 -> 3

    ll x = 1;
    ll xcount = 0;
    while (x <= ccount) {
      x = x * 2;
      xcount ++;
    }
    
    cout << "Case #" << casenum << ": ";
    cout << xcount;
    cout << endl;
  }
}
