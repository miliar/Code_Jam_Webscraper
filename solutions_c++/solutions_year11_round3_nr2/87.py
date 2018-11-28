#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define ll long long

ll c[1000];
ll d[1000001];
int main() {
    ll T;
    cin>>T;
    for (ll t=1;t<=T;t++) {
        ll L,s,N,C;
        cin>>L>>s>>N>>C;
        for (ll i=0;i<C;i++) {
            cin>>c[i];
        }
        d[0] = 0;
        for (int i=0;i<N;i++) {
            d[i+1] = d[i] + c[i % C];
        }
        ll p = 0;
        ll pos = 0;
        ll ct = 0;
        vector<ll> dists;
        while (p < N) {
            ll dt = (d[p+1] - pos) * 2;
            if (dt > s) {
                pos += s/2;
                ct += s;
                dists.push_back(d[p+1] - pos);
                for (int i=p+2;i<=N;i++) {
                    dists.push_back(d[i] - d[i-1]);
                }
                sort(dists.rbegin(), dists.rend());
                for (int i=0;i<dists.size();i++) {
                    if (i < L) {
                        ct += dists[i];
                    } else {
                        ct += dists[i] * 2;
                    }
                    //cout << "Dists is " << dists[i] << " to " << ct << endl;
                }
                break;
            }
            s -= dt;
            pos = d[p+1];
            ct += dt;
            //cout << "Spend " << dt << " to get to " << p << endl;
            p++;
        }

        cout << "Case #" << t << ": " << ct << endl;
    }
}
