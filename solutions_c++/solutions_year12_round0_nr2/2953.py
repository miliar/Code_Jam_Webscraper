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
#define P_MAX   (10)
#define N_MAX   (100)
#define S_MAX   (N_MAX)
#define Ti_MAX  (30)


int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        uint32 N;
        uint32 S;
        uint32 s = 0;
        uint32 P;
        uint32 ti[N_MAX];
        uint32 ans = 0;
        int32 i;

        /* Test Case run once */
        scanf("%d", &N);    //printf("N = %d\n", N);
        scanf("%d", &S);    //printf("S = %d\n", S);
        scanf("%d", &P);    //printf("P = %d\n", P);

        for (i=0; i<N; i++)
        {
            uint32 d,r;

            scanf("%d", &ti[i]);
            //printf("ti[%d] = %d\n", i, ti[i]);

            if (((ti[i] + 2) / 3) >= P)
            {
                ans += 1;
            }
            else if ((ti[i] >= 2) && (s < S))
            {
                if (((ti[i] + 4) / 3) >= P)
                {
                    ans += 1;
                    s += 1;
                }
            }
        }

        /* Print */
        printf("Case #%d: %d\n", Ti, ans);
    }

    return 0;
}


