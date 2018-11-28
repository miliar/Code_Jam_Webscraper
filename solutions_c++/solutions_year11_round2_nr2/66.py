#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;

ll D;
vector<ll> P;

ll skus(ll dist) {
  ll last = P[0] - dist;
  for(ll i = 1; i < P.size(); i++) {
    ll pos = max(last + D, P[i] - dist);
    if(llabs(P[i] - pos) > dist) return false;
    last = pos;
  }
//printf("skus(%lld) is true\n", dist);
  return true;
}

int main() {
  ll T;
  scanf("%lld", &T);
  for(ll t = 1; t <= T; t++) {
    ll C;
    scanf("%lld%lld", &C, &D);
    D *= 2;
    P.clear();
    for(ll i = 0; i < C; i++) {
      ll p, v;
      scanf("%lld%lld", &p, &v);
      p *= 2;
      while(v--) P.push_back(p);
    }
    sort(P.begin(), P.end());
//for(ll i = 0; i < P.size(); i++) printf("%lld ", P[i]); printf("\n");
    ll low = 0, high = 1000000LL*1000000LL*100LL;
    // <low doesn't work, >=high does work
    while(low != high) {
      ll mid = (low+high)/2;
      if(skus(mid))
        high = mid;
      else
        low = mid+1;
    }
    printf("Case #%lld: %lld.%c\n", t, low/2, low%2 ? '5' : '0');
  }
  return 0;
}

