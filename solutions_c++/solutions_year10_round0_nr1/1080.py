#include <stdio.h>

int main()
{
    int i,m,n,flag,tt,cas;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cas);
    for (tt = 1; tt <= cas; tt ++)
    {
        scanf("%d%d",&m,&n);
        flag = 1;
        for (i = 0; i < m; i ++)
        {
            if (n % 2 == 0)
            {
                flag = 0;
                break;
            }
            n /= 2;
        }
        printf("Case #%d: ",tt);
        if (flag)
            puts("ON");
        else
            puts("OFF");
    }
    return 0;
}
