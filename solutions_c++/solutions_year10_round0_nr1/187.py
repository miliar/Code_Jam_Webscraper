#include <stdio.h>
int t1,t0,n,k;
int main()
{
    freopen("a2.in","r",stdin);
    freopen("a2.out","w",stdout);
     scanf("%d",&t1);
    for (int t0=1;t0<=t1;t0++)
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",t0);
        if ((((1<<n)-1)|k)==k) printf("ON\n");
        else printf("OFF\n");
    }
}
