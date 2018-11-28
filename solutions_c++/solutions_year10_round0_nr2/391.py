#include<iostream>
using namespace std;

const int maxn = 1000+3;

long long cases, n, ans, z;
long long a[maxn];

long long gcd(long long x, long long y)
{
    if (x < y) {
      z = x;
      x = y;
      y = z;
    }
    if (y == 0) return x;
    else return gcd(y,x%y);
}
int main()
{
    freopen("B0.in","r",stdin);
    freopen("B.out","w",stdout);
    
    cin >> cases;
    for (int i = 1; i <= cases; ++i) {
      cout << "Case #" << i << ": ";

      cin >> n;
      for (int j = 1; j <= n; ++j) cin >> a[j];
      sort(&a[1],&a[1]+n);
      ans = a[2]-a[1];
      for (int j = 2; j < n; ++j) 
        ans = gcd(ans,a[j+1]-a[j]);
      a[1] = a[1]%ans;
      if (a[1] == 0) a[1] = ans;
      ans -= a[1];
      cout << ans << endl;
    }
    return 0;
}
