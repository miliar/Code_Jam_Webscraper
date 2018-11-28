#include <stdio.h>

int main()
{
    int num, n, k;

    scanf("%d", &num);

    for (int i = 1; i <= num; ++i) {
        scanf("%d %d", &n, &k);
        
        if ((k+1) % (1<<n) == 0)
            printf("Case #%d: ON\n", i);
        else
            printf("Case #%d: OFF\n", i);
    }
}
