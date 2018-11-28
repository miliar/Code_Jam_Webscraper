#include<iostream>
using namespace std;

const int maxn = 2000+3;

long long ans, z;
int cases;
int n, k, r, l;
int a[maxn];
long long b[maxn];
int c[maxn];

int main()
{
    freopen("C1.in","r",stdin);
    freopen("C.out","w",stdout);
    cin >> cases;
    for (int i = 1; i <= cases; ++i) {
      cout << "Case #" << i << ": ";

      cin >> r >> k >> n;
      for (int i = 1; i <= n; ++i) cin >> a[i];
      l = 1; a[0] = 0;
      memset(c,0,sizeof(c));
      while ((!c[l])&&(a[0] < r)) {
        ++a[0]; z = l; c[l] = a[0];
        b[a[0]] = 0;
        while (1) {
          b[a[0]] += a[l];
          if (b[a[0]] > k) {
            b[a[0]] -= a[l];
            break;
          }
          ++l; if (l > n) l = 1;
          if (l == z) break;
        }
        b[a[0]] += b[a[0]-1];
      }
      ans = b[a[0]];
      if (c[l]) {
        r -= a[0];
        z = r/(a[0]-c[l]+1);
        r %= (a[0]-c[l]+1);
        
        ans += b[c[l]+r-1]-b[c[l]-1];
        ans += z*(b[a[0]]-b[c[l]-1]);
      }
      
      cout << ans << endl;
    }
    return 0;
}
