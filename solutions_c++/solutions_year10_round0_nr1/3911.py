#include <stdio.h>
int main()
{
    int C, Case, N, K, i;
    bool flag;
    
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &Case);
    for (C=1; C<=Case; ++C)
    {
        scanf("%d%d", &N, &K);
        for (i=0, flag=true; i<N; ++i)
        {
            if ((K & (1<<i)) == 0)
            {
               flag = false;
               break;
            }
        }
        if (flag)
           printf("Case #%d: ON\n", C);
        else
            printf("Case #%d: OFF\n", C);
    }
    return 0;
}
