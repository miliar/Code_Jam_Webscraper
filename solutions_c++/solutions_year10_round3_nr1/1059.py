#include <stdio.h>
#include <stdlib.h>

typedef struct WIRE
{
    int a;
    int b;    
};

int main()
{
    int num = 1, T;
    WIRE wire[1000];
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    scanf("%d", &T);
    
    while(T--)
    {
        int N, result = 0;
        scanf("%d", &N);
        for(int i=0; i<=N-1; i++)
        {
            scanf("%d", &wire[i].a);
            scanf("%d", &wire[i].b); 
        }
        
        for(int i=0;  i<=N-2; i++)
        {
            for(int j=i+1; j<=N-1; j++)
            {
                if((wire[j].a > wire[i].a && wire[i].b > wire[j].b) 
                    || (wire[j].a < wire[i].a && wire[i].b < wire[j].b) )
                    result++;
            }    
        }
        
        printf("Case #%d: %d\n", num, result);
        num++;
            
    }
//    system("pause");
    return 0;
}
