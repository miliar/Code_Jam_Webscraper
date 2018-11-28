#include <iostream>
using namespace std;
typedef long long ll;

ll gcd(ll a, ll b) {
    if (b==0) return a;
    return gcd(b,a%b);
}

int main() {
    ll t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        ll n,pd,pg;
        cin >> n >> pd >> pg;
        bool ok=1;
        if (pg==100 and pd<100) ok=0;
        if (pg==0 and pd>0) ok=0;
        else {
            ll g = gcd(100,pd);
            if (100/g>n) ok=0;
        }
        cout << "Case #" << cas << ": ";
        if (ok) cout <<"Possible" << endl;
        else cout << "Broken" << endl;
    }
}
