#include<iostream>
using namespace std;
#include<stdlib.h>
int a[1002];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,i,j,R,K,N,k,sum1,s;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
       int count=0,sum=0;
       k=0;
       scanf("%d%d%d",&R,&K,&N);
       for(j=0;j<N;j++)
       {
           scanf("%d",&a[j]);
       }
       for(j=1;j<=R;j++)
       {
          sum1=0;
          s=0;
          while(1)
          {
                  s++;
             sum1=sum1+a[k%N];
             k++;
             if(sum1+a[k%N]>K||s>=N)
             break;
          }
          sum=sum+sum1;
       }
       printf("Case #%d: %d\n",i,sum);
    }
    return 0;
}
