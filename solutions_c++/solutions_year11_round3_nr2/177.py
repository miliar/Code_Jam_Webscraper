using namespace std;
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <memory.h>
#include <iostream>
#include <algorithm>
#include <assert.h>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FORND(i,n) for(i=0;i<(n);i++)
#define FORab(i,a,n) for(__typeof(n) i=(a);i<=(n);i++)
#define FOR1(i,n) FORab(i,1,n)
#define pb push_back
#define ms(n,p) memset(n, (p), sizeof(n))
#define ms0(n) ms(n, 0)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll,ll> pii;

ll a[1100];

bool cmp(ll a, ll b) {
    return a > b;
}

int main() {
    freopen("/home/enzam/Downloads/B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ll tc;cin>>tc;
    FOR1(cno, tc) {
        ll L, t, N, C;
        cin>>L>>t>>N>>C;
        FOR(i, C) cin>>a[i];

        vi distances;
        ll na=0;
        ll cc=0;
        ll ans=0;
        bool crossed = false;
        ll i;
        FORND(i, N) {
            if(!crossed) {
                if(ans+a[na]*2 <= t) {
                    ans += a[na]*2;
                    //clog<<"Norm "<<a[na]*2<<endl;
                } else {
                    ll left = ans+a[na]*2 - t;
                    assert(!(left&1));
                    distances.pb(left/2);
                    ans += (a[na]*2 - left);
                    //clog<<"Half "<<a[na]*2 - left<<endl;
                    crossed = true;
                }
            } else {
                distances.pb(a[na]);
            }
            na = (na+1)%C;
        }
        sort(all(distances), cmp);
        for(i=0;i<L && i<distances.size(); i++) {
            ans += distances[i];
            //clog<<"L "<<distances[i]<<endl;
        }
        for(;i<distances.size();i++) {
            ans += distances[i]*2;
            //clog<<"NONL "<<distances[i]*2<<endl;
        }
        cout<<"Case #"<<cno<<": "<<ans<<endl;
    }
    return 0;
}

