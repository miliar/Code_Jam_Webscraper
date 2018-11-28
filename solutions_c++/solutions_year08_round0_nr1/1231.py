#include <stdio.h>
#include <string.h>

long n,k,t,s,q,d[1002][102],ans,i,j,x;
char se[1001][102],que[1001][102];
main()
{
 freopen("first.in","r",stdin);
 freopen("first.out","w",stdout);
 scanf("%d\n",&n);
 for(t=0;t<n;t++)
 {
    scanf("%d\n",&s);
    for(k=0;k<s;k++) gets(se[k]);
    scanf("%d\n",&q);
    for(k=0;k<q;k++) gets(que[k]);
    for(k=0;k<q;k++)
    for(j=0;j<s;j++)
    d[k][j]=20000000;
    for(k=0;k<s;k++)
    if (strcmp(que[0],se[k])!=0) d[0][k]=0;
    for(k=1;k<q;k++)
    {
      for(i=0;i<s;i++)
       if (!strcmp(que[k],se[i])) {x=i; break;}
      for(i=0;i<s;i++)
       for(j=0;j<s;j++)
       if(j!=x)
       if (d[k-1][i]+(j!=i)<d[k][j]) d[k][j]=d[k-1][i]+(j!=i);
    }
    ans=2000000;
    for(j=0;j<s;j++) if (d[q-1][j]<ans) ans=d[q-1][j];
    printf("Case #%d",t+1); printf(": %d\n",ans);
 }
}
