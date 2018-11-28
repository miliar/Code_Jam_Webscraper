#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int Q, n, k, p, ans, a[1000];
int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
 
  scanf("%d", &Q);
  for(int q = 1; q <= Q; q++)
  {
    scanf("%d%d%d", &n, &k, &p);
    for(int i = 1; i <= n; i++) scanf("%d", &a[i]);
    sort(a+1, a+1+n);
    ans = 0;
    for(int i = n; i >= 1; i--)
    {
      if(a[i] >= p*3-2) ans++;
      else
        if(k and a[i] >= p*3-4 and a[i]>1)
        {
          k--;
          ans++;
        }
    }
    printf("Case #%d: %d\n", q, ans);
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
