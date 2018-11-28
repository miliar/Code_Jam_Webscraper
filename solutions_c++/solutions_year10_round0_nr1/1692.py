#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef unsigned long uint32;

int main(void)
{
    uint32 Ncase, N, K;
    scanf("%lu\n", &Ncase);
    for (uint32 i=0; i<Ncase; i++){
        scanf("%lu %lu\n", &N, &K);
        uint32 needK = (uint32) pow(2.0, N) - 1;
        printf("Case #%lu: ", i+1);
        if (K == 0) printf("OFF\n");
        else if (K == needK) printf("ON\n");
        else if (K <  needK) printf("OFF\n");
        else if (K >  needK) {
            uint32 diff = K - needK;
            if ( diff % (needK+1) == 0  ) printf("ON\n");
            else printf("OFF\n");
        }
    }
    return 0;
}
