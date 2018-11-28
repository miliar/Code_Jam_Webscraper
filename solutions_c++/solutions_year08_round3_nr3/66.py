#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

const ll M = 1000000007;

int n;
ll t[500000];
ull b[500000];
ull a[500000];

ll calc(int cur){
  ll &res = t[cur];
  if(res == -1){
    res = 1;
    for(int j = cur+1; j < n; ++j)
      if(a[cur] < a[j]){
        res += calc(j);
        res %= M;
      }
  }
  return res;
}

int main(void){
  int c;
  cin >> c;
  for(int k = 0; k < c; ++k){
    ll m, X, Y, Z;
    cin >> n >> m >> X >> Y >> Z;

    for(int i = 0; i < m; ++i)
      cin >> b[i];
    for(int i = 0; i < n; ++i){
      a[i] = b[i%m];
      b[i%m] = (X * b[i%m] + Y * (i+1)) % Z;
    }

    fill_n(t, n, -1);
    ll ans = 0;
    for(int i = 0; i < n; ++i){
      ans += calc(i);
      ans %= M;
    }
    cout << "Case #" << k+1 << ": " << ans << endl;
  }

  return 0;
}
