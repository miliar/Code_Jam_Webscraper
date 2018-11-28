#include <stdio.h>
#define MaxN 105
int main(){
    int i,j,T,N,R[MaxN],P[MaxN],Orange,Blue,ans,order;
    char s[2];
    freopen("Bot Trust.in","r",stdin);
    freopen("Bot Trust.out","w",stdout);
    scanf("%d",&T);
    for (j=1;j<=T;j++){
          scanf("%d",&N);
          for (i=1;i<=N;i++){
              scanf("%s%d",s,&P[i]);
              if (s[0]=='O') R[i]=0;
              else R[i]=1;
          }
          Orange=1;
          Blue=1;
          ans=0;
          order=1;
          while (order<=N)
          {
              ans++;
              if (R[order]==0){
                 i=order;
                 while (i<=N&&R[i]!=1)
                       i++;
                 if (!(i>N||Blue==P[i]))
                    if (Blue<P[i])
                       Blue++;
                    else 
                       Blue--;
                 
                 if (Orange==P[order])
                    order++;
                 else if (Orange<P[order])
                         Orange++;
                      else
                         Orange--;
              } else{
                 i=order;
                 while (i<=N&&R[i]!=0)
                       i++;
                 if (!(i>N||Orange==P[i]))
                    if (Orange<P[i])
                       Orange++;
                    else
                       Orange--;
                 
                 if (Blue==P[order])
                    order++;
                 else if (Blue<P[order])
                         Blue++;
                      else
                         Blue--;
              }
          }
          printf("Case #%d: %d\n",j,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
