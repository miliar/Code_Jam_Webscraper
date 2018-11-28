#include <stdio.h>


int main () {
    int kase, i, n, h = 1, a;
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d", &n);
          int x = 0;
          long long sum = 0;
          int Min = 100000000;
          for (i = 0; i < n; ++i) {
              scanf("%d", &a);
              x ^= a;
              sum += a;
              if (Min > a)
                 Min = a;
          }
          printf("Case #%d: ", h++);
          if (x != 0) 
             printf("NO\n");
          else
              printf("%lld\n", sum-Min);
    }
    return 0;
}
