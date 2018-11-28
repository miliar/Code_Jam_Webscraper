#include <cstdio> 

using namespace std;

typedef long long ll;

int T;

int r, n, k;

int a[2010];           
 
ll s[2010];
int s1[2010];

int main()
{
  //freopen("a.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    scanf("%d %d %d", &r, &k, &n);
    for (int i = 0; i < n; ++i)
      scanf("%d", &a[i]);
    for (int i = 0; i < n; ++i)
    {
      ll p = a[i];
      int j = (i + 1)%n;
      s1[i] = 1;
      
      while(s1[i] < n && p + a[j] <= k )
      {
        ++s1[i];
        p += a[j];
        j = (j + 1)%n;   
      }
      s[i] = p;
      
     
    }
    ll res = 0;
    int p = 0;
    for (int i = 0; i < r; ++i)
    {
      res += s[p];
      p = (p + s1[p]) % n;
    }
    printf("Case #%d: %I64d\n", t + 1, res);
  }
  return 0;
}                          