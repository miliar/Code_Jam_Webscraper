#include <stdio.h>

int a[1010], b[1010];

int main () {
    int kase, i, j, h = 1, n;
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d", &n);
          for (i = 0; i < n; i++) 
              scanf("%d %d", &a[i], &b[i]);
          int ans = 0;
          for (i = 0; i < n; i++)
              for (j = i+1; j < n; j++)
                  if ( (a[i]-a[j])*(b[i]-b[j]) < 0)
                     ans++;
          printf("Case #%d: %d\n",h++, ans);
    }
    return 0;
}
