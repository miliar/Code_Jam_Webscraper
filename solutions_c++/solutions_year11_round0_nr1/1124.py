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
char s[10];

int main(void)
{
//   freopen("A-small-attempt0.in", "r", stdin);
//   freopen("A-small-attempt0.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);

   scanf("%d", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      scanf("%d", &n);
      int cur = 0, p[2]={1, 1}, curt = 0;
      int ans = 0;
      for (int i=0; i<n; i++) {
        int k, c;
        scanf("%s%d", s, &k);
        c = s[0] == 'O';
        if (c == cur) {
          ans += abs (k - p[c]) + 1;
          curt += abs (k - p[c]) + 1;
        } else {
          int d = abs (k - p[c]);
          int tt = min (d, curt);
          ans += d - tt + 1;
          curt = d - tt + 1;
        }
        cur = c;
        p[c] = k;
      }
      printf ("%d\n", ans);
   }
   return 0;
}
