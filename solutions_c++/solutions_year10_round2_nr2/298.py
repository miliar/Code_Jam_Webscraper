#include <iostream>
#include <map>

using namespace std;

const int maxn = 100;

int x[maxn];
int v[maxn];

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    int n, k, b, t;
    cin >> n >> k >> b >> t;
    for(int i=0;i<n;i++) cin >> x[i];
    for(int i=0;i<n;i++) cin >> v[i];
    int res = 0;

    for(int i=n-1;(i>=0)&&k;--i)
      if(x[i]+v[i]*t>=b)
	--k;
      else
	res += k;

    cout << "Case #" << tcase << ": ";
    if(k) cout << "IMPOSSIBLE\n";
    else cout << res << '\n';
  }
}
