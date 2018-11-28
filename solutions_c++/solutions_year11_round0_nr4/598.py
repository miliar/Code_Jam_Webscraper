#include <stdio.h>
#include <algorithm>
using namespace std;

int a[1010], b[1010];

int main () {
    int i, kase, n, h = 1;
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d", &n);
          for (i = 0; i < n; ++i) {
              scanf("%d", &a[i]);
              b[i] = a[i];
          }
          sort(b,b+n);
          double m = 0;
          for (i = 0; i < n; ++i) {
              if (a[i] != b[i])
                 m++;
          }
          printf("Case #%d: %.6lf\n",h++,m);
    }
    return 0;
}

