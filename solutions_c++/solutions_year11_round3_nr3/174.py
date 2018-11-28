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

int nums[110];
int n, l, h;

int getAns() {
    FORab(i, l, h) {
        int j;
        FORND(j, n) {
            if((nums[j]%i) && (i%nums[j])) break;
        }
        if(j >= n) return i;
    }
    return 0;
}
int main() {
    //freopen("input.in", "r", stdin);
    freopen("/home/enzam/Downloads/C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    ll tc;cin>>tc;
    FOR1(cno, tc) {
        cin>>n>>l>>h;
        FOR(i, n) cin>>nums[i];
        int ans = getAns();
        cout<<"Case #"<<cno<<": ";
        if(ans) cout<<ans<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}


