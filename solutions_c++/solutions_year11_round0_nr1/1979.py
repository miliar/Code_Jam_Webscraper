#include <stdio.h>
#include <algorithm>
using namespace std;

struct Target {
  int rob, tar;
} a[1000];

int pos[2], cnt[2];

int tc, n;
char s[100];

int main ()
{
  scanf ("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
      scanf("%s%d", s, &a[i].tar);
      a[i].rob = s[0] == 'O' ? 0 : 1;
    }
    pos[0] = pos[1] = 1;
    cnt[0] = cnt[1] = 0;
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
      int rob = a[i].rob;
      int need = abs(a[i].tar - pos[rob]) - cnt[rob];
      if (need < 0) need = 0;
      need++;
      ans += need;
      cnt[rob] = 0;
      pos[rob] = a[i].tar;
      cnt[1 - rob] += need;
    }
    printf ("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
