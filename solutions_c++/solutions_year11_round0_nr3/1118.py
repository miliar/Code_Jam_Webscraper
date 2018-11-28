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

#define ll long long

int tn, nt, n;

int main(void)
{
//   freopen("C-small-attempt0.in", "r", stdin);
//   freopen("C-small-attempt0.out", "w", stdout);
   freopen("C-large.in", "r", stdin);
   freopen("C-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      scanf("%d", &n);
      int mi = 10000000, x = 0, sum = 0;
      for (int i=0; i<n; i++) {
        int t;
        scanf("%d", &t);
        mi = min (mi, t);
        sum += t;
        x ^= t;
      }

      if (x == 0) {
        printf ("%d\n", sum - mi);
      } else {
        printf ("NO\n");
      }
   }
   return 0;
}
