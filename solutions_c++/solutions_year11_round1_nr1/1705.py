#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
int n,pd,pg;
int main(void)
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("1.out","w",stdout);
    int t;
    int i,D;
    int x,y;
    int m,k;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
        {
            scanf("%d%d%d",&n,&pd,&pg);
            D=1;
            if(pg==100 && 100 != pd)
                D = n+1;
            if(pg == 0 && pd > 0)
                D = n+1;
            for(;D<=n;D++)
                {
                    if((D*pd)%100 == 0)
                        {
                            break;
                        }
                }
            printf("Case #%d: ",i);
            if(D <= n)
                printf("Possible\n");
            else
                printf("Broken\n");
        }
    return 0;
}
