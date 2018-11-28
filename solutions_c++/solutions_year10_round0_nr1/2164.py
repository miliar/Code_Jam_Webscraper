#include <iostream>
#include <cmath>

using namespace std;
#define pb push_back
#define all(a) (a).begin(),(a).end()
#define sz(a) (int)((a).size())
#define rep(i,n) for(int i=0; i<n; ++i)
#define fori(T,v,i) for(T::iterator i = v.begin(); i != v.end(); i++)
#define forc(T,v,i) for(T::const_iterator i = v.begin(); i != v.end(); i++)
static const double EPS = 1e-8;

typedef long long ll;

ll po(ll a, ll n) {
  ll x = 1;
  rep (i, n) x*=a;  
  return x;
}

int main () {
  int T; cin >> T;
  rep (t, T) {
    ll n, k; cin >> n >> k;
    bool result = true;
    ll x = po(2, n);
    if ((k - x + 1) < 0) result = false;
    if ((k - x + 1) % x) result = false;
    cout << "Case #" << t+1 << ": " << (result?"ON":"OFF") << endl;
  }
  return 0;
}
