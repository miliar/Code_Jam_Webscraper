#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long uint32;
typedef unsigned long long uint64;

#define MAX_N 1010
uint32 gi[MAX_N];

int main(void)
{
    int T, N;
    uint32 R, k;
    
    scanf("%d", &T);
    for (int i=0; i<T; i++) {
        scanf("%lu %lu %d", &R, &k, &N);

        uint64 all=0;
        for (int j=0; j<N; j++) {
            scanf("%lu", &gi[j]);
            all += gi[j];
        }

        if (all <= k) {
            printf("Case #%d: %llu\n", i+1, all*R);
            continue;
        }

        uint64 euro = 0;
        uint32 sum = 0;
        int    pos = 0;
        while (R>0) {
            if (sum + gi[pos] <= k) {
                sum += gi[pos];
                if (pos == N-1) pos = 0;
                else pos++;
            }
            else {
                euro += sum;
                sum = 0;
                R--;
            }
        }

        printf("Case #%d: %llu\n", i+1, euro);
    }
    return 0;
}
