#include<iostream>
using namespace std;

const int maxn = 1000000+3;

int cases;
int f[maxn], g[maxn];
int a1, a2, b1, b2, c;
long long ans;

int main()
{
    freopen("C0.in","r",stdin);
    freopen("C.out","w",stdout);
    for (int i = 1; i < maxn; ++i)
      f[i] = int(i/1.61803398874);
    for (int i = 1; i < maxn; ++i) {
      g[i] = g[i-1];
      while ((g[i] < maxn)&&(f[g[i]] < i)) ++g[i];
    }
    cin >> cases;
    for (int k = 1; k <= cases; ++k) {
      cout << "Case #" << k << ": ";
      cin >> a1 >> a2 >> b1 >> b2;
      ans = 0;
      for (int i = b1; i <= b2; ++i) {
        c = f[i];
        if (a1 <= c) ans += c-a1+1;
        if (a2 <= c) ans -= c-a2;
        c = g[i];
        if (a2 >= c) ans += a2-c+1;
        if (a1 >= c) ans -= a1-c;
      }
      cout << ans;
      cout << endl;
    }
    
    return 0;
}
