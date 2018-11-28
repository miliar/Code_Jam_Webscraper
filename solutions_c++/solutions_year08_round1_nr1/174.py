#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
ll calc(vi &x, vi &y) {
  sort(x.begin(), x.end());
  sort(y.rbegin(), y.rend());
  int n = x.size();
  ll ret = 0;
  for (int k = 0; k < n; ++k) {
    //cout << ' ' << x[k] << '*' << y[k];
    ret += (ll)x[k]*y[k];
  }
  //cout << endl;
  return ret;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int n;
    cin >> n;
    vi x(n), y(n);
    for (int j = 0; j < n; ++j) { cin >> x[j]; }
    for (int j = 0; j < n; ++j) { cin >> y[j]; }
    ll r = calc(x, y);
    printf("Case #%d: %lld\n", i, r);
  }
}
