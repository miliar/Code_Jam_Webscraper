#include<iostream>
using namespace std;

long long T,N,A[10005],L,H,i,j,k,F,flag;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%lld",&T);
    for (k=1;k<=T;k++)
    {
          scanf("%lld%lld%lld",&N,&L,&H);
          for (i=0;i<N;i++)
              scanf("%lld",&A[i]);
          F=0;    
          printf("Case #%lld: ",k);
          for (i=L;i<=H;i++)
          {
              flag=1;
              for (j=0;j<N;j++)
                  if (A[j]%i!=0 && i%A[j]!=0)
                     flag=0;
              if (flag)
              {
                       printf("%lld\n",i);
                       F=1;
                       i=H+1;
              }
          }
          if (!F)
             printf("NO\n");       
    }
}
