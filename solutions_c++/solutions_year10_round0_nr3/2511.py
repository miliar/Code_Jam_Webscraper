#include <stdio.h>

#define MAX 1000

int main()
{
    int num, r, k, n, s, t, e;
    int g[MAX];
    int profits;

    scanf("%d", &num);
    
    for (int i = 1; i <= num; ++i) {
        scanf("%d %d %d", &r, &k, &n);
        for (int j = 0; j < n; ++j)
            scanf("%d", &g[j]);

        profits = 0;
        s = 0;
        for (int j = 0; j < r; ++j) {            
            t = k;
            e = s;
            while (t-g[s] >= 0) {
                t -= g[s];
                profits += g[s];                
                s = (s+1)%n; 
                if (s == e)
                    break;
            }
        }

        printf("Case #%d: %d\n", i, profits);
    }

    return 0;
}
