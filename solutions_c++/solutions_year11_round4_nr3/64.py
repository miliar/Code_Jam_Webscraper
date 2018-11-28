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

long long n;
int tn, nt;
int a[1000005];
long long p[100005];
long long p2[100005];
int k;

int main(void)
{
//   freopen("C-small-attempt0.in", "r", stdin);
//   freopen("C-small-attempt0.out", "w", stdout);
   freopen("C-large.in", "r", stdin);
   freopen("C-large.out", "w", stdout);

   for (int i=2; i<=1000; i++) {
     for (int j=i*i; j<=1000000; j+=i) {
       a[j] = 1;
     }
   }

   for (int i=2; i<=1000000; i++) {
     if (!a[i]) {
       p2[k] = (long long)i * i;
       p[k++] = i;
     }
   }

   scanf("%d", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      scanf("%I64d", &n);
      int ans = n >= 2;

      int j;
      for (j = 0; j<k && p[j] * p[j] * p[j] <= n; j++) {
        long long x = n / p[j];
        while (x >= p[j]) {
          x /= p[j];
          ans++;
        }
      }
      int t = lower_bound(p2+j, p2+k, n + 1) - p2;
      ans += t - j;

      printf ("%d\n", ans);
   }
   return 0;
}
