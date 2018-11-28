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

#define T_MAX   (20)
#define N_MAX   (100)

int main(void) {
    uint32  T;
    uint32  N;
    char    score[N_MAX][N_MAX];
    uint32  Total_OP[N_MAX];
    uint32  Total_Win[N_MAX];
    uint32  Total_Lose[N_MAX];
    char    ends;
    uint32  row, col;
    double   WP[N_MAX];
    double   OWP[N_MAX];
    double   OOWP[N_MAX];
    double   RPI[N_MAX];
    uint32  Total_OWP;
	
    scanf("%d\n", &T);
    //printf("T = %d\n", T);
	
    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        scanf("%d\n", &N);
        //printf("N = %d\n", N);
        /* Test Case run once */

        for (row=0; row<N; row++)
        {
            WP[row] = 0;
            Total_OP[row] = 0;
            Total_Win[row] = 0;
            Total_Lose[row] = 0;
            for (col=0; col<N; col++)
            {
                scanf("%c", &score[row][col]);
                if (score[row][col] == '1')
                {
                    Total_OP[row]++;
                    Total_Win[row]++;
                }
                else if (score[row][col] == '0')
                {
                    Total_OP[row]++;
                    Total_Lose[row]++;
                }
            }
            scanf("%c", &ends);
            //printf("Team %d: OP = %d, Win = %d, Lose = %d\n", row, Total_OP[row], Total_Win[row], Total_Lose[row]);
            //printf("test = %f\n", ((double)Total_Win[row] / (double)Total_OP[row]));
            WP[row] = (Total_OP[row] != 0)? ((double)Total_Win[row] / (double)Total_OP[row]) : 0.0;
            //printf("Team %d: WP = %.12f\n", row, WP[row]);
        }

        /* caculate OWP */
        for (row=0; row<N; row++)
        {
            uint32 win = 0;
            uint32 sum = 0;

            OWP[row] = 0.0;
            Total_OWP = 0;
            for (col=0; col<N; col++)
            {
                if (row == col)
                    continue;
                if (score[row][col] != '.')
                {
                    win = 0;
                    sum = 0;
                    
                    for (uint32 i=0; i<N; i++)
                    {
                        if ((row == i) || (col == i))
                            continue;

#if 0
                        if (score[row][i] != '.')
                        {
#endif
                            if (score[col][i] == '1')
                            {
                                win ++;
                                sum ++;
                            }
                            else if (score[col][i] == '0')
                            {
                                sum ++;
                            }
#if 0
                        }
#endif
                    }
                    //printf("win = %d, sum = %d\n", win, sum);
                    Total_OWP ++;
                    //printf("w/s = %.12f\n", (double)win / (double)sum);
                    OWP[row] += (double)((double)win / (double)sum);
                }
            }
            //printf("Total_OWP = %d, OWP[row] = %f\n", Total_OWP, OWP[row]);
            OWP[row] = (Total_OWP != 0)? (OWP[row] / (double)Total_OWP) : 0.0;
            //printf("Team %d: OWP = %.12f\n", row, OWP[row]);
        }

        printf("Case #%d:\n", Ti);
        /* caculate OOWP */
        for (row=0; row<N; row++)
        {
            OOWP[row] = 0.0;
            Total_OWP = 0;

            for (col=0; col<N; col++)
            {
                if (row == col)
                    continue;
                if (score[row][col] != '.')
                {
                    //printf("OWP[col] = %.12f\n", OWP[col]);
                    OOWP[row] += OWP[col];
                    Total_OWP++;
                }
            }
            //printf("Team %d: OOWP[row] = %f, Total_OWP = %d\n", row, OOWP[row], Total_OWP);
            OOWP[row] = (Total_OWP != 0)? (OOWP[row] / (double)Total_OWP) : 0.0;
            //printf("Team %d: OOWP = %.12f\n", row, OOWP[row]);

            /* RPI */
            //printf("Team %d: WP = %.12f, OWP = %.12f, OOWP = %.12f\n", row, WP[row], OWP[row], OOWP[row]);
            RPI[row] = (0.25 * WP[row]) + (0.5 * OWP[row]) + (0.25 * OOWP[row]);
//            printf("Team %d: RPI = %.12f\n", row, RPI[row]);

            /* Print */
            printf("%.12f\n", Ti, RPI[row]);

        }
    }

    return 0;
}


