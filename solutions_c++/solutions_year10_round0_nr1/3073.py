#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int i;
    int T, casen=1;
    int pow[35];
    
    for (i=1,pow[0]=1; i<31; i++) pow[i] = pow[i-1]<<1;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    scanf("%d", &T);
    while (T--)
    {
         int N, K;
         scanf("%d%d", &N, &K);
         
         if (K % pow[N] == pow[N]-1)
            printf("Case #%d: ON\n", casen++);
         else
            printf("Case #%d: OFF\n", casen++);
    }
    
   // system("pause");
    return 0;
}

/*
10
1 0
1 1
2 3
3 7
4 47
4 0
*/
