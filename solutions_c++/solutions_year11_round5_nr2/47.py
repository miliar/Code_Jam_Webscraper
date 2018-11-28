#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;
int a[1005];
int d[1005], cnt;

int main(void)
{
//  freopen("B-small-attempt0.in", "r", stdin);
//  freopen("B-small-attempt0.out", "w", stdout);
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

  scanf("%d", &nt);
  for (tn=0; tn<nt; tn++)
  {
    fprintf(stderr, "Case #%d: \n", tn+1);

    printf("Case #%d: ", tn+1);

    scanf("%d", &n);
    for (int i=0; i<n; i++)
      scanf("%d", &a[i]);

    if (n == 0) {
      puts("0");
      continue;
    }

    int ans = 1000000;
    cnt = 0;
    sort (a, a+n);
    for (int i=0; i<n; ) {
      int j;
      for (j=i; j<n && a[j] == a[i]; j++) ;
      int b = j - i;

      if (a[i] - 1 != a[i-1]) {
        for (int t = 0; t < cnt; t++)
          ans = min(ans, d[t]);
        cnt = 0;
      }

      for (int t=0; t < min (b, cnt); t++)
        d[cnt - 1 - t]++;
      if (b < cnt) {
        for (int t = b; t < cnt; t++)
          ans = min(ans, d[cnt - 1 - t]);
        for (int t = b-1; t >= 0; t--)
          d[b - 1 - t] = d[cnt - 1 - t];
      } else {
        for (int i=cnt; i<b; i++)
          d[i] = 1;
      }

      cnt = b;
      sort (d, d+cnt);
      reverse (d, d+cnt);
      i = j;
//      for (int t=0; t<cnt; t++)
//        fprintf (stderr, "%d%c", d[t], " \n"[t+1==cnt]);
    }
    for (int t = 0; t < cnt; t++)
      ans = min(ans, d[t]);

    printf ("%d\n", ans);
  }
  return 0;
}
