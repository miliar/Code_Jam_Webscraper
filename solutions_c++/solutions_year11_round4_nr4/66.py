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

int n, tn, nt, m;
int a[50][50];
long long mask[50];

int ans;

void get(int x, long long y, int d) {
  if (a[x][1] == 1) {
    assert (d == 1);
    int cur = 0;
    while (y) {
      y &= y - 1;
      cur++;
    }
    if (cur > ans)
      ans = cur;
    return;
  }
  assert (d > 1);

  for (int j = 0; j<n; j++) {
    if (((y >> j) & 1) && a[j][1] == d - 1) {
      get (j, y | mask[j], d - 1);
    }
  }
}

int main(void)
{
   freopen("D-small-attempt2.in", "r", stdin);
   freopen("D-small-attempt2.out", "w", stdout);
//   freopen("D-large.in", "r", stdin);
//   freopen("D-large.out", "w", stdout);

   scanf("%d", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      memset(a, 63, sizeof (a));
      memset(mask, 0, sizeof (mask));
      scanf("%d%d", &n, &m);
      for (int i=0; i<n; i++)
        a[i][i]=0;

      for (int i=0; i<m; i++) {
        int x, y;
        scanf("%d,%d", &x, &y);
        a[x][y] = a[y][x] = 1;
        mask[x] |= (1ll << y);
        mask[y] |= (1ll << x);
      }

      for (int k=0; k<n; k++)
        for (int i=0; i<n; i++)
          for (int j=0; j<n; j++) {
            int t = a[i][k] + a[k][j];
            if (t < a[i][j])
              a[i][j] = t;
          }

      ans = -1;
      get (0, mask[0] | 1, a[0][1]);

      printf ("%d %d\n", a[0][1] - 1, ans - a[0][1]);
   }
   return 0;
}
