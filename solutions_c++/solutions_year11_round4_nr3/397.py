#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;

int main() {
    ll casos;
    cin >> casos;
    for (ll cas = 1; cas <= casos; ++cas) {
        ll n;
        cin >> n;
        if (n == 1) {
            cout << "Case #" << cas << ": " << 0 << endl;
            continue;
        }
        vector<bool> esp(sqrt(n) + 1, true);
        esp[0] = esp[1] = false;
        for (ll i = 2; i*i <= esp.size(); ++i) {
            if (not esp[i]) continue;
            for (ll j = i + i; j < esp.size(); j += i) esp[j] = false;
        }
        vector<ll> primo;
        for (ll i = 0; i < esp.size(); ++i) if (esp[i]) primo.push_back(i);
        ll cnt = 0;
        for (ll i = 0; i < primo.size(); ++i) {
            ll a = primo[i];
            while (a*primo[i] <= n) {a *= primo[i]; ++cnt;}
        }
        cout << "Case #" << cas << ": " << cnt + 1 << endl;
    }
}