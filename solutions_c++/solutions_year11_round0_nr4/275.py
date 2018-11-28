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

#define T_MAX   (100)
#define N_MAX   (1000)


int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32   N;
        uint32  Num[N_MAX];
        int32   fixed_num = 0;

        /* Test Case run once */

        scanf("%d", &N);
        //printf("N = %d\n", N);
        for (uint32 Ni=0; Ni<N; Ni++)
        {
            scanf("%d", &Num[Ni]);
            if (Num[Ni] == (Ni + 1))
                fixed_num ++;
        }

        


        /* Print */
        printf("Case #%d: %d.000000\n", Ti, (N - fixed_num));
    }

    return 0;
}


