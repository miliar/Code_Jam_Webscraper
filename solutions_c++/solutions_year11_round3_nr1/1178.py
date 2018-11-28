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
#define R_MAX   (50)
#define C_MAX   (50)

int main(void) {
    uint32  T;
    uint32  R;
    uint32  C;
    char    floor[R_MAX][C_MAX];
    uint32  w_sum;
    uint32  b_sum;
    char    ends;
    int32   result;
    uint32  r, c;
	
    scanf("%d\n", &T);
    //printf("T = %d\n", T);
	
    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        scanf("%d %d\n", &R, &C);
        //printf("N = %d\n", N);
        
        /* Test Case run once */

        result = 0;
        /* Input */
        w_sum = 0;
        b_sum = 0;
        for (r=0; r<R; r++)
        {
            for (c=0; c<C; c++)
            {
                scanf("%c", &floor[r][c]);
                if (floor[r][c] == '.')
                {
                    w_sum += 1;
                }
                else if (floor[r][c] == '#')
                {
                    b_sum += 1;
                }
            }
            scanf("%c", &ends);
        }

        /* Check */
        if (b_sum % 4 == 0)
        {
            /* try to solve */
            for (r=0; r<(R - 1); r++)
            {
                for (c=0; c<(C - 1); c++)
                {
                    if (floor[r][c] == '#')
                    {
                        /* should 4 piece full if it can be solved */
                        if ((floor[r+0][c+1] == '#') && \
                            (floor[r+1][c+0] == '#') && \
                            (floor[r+1][c+1] == '#'))
                        {
                            floor[r+0][c+0] = '/';
                            floor[r+1][c+1] = '/';
                            floor[r+0][c+1] = '\\';
                            floor[r+1][c+0] = '\\';
                        }
                        else
                        {
                            result = -1;
                            break;
                        }
                    }
                }
                if (result < 0)
                    break;
            }
        }
        else
        {
            result = -1;
        }

        /* Output */
        printf("Case #%d:\n", Ti);
        if (result < 0)
        {
            printf("Impossible\n");
        }
        else
        {
            for (r=0; r<R; r++)
            {
                for (c=0; c<C; c++)
                {
                    printf("%c", floor[r][c]);
                }
                printf("\n");
            }
        }
    }
    
    return 0;
}


