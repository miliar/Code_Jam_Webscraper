#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>

#define mp make_pair
#define eps 1e-8

using namespace std;

typedef long long ll;
typedef long double ld;

ll d, c;
vector<ll> p, v;

ll calcT(ll a) {
    ll res = a-1;
    res *= d/2;
    return res;
}

bool check(ll a) {
    ll s = p[0] - a;
    ll e = s + (v[0]-1)*d;
    ll i;
    for(i=1; i<c; ++i) {
        s = p[i] - a;
        s = max(s, e+d);
        e = s + (v[i]-1)*d;
        if (e - p[i] > a) return false;
    }
    return true;
}

void printRes(ll t, ll r) {
    cout<<"Case #"<<t<<": "<<r/2<<(r%2 ? ".5" : ".0")<<endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ll T, t, n, i, j;
    cin>>T;
    for(t=1; t<=T; ++t) {
        cin>>c>>d;
        p.clear();
        p.resize(c);
        v.clear();
        v.resize(c);
        d *= 2;
        for(i=0; i<c; ++i) {
            cin>>p[i]>>v[i];
            p[i] *= 2;
        }
        ll s=0, e=1LL<<42, m;
        s = 0;
        for(i=0; i<c; ++i) {
            s = max(s, calcT(v[i]));
        }
        if (check(s)) {
            printRes(t, s);
            continue;
        }
        while(e-s > 1) {
            m = (s+e) / 2;
            if (check(m)) e = m;
            else s = m;
        }
        printRes(t, e);
    }
    return 0;
}
