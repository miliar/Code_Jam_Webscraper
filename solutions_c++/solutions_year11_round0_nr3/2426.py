#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int a, x, s, t, n, mn;

int main()
{
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    scanf("%d", &n);
    x = s = 0;
    for (int j = 0; j < n; j++)
    {
      scanf("%d", &a);
      if (!j || a < mn) mn = a;
      x ^= a;
      s += a;
    }
    printf("Case #%d: ", i+1);
    if (x) printf("NO\n");
    else printf("%d\n", s-mn);
  }
  return 0;
}
