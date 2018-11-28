#include <stdio.h>
#include <stdlib.h>

int main()
{
    
    int T, N, K;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    scanf("%d", &T);
    int num = 1;
    while(T--)
    {
         scanf("%d %d", &N, &K);
         int a = 0, b = 1;
         
         if(K <= 0)
         {
              printf("Case #%d: OFF\n", num);
              num++; 
              continue;
         } 
         b = 1 << N;
         a = b-1;
         


         K = K%b;
         if(K==a)
             printf("Case #%d: ON\n", num);
         else
             printf("Case #%d: OFF\n", num);
         num++;
    }
//    system("pause");
    return 0;    
}
