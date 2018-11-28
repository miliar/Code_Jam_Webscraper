#include <cstdio>
#include <cstring>

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,tt,test,n,k;
    scanf("%d",&test);
    for (tt = 1; tt<=test; tt++) {
      scanf("%d%d",&n,&k);
      int ans = 0;
      for (i = 1; i<=n ; i++) {
        if ((k & 1) != 1) break;
        ans++;
        k = k / 2;   
      }
      if (ans>=n)
         printf("Case #%d: ON\n",tt);
         else printf("Case #%d: OFF\n",tt); 
    }
    return 0;
}
