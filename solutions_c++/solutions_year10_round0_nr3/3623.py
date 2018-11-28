// C. Theme Park

#include <stdio.h>
#include <iostream.h>

typedef unsigned long long int integer;

int main ()
{
        // --- --- ---
        freopen("C-small.in","rt",stdin);
        freopen("C-small.out","wt",stdout);
        // --- --- ---
//      freopen("C-large.in","rt",stdin);
//      freopen("C-large.out","wt",stdout);
        // --- --- ---

        integer queue[1000];
        integer r, R, k, K, q0, q1, n, N, euros;
        unsigned int T;

        cin >> T;
        for (unsigned int cnum = 1; cnum <= T; cnum ++)
        {
                cin >> R;
                cin >> K;
                cin >> N;
                for (n = 0; n < N; n ++) cin >> queue[n];
                q0 = 0;                                                            // inclusive starting queue index
                euros = 0;

                for (r = 0; r < R; r ++)
                {
                        k = 0;                                                      // number of people aboard
                        q1 = q0;                                                    // exclusive ending queue index
                        while(k + queue[q0] <= K)
                        {
                                k += queue[q0 ++];
                                if (q0 >= N) q0 = 0;
                                if (q0 == q1) break;
                        }
                        euros += k;
                }
                printf("Case #%u: %llu\n", cnum, euros);
        }
        return 0;
}
