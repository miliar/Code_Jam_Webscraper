#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define N_MAX   (1000)
#define Ci_MAX  (1000000)

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        uint32  N;
        uint32  P[N_MAX];
        uint64  all_xor_mask = 0;
        uint64  all_or_mask = 0;
        uint64  total_sum = 0;
        uint64  min_number = Ci_MAX;

        scanf("%d", &N);

        for (uint32 Ni=0; Ni<N; Ni++)
        {
            scanf("%d", &P[Ni]);
            all_xor_mask ^= P[Ni];
            total_sum += P[Ni];
            if (P[Ni] < min_number)
            {
                //printf("P[Ni] = %d\n", P[Ni]);
                min_number = P[Ni];
            }
        }

        if (all_xor_mask != 0)
        {
            printf("Case #%d: NO\n", Ti);
        }
        else
        {
            printf("Case #%d: %d\n", Ti, total_sum - min_number);
        }
    }

    return 0;
}


