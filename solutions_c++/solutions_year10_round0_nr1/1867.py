#include<cstdio>

int main()
{
    int t,n,k,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
      scanf("%d%d",&n,&k);
      if((k&((1<<n)-1)) == ((1<<n)-1))
        printf("Case #%d: ON\n",i);
      else
        printf("Case #%d: OFF\n",i);
    }
    return 0;
}
