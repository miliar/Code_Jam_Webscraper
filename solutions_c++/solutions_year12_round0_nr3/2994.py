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

#define T_MAX   (50)
#define N_MAX   (2000000)

#define BUF_LEN (16)

void shift_string(char *src, int len, int shift, char *dst)
{
    int32 i;
    
    for (i=0; i<len; i++)
    {
        dst[i] = src[(i + shift) % len];
    }

    dst[len] = '\0';
}

int main(void) {
    uint32 T;

    scanf("%d", &T);
    //printf("T = %d\n", T);

    for (uint32 Ti = 1; Ti <= T; ++Ti)
    {
        uint32  A, B;
        char str[BUF_LEN];
        char strShift[BUF_LEN];
        int32 n, m, j;
        uint32 t;
        uint8 match[N_MAX];

        /* Test Case run once */
        scanf("%d %d", &A, &B); //printf("A: %d, B: %d\n", A, B);

        t = 0;
        for (n=A; n<B; n++)
        {
            sprintf(str, "%d", n);
            //printf("STR: %s", str);

            /* calculate m */
            memset(match, 0, sizeof(match));
            for (j=1; j<strlen(str); j++)
            {
                shift_string(str, strlen(str), j, strShift);
                //printf("SHT: %s", strShift);
                m = atoi(strShift);
                //printf("n = %u, m = %u\n", n, m);

                if (n < m)
                {
                    if ((m > A) && (m <= B))
                    {
                        if (match[m] == 0)
                        {
                            match[m] = 1;
                            t += 1;
                            //printf("t[%u] n = %u, m = %u\n", t, n, m);
                        }
                    }
                }

            }
        }

        /* Print */
        printf("Case #%d: %d\n", Ti, t);
    }

    return 0;
}


