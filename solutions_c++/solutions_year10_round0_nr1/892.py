#include <iostream>

using namespace std;

typedef long long ll;

int main() {
  int t;
  cin >> t;
  for (int ca = 1; t--; ++ca) {
    ll n, k;
    cin >> n >> k;
    cout << "Case #" << ca << ": ";
    if ((k+1)%(1<<n) == 0) cout << "ON" << endl;
    else cout << "OFF" << endl;
  }
}
