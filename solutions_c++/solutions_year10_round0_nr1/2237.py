#include<iostream>
using namespace std;
#include<stdlib.h>
int fuct(int a )
{
    int sum=2,i;
    for(i=1;i<a;i++)
      sum=sum*2;
      return sum;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,n,k,j;
    scanf("%d",&T);
    for(j=1;j<=T;j++)
    {
       scanf("%d%d",&n,&k);
       if(k%fuct(n)==(fuct(n)-1))
       {
         printf("Case #%d: ON\n",j);
       }
       else
       {
           printf("Case #%d: OFF\n",j);
       }
    }
    return 0;
}
