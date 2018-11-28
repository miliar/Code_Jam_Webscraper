#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int maxn = 88;
const int inf = (int)1e9;

int c[maxn][maxn], w[maxn][maxn], a[maxn], d[maxn], p[maxn];
int n, nt, nv, s, t;
char buf[maxn];

int main()
{
  scanf("%d", &nt);
  for (int tt = 1; tt <= nt; tt++)
  {
    scanf("%d", &n);
    nv = n * 2 + 2;
    s = nv - 2, t = nv - 1;
    for (int i = 0; i < n; i++)
    {
      char buf[99];
      scanf("%s", buf);
      int j;
      for (j = n - 1; j >= 0 && buf[j] == '0'; j--)
        ;
      a[i] = j;
    }
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
      int j;
      for (j = i; j < n && a[j] > i; j++)
        ;
      ans += j - i;
      int t = a[j];
      for (int k = j; k > i; k--)
        a[k] = a[k - 1];
      a[i] = t;
    }
    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
