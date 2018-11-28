#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    ll r, k, n;
    cin >> r >> k >> n;
    vector<ll> g(n);
    ll sum = 0;
    for (int i = 0; i < n; ++i) {
      cin >> g[i];
      sum += g[i];
    }
    cout << "Case #" << ca << ": ";
    if (sum <= k) {
      cout << sum*r << endl;
    }
    else {
      vector<ll> time(n, -1), money(n, 0);
      ll ind = 0, t = 0;
      for (; t < r && time[ind] == -1; ++t) {
        time[ind] = t;
        if (t > 0) money[t] = money[t-1];
        ll cur = 0;
        for (; cur+g[ind] <= k; ind = (ind+1)%n) {
          cur += g[ind];
        }
        money[t] += cur;
      }
      if (t == r) {
        cout << money[t-1] << endl;
      }
      else {
        ll precycl = 0;
        if (time[ind] > 0) precycl = money[time[ind]-1];
        ll ans = precycl;
        r -= time[ind];
        ans += (money[t-1]-precycl)*(r/(t-time[ind]));
        r %= t-time[ind];
        time = vector<ll>(n, -1);
        money = vector<ll>(n, 0);
        t = 0;
        if (t < r) {
          for (; t < r; ++t) {
            time[ind] = t;
            if (t > 0) money[t] = money[t-1];
            ll cur = 0;
            for (; cur+g[ind] <= k; ind = (ind+1)%n) {
              cur += g[ind];
            }
            money[t] += cur;
          }
          ans += money[t-1];
        }
        cout << ans << endl;
      }
    }
  }
}
