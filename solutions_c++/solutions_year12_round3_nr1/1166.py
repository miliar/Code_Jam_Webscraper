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

#define T_MAX   (50)
#define Mi_MAX  (10)
#define N_MAX   (1000 + 1)


int main(void) {
    uint32 T;
    
    scanf("%d", &T); //printf("T = %d\n", T);
    
    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        uint32 N;
        uint32 Mi[N_MAX];
        uint32 I[N_MAX][Mi_MAX];
        
        uint32 P[N_MAX][N_MAX];
        uint32 R[N_MAX];
        uint32 found = 0;
        uint32 good = 0;

        /* Test Case run once */
        scanf("%d", &N); //printf("N=%u\n", N);

        good = 0;
        memset(P, 0, sizeof(P));
        memset(R, 0, sizeof(R));
        for (uint32 Ii=1; Ii <= N; Ii++)
        {
            scanf("%d", &Mi[Ii]);   //printf("Mi[%u] = %u\n", Ii, Mi[Ii]);

            for (uint32 Jj=1; Jj <= Mi[Ii]; Jj++)
            {
                scanf("%d", &I[Ii][Jj]);    //printf("I[%u][%u] = %u\n", Ii, Jj, I[Ii][Jj]);

                R[I[Ii][Jj]] += 1;  /* be ref */
            }
        }

        do 
        {
            found = 0;
            for (uint32 i=1; i<=N; i++)
            {
                /* reduce */
                if ((R[i] == 0) && (Mi[i] != 0))
                {
                    found = 1;

                    for (uint32 j=1; j<=Mi[i]; j++)
                    {
                        if (P[I[i][j]][i] != 0)
                        {
                            //printf("Good: Case = %u\n", Ti);
                            good = 1;
                            break;
                        }
                        else
                        {
                            //printf("C(%u) cover C(%u)\n", I[i][j], i);
                            P[I[i][j]][i] = 1;
                            for (uint32 k=1; k<=N; k++)
                            {
                                if (P[i][k])
                                {
                                    //printf("    C(%u) get C(%u)\n", I[i][j], k);
                                    if (P[I[i][j]][k])
                                    {
                                        good = 1;
                                        break;
                                    }
                                    else
                                    {
                                        P[I[i][j]][k] = 1;
                                    }
                                }
                            }

                            R[I[i][j]] -= 1;
                        }
                    }

                    Mi[i] = 0;
                }
            }

        } while (found);



        /* Print */
        printf("Case #%d: %s\n", Ti, (good)? "Yes" : "No");
    }

    return 0;
}


