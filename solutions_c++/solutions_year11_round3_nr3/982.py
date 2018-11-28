#include <stdio.h>
#include <stdlib.h>
int main()
{
    int T,t,N,L,H,i,a[10000];
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%d%d%d",&N,&L,&H);
        for (i=1;i<=N;i++) scanf("%d",&a[i]);
        while (L<=H)
        {
              for (i=1;i<=N;i++)
                  if (a[i]%L!=0&&L%a[i]!=0) break;
              if (i<=N) L++;
              else break;
        }
        printf("Case #%d: ",t);
        if (L>H) printf("NO\n");
        else printf("%d\n",L);
    }
    return 0;
}
