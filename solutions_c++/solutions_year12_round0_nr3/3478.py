#include <cstdio>
#include <cstring>

int main()
{
    int t;
    char buffer[10];
    
    scanf("%d\n", &t);
    
    for (int i = 0; i < t; i++)
    {
        int a, b, count;
        scanf("%d %d", &a, &b);
        count = 0;
        printf("Case #%d: ", i + 1);
        
        for (int n = a; n < b; n++)
        {
            int mask, fst, snd, m, last_m;
            
            mask = 10;
            fst = n / mask;
            snd = n % mask;
            last_m = n;
            
            while (fst > 0)
            {
                sprintf(buffer, "%d%d\0", snd, fst);
                sscanf(buffer, "%d", &m);
                
                if (m != last_m && m > n && m <= b)
                {
                    count++;
                    //printf("%d, %d\n", n, m);
                    last_m = m;
                }
                
                mask *= 10;
                fst = n / mask;
                snd = n % mask;
            }
        }
        
        printf("%d\n", count);
    }
    
    return 0;
}

