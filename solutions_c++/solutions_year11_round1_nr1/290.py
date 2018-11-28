#include <iostream>

#define debug(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b) {
  if (b == 0) return a;
  return gcd(b, a%b);
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    ll n, pd, pg;
    cin >> n >> pd >> pg;
    cout << "Case #" << ca << ": ";
    if (100/gcd(100, pd) <= n && (pg < 100 || pd == 100) && (pg > 0 || pd == 0)) cout << "Possible" << endl;
    else cout << "Broken" << endl;
  }
}
