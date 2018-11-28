#include<stdio.h>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,N,K,i,j;
    bool ON;
    scanf("%d",&n);
    for (i=1;i<=n;i++){
          scanf("%d %d",&N,&K);
          ON=true;
          for (j=1;j<=N;j++,K>>=1)
              if (!(K&1)){
                 ON=false;
                 break;
              }
          printf("Case #%d: ",i);
          if (ON) printf("ON\n");
          else printf("OFF\n");
    }
    return 0;
}
