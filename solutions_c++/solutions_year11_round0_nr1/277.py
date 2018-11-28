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
#define N_MAX   (100)

struct ins_s
{
    char    R;
    int32   P;
};

int main(void) {
    char line[2048];
    uint32 T;

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%d", &T);
    //printf("T = %d\n", T);
    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        uint32  N;
        struct ins_s INS[N_MAX];
        uint32  O_SEQ[N_MAX];
        uint32  B_SEQ[N_MAX];
        int32   O_CMD[N_MAX];
        int32   B_CMD[N_MAX];
        int32   O_POS = 0;
        int32   B_POS = 0;
        uint32  W_INS = 0;
        uint32  STEP = 0;
        uint32  O_NOW = 0;
        uint32  B_NOW = 0;
        uint32  TIMES = 0;
        char    tmp[16];

        /* Init */
        for (uint32 Ii=0; Ii<N_MAX; Ii++)
        {
            O_SEQ[Ii] = -1;
            O_CMD[Ii] = -1;
            O_POS = 0;
            B_SEQ[Ii] = -1;
            B_CMD[Ii] = -1;
            B_POS = 0;
        }

        N = 0;
        fgets(line, sizeof(line), stdin);
        for (uint32 Ci=0,Ch=0,Nt=0; Ci<sizeof(line); Ci++)
        {
            if ((N != 0) && (Nt == N))
                break;

            if (line[Ci] == 0 || line[Ci] == ' ')
            {
                if (N == 0)
                {
                    strncpy(tmp, &line[Ch], Ci - Ch);
                    tmp[Ci-Ch] = 0;

                    N = (uint32)atoi(tmp);
                }
                else
                {
                    strncpy(tmp, &line[Ch], Ci - Ch);
                    tmp[Ci-Ch] = 0;

                    if ((tmp[0] == 'O') || (tmp[0] == 'B'))
                    {
                        INS[Nt].R = tmp[0];
                    }
                    else
                    {
                        INS[Nt].P = (int32)atoi(tmp);
                        Nt++;
                    }
                }

                Ch = Ci + 1;
            }

        }

#if 0
        scanf("%d " \
              "%c %d %c %d %c %d %c %d %c %d %c %d %c %d %c %d %c %d %c %d",
              &N, \
              &INS[0].R, &INS[0].P, &INS[1].R, &INS[1].P, &INS[2].R, &INS[2].P, &INS[3].R, &INS[3].P, &INS[4].R, &INS[4].P,
              &INS[5].R, &INS[5].P, &INS[6].R, &INS[6].P, &INS[7].R, &INS[7].P, &INS[8].R, &INS[8].P, &INS[9].R, &INS[9].P);
#endif
        //printf("N = %d\n", N);
        for (uint32 Ni=0; Ni<N; Ni++)
        {
            //printf("INS[%d].R = %c, .P = %d\n", Ni, INS[Ni].R, INS[Ni].P);

            if (INS[Ni].R == 'O')
            {
                O_SEQ[O_POS] = Ni;
                O_CMD[O_POS] = INS[Ni].P;
                O_POS++;
            }
            else
            {
                B_SEQ[B_POS] = Ni;
                B_CMD[B_POS] = INS[Ni].P;
                B_POS++;
            }
        }
        O_CMD[O_POS] = -1;
        B_CMD[B_POS] = -1;

        /* DO */
        O_POS = 0;
        B_POS = 0;
        W_INS = 0;
        STEP = 0;
        O_NOW = 1;
        B_NOW = 1;
        TIMES = 0;
        while ((O_CMD[O_POS] != -1) || (B_CMD[B_POS] != -1))
        {
            uint32 pressed = 0;

            /* walk ? */
            if ((O_CMD[O_POS] != -1))
            {
                if (O_CMD[O_POS] != O_NOW)
                {
                    if (O_NOW > O_CMD[O_POS])
                    {
                        O_NOW--;
                    }
                    else
                    {
                        O_NOW++;
                    }
                    //printf("O move to %d\n", O_NOW);
                }
                else
                {
                    if (STEP == O_SEQ[O_POS])
                    {
                        pressed = 1;
                        //printf("O press button %d\n", O_CMD[O_POS]);
                        STEP++;
                        O_POS++;
                    }
                }
            }


            if ((B_CMD[B_POS] != -1))
            {

                if (B_CMD[B_POS] != B_NOW)
                {
                    if (B_NOW > B_CMD[B_POS])
                        B_NOW--;
                    else
                        B_NOW++;

                    //printf("B move to %d\n", B_NOW);

                }
                else
                {
                    if ((pressed == 0) && (STEP == B_SEQ[B_POS]))
                    {
                        //printf("B press button %d\n", B_CMD[B_POS]);

                        STEP++;
                        B_POS++;
                    }
                }
            }
            
            TIMES++;
        }

        //printf("TIMES = %d\n", TIMES);

        printf("Case #%d: %d\n", Ti, TIMES);

#if 0
        if ((k + 1) % (1 << n) == 0) printf("Case #%d: %s\n", Ti, "ON");
        else printf("Case #%d: %s\n", Ti, "OFF");
#endif
    }

    return 0;
}


