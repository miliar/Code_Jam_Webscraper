using namespace std;
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <iostream>
#include <memory.h>
#include <algorithm>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FORab(i,a,n) for(__typeof(n) i=(a);i<=(n);i++)
#define FOR1(i,n) FORab(i,1,n)
#define pb push_back
#define ms(n,p) memset(n, (p), sizeof(n))
#define ms0(n) ms(n, 0)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

bool ans(ll n, ll d, ll g) {
    if(d == 0) {
        if(g == 100) return false;
        else return true;
    }
    if(g == 0) return false;
    if(d == 100) return true;
    if(g == 100) return false;
    ll cd = 100/__gcd(100, (int)d);
    ll cg = 100/__gcd(100, (int)g);
    //cout<<n<<' '<<d<<' '<<g<<endl;
    //cout<<cd<<' '<<cg<<endl;
    if(n < cd) return false;
    return true;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    ll t;cin>>t;
    FOR1(cno,t) {
        ll n, d, g;
        cin>>n>>d>>g;
        bool p = ans(n, d, g);
        cout<<"Case #"<<cno<<": ";
        if(p) cout<<"Possible"<<endl;
        else cout<<"Broken"<<endl;
    }
    return 0;
}
