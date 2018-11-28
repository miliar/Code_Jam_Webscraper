#include<cstdio>

int main()
{
    int t, teste;
    scanf("%d", &teste);
    for (t=1; t<=teste; t++)
    {
        int n, k;
        scanf("%d %d", &n, &k);
        int mask = (1 << n) - 1;
        if ((mask & k) == mask)
        {
            printf("Case #%d: ON\n", t);
        }
        else
        {
            printf("Case #%d: OFF\n", t);            
        }
    }
    return 0;    
}
