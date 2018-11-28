#include <cstdio>
#include <algorithm>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

#define m 1010

int a[m], n, k, p, l;

int main()
{
  freopen("keys.in", "r", stdin);
  freopen("keys.out", "w", stdout);
  scanf("%d", &n);
  forn (tt, n)
  {
    printf("Case #%d: ", tt + 1);
    scanf("%d%d%d", &p, &k, &l);
    forn (i, l)
      scanf("%d", &a[i]);
    if (p * k < l)
      printf("Impossible\n");
    else
    {
      long long ans = 0;
      sort(a, a + l);
      reverse(a, a + l);
      forn (i, l)
        ans += a[i] * (i / k + 1);
      printf("%lld\n", ans);
    }
  }
  return 0;
}
