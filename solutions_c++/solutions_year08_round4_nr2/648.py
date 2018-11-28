#include<stdio.h>

int N,M,T,A;

int abs(int n)
{
    return n>0?n:-n;
}

void solve()
{
     int i,j,k,l;
     int tt;
     for(i=0;i<=N;i++)
       for(j=0;j<=M;j++)
          for(k=0;k<=N;k++)
            for(l=0;l<=M;l++)
            {
               tt=i*l-j*k;
               if(abs(tt)==A)
               {
                   printf("%d %d %d %d %d %d\n",0,0,i,j,k,l);
                   return;
               }
            }
       printf("IMPOSSIBLE\n");
}

int main()
{
    int i;
    //freopen("B.in","r",stdin);
    //freopen("B.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
       scanf("%d%d%d",&N,&M,&A);
       printf("Case #%d: ",i);
       solve();
    }
    return 0;
}
                            
            
