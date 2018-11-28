#include <stdio.h>

int main () {
    int kase, n, k, i, h = 1;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d %d", &n, &k);
          int tmp = 1;
          for (i = 0; i < n; i++)
              tmp *= 2;
          printf("Case #%d: ",h++);
          if ( (k+1)%tmp  == 0) 
             printf("ON\n");
          else printf("OFF\n");
    }
    return 0;
}
