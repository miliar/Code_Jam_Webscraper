#include <stdio.h>

int main()
{
    int T, cs;

    scanf("%d", &T);

    for (cs = 1; cs <= T; cs++)
    {
        int N, S, P, googlers, accepted, surprise;
        int TOTAL[100][4];

        surprise = accepted = 0;

        scanf("%d", &N);
        scanf("%d", &S);
        scanf("%d", &P);

        //printf("NSP = %d %d %d\n", N, S, P);

        for (googlers = 0; googlers < N; googlers++)
        {
            int mod, mid, eval;

            scanf("%d", &TOTAL[googlers][0]);

            mod = TOTAL[googlers][0] % 3;
            mid = TOTAL[googlers][0] / 3;

            TOTAL[googlers][1] = mid + mod;
            TOTAL[googlers][2] = mid;
            TOTAL[googlers][3] = mid;

            if (mod == 0 && surprise < S && (mid + 1) == P)
            {
                if (TOTAL[googlers][3] > 0)
                {
                    TOTAL[googlers][1]++;
                    TOTAL[googlers][3]--;
                    surprise++;
                }
            }
            else if (mod == 2)
            {
                if ((mid + mod - 1) >= P && TOTAL[googlers][1] > 0)
                {
                    TOTAL[googlers][1]--;
                    TOTAL[googlers][2]++;
                }
                else
                {
                    if (surprise < S)
                    {
                        surprise++;
                    }
                    else
                    {
                        TOTAL[googlers][1] = 0; // invalidate
                        TOTAL[googlers][2] = 0;
                        TOTAL[googlers][3] = 0;
                    }
                }
            }

            for (eval = 1; eval <= 3; eval ++)
            {
                if (TOTAL[googlers][eval] >= P)
                {
                    accepted++;
                    break;
                }
            }

            //printf("Case #%d: googler[%d] = (%d) %d %d %d\n", cs, googlers, TOTAL[googlers][0], TOTAL[googlers][1], TOTAL[googlers][2], TOTAL[googlers][3]);
        }

        printf("Case #%d: %d\n", cs, accepted);
    }

    return 0;
}

