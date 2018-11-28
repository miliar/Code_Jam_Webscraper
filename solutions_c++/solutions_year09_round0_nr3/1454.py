#include <stdio.h>
#include <memory.h>

int d[512];

char w[] = "welcome to code jam\x01";

int main()
{
    int t;
    scanf("%d", &t);

    char s[512];
    gets(s);
    
    for (int tt=1, i, j, n; tt<=t; tt++)
    {
        gets(s);

        memset(d, 0, sizeof(d));

        for (i=0; w[i]; i++)
            for (j=0, n = !i; s[j]; j++)
            {
                int x = d[j];
                d[j] = s[j] == w[i] ? n : 0;
                n += x;
                if (n >= 10000)
                    n -= 10000;
            }
        
        printf("Case #%d: %04d\n", tt, n);
    }
    return 0;
}
