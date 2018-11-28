#include <cstdio>
#include <cstring>

int main()
{
    int t;
    
    scanf("%d\n", &t);
    
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        
        int n, s, p, max;
        scanf("%d %d %d", &n, &s, &p);
        max = 0;
        //printf("%d %d %d\n", n, s, p);
        
        for (int j = 0; j < n; j++)
        {
            int total;
            scanf("%d", &total);
            //printf("%d ", total);
            
            if (total >= p)
            {
                float rest2 = (total - p) / 2;
                
                if (rest2 >= (p - 1))
                {
                    max++;
                }            
                else
                {
                    if (s > 0 && rest2 >= (p - 2))
                    {
                        s--;
                        max++;
                    }
                }
            }
        }
        
        printf("%d\n", max);
    }
    
    return 0;
}
