#include<stdio.h>
int main()
{
    int t,n,k;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
          scanf("%d%d",&n,&k);
          int tk=0;
          k++;
          while(k&&(!(k&1))) k>>=1,tk++;
          printf("Case #%d: %s\n",i,tk<n?"OFF":"ON");
    }
}
