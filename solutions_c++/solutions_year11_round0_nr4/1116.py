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

int tn, nt, n;
int a[1005];

int main(void)
{
//   freopen("D-small-attempt0.in", "r", stdin);
//   freopen("D-small-attempt0.out", "w", stdout);
   freopen("D-large.in", "r", stdin);
   freopen("D-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      scanf("%d", &n);
      int ans = 0;
      for (int i=0; i<n; i++) {
        scanf("%d", &a[i]);
        if (a[i] != i+1)
          ans++;
      }
      printf ("%d.000000\n", ans);
   }
   return 0;
}
