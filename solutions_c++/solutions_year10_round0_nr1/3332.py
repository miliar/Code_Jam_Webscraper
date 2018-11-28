#include<stdio.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,k;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
    {
        scanf("%d%d",&n,&k);
        //printf("<<<<%d>>>>\n",1<<n);
        if(k < ((1<<n) - 1))
            printf("Case #%d: OFF\n",i);
        else
        {
            if((k - ((1<<n)-1)) % (1<<n) == 0)
                printf("Case #%d: ON\n",i);
            else
                printf("Case #%d: OFF\n",i);
           /* if(((n*2) - 1) % 2 == 0)
            {
                if(k % 2 == 0)
                    printf("Case #%d: ON\n",i);
                else
                    printf("Case #%d: OFF\n",i);
            }
            else
            {
                if(k % 2 == 0)
                    printf("Case #%d: OFF\n",i);
                else
                    printf("Case #%d: ON\n",i);
            }*/
        }
    }
    return 0;
}
