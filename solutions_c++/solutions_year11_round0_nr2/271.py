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
#define C_MIN   (0)
#define C_MAX   (36)
#define D_MIN   (0)
#define D_MAX   (28)
#define N_MIN   (1)
#define N_MAX   (100)


int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        int32 C;
        int32 D;
        int32 N;
        char Combine[C_MAX][3];
        char Opposed[D_MAX][2];
        char Invoke[N_MAX];
        char Elist[N_MAX];
        int32 Elen = 0;

        /* Test Case run once */

        /* Combine */
        scanf("%d", &C);
        //printf("C = %d\n", C);
        for (uint32 Ci=0; Ci<C; Ci++)
        {
            char str[8];
            
            scanf("%s", &Combine[Ci]);
#if 0
            printf("STR = %s\n", Combine[Ci]);
            printf("Combine[Ci][0] = %c\n", Combine[Ci][0]);
            printf("Combine[Ci][1] = %c\n", Combine[Ci][1]);
            printf("Combine[Ci][2] = %c\n", Combine[Ci][2]);
#endif
        }

        /* Opposed */
        scanf("%d", &D);
        //printf("D = %d\n", D);
        for (uint32 Di=0; Di<D; Di++)
        {
            scanf("%s", &Opposed[Di]);
            //printf("Opposed[%d] = %s\n", Di, Opposed[Di]);
        }

        /* Invoke list */
        scanf("%d", &N);
        //printf("N = %d\n", N);
        scanf("%s", &Invoke);
        //printf("Invoke = %s\n", Invoke);

        /* Process */
        Elen = 0;
        for (uint32 ni=0; ni<N; ni++)
        {
            int32 combined = 0;
            int32 opposed = 0;
            Elist[Elen] = Invoke[ni];
            Elen ++;

            /* check combine */
            if (Elen > 1)
            {
                for (uint32 ci=0; ci<C; ci++)
                {
                    if (((Elist[Elen-1] == Combine[ci][0]) && (Elist[Elen-2] == Combine[ci][1])) || \
                        ((Elist[Elen-1] == Combine[ci][1]) && (Elist[Elen-2] == Combine[ci][0])))
                    {   /* Combine match */
                        //printf("STR: %12s\n", Elist);
                        //printf("COMBINE: %c and %c -> %c\n", Combine[ci][0], Combine[ci][1], Combine[ci][2]);
                        Elen --;
                        Elist[Elen-1] = Combine[ci][2];
                        combined = 1;
                        break;
                    }
                }
            }

            /* check opposed ? */
            if ((Elen > 1) && (!combined))
            {
                for (uint32 ei=0; ei<Elen; ei++)
                {
                    for (uint32 di=0; di<D; di++)
                    {
                        if ((Elist[ei] == Opposed[di][0]) || (Elist[ei] == Opposed[di][1]))
                        {
                            for (uint32 ej=ei+1; ej<Elen; ej++)
                            {
                                if (((Elist[ei] == Opposed[di][0]) && (Elist[ej] == Opposed[di][1])) || \
                                    ((Elist[ei] == Opposed[di][1]) && (Elist[ej] == Opposed[di][0])))
                                {   /* Opposed !! */
                                    //printf("OPPOSED: %c and %c\n", Opposed[di][0], Opposed[di][1]);
                                    opposed = 1;
                                    break;
                                }
                            }

                            if (opposed)
                                break;
                        }
                    }

                    if (opposed)
                        break;
                }
            }

            if (opposed)
            {
                Elen = 0;
            }
        }

//            printf("Case #%d: %d\n", Ti, total_sum - min_number);
        /* Print */
        printf("Case #%d: [", Ti);
        for (uint32 p=0; p<Elen; p++)
        {
            if (p > 0)
                printf(", ");
            printf("%c", Elist[p]);
        }
        printf("]\n");
    }

    return 0;
}


