#include <cmath>
#include <cstdio>
#include <algorithm>
//#include <map>
//#include <numeric>
//#include <queue>
//#include <set>
//#include <string>
//#include <utility>
//#include <vector>

using namespace std;

typedef signed long long    int64;
typedef unsigned long long  uint64;
typedef signed int          int32;
typedef unsigned int        uint32;
typedef signed short        int16;
typedef unsigned short      uint16;
typedef signed char         int8;
typedef unsigned char       uint8;

#define T_MAX   (40)
#define N_MAX   (100)
#define L_MAX   (10000)
#define H_MAX   (L_MAX)

int main(void) {
    uint32  T;
    uint32  N;
    uint64  L;
    uint64  H;
    uint32  n;
    uint64  F[N_MAX];
    uint64  f;
    uint32  ni;
    int32   result;
    char    ends;
	
    scanf("%d\n", &T);
    //printf("T = %d\n", T);
	
    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        scanf("%u %Lu %Lu\n", &N, &L, &H);
        //printf("N = %u, L=%Lu, H=%Lu\n", N, L, H);
        
        /* Test Case run once */

        /* Input */
        for (n=0; n<N; n++)
        {
            scanf("%Lu", &F[n]);
        }
        scanf("%c", &ends);

        /* Check */
        for (f=L; f<=H; f++)
        {
            result = 0;
            for (ni=0; ni<N; ni++)
            {
                //printf("Check F[%u] = %Lu\n", ni, F[ni]);
                if (f > F[ni])
                {
                    if ((f % F[ni]) == 0)
                    {
                        continue;
                    }
                    else
                    {
                        result = -1;
                    }
                }
                else
                {
                    if ((F[ni] % f) == 0)
                    {
                        continue;
                    }
                    else
                    {
                        result = -1;
                    }
                }
            }

            if (result == 0)
            {
                /* found */
                result = 1;
                break;
            }
        }

        /* Output */
        if (result == 1)
        {
            printf("Case #%d: %Lu\n", Ti, f);
        }
        else
        {
            printf("Case #%d: NO\n", Ti);
        }
    }

    return 0;
}


