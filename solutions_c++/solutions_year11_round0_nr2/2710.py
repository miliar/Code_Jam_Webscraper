/*
 * Main.cpp
 *
 *  Created on: 2011/05/07
 *      Author: Philo
 */

#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <deque>
#include <vector>
#include <string>
#include <algorithm>

typedef char  s8;
typedef short s16;
typedef long  s32;
typedef long long s64;
typedef unsigned char  u8;
typedef unsigned short u16;
typedef unsigned long  u32;
typedef unsigned long long u64;

#ifdef __DEBUG__
#define DBG(...) \
{ \
    printf("%s:%d ", __FILE__, __LINE__); \
    printf(__VA_ARGS__); \
    fflush(stdout); \
}
#else
#define DBG(fmt, ...) void(fmt)
#endif

const char INPUT_FILE_NAME[]  = "D:/Temp/input.in";
const char OUTPUT_FILE_NAME[] = "D:/Temp/output.out";

int bD[28][2];

void ClearBD()
{
    for (int i = 0; i < 28; i++)
        bD[i][0] = bD[i][1] = 0;
}

int main(int argc, char *argv[])
{
    u64 caseNum;
    FILE *fp = fopen(INPUT_FILE_NAME, "r");
    fscanf(fp, "%lld\n", &caseNum);

    char C[36][3];
    char D[28][2];
    char N[101];
    for (u32 j = 0; j < caseNum; j++)
    {
        int cntC;
        int cntD;
        int cntN;

        fscanf(fp, "%d ", &cntC);
        for (int i = 0; i < cntC; i++)
        {
            fscanf(fp, "%c%c%c ", &C[i][0], &C[i][1], &C[i][2]);
        }

        fscanf(fp, "%d ", &cntD);
        for (int i = 0; i < cntD; i++)
        {
            fscanf(fp, "%c%c ", &D[i][0], &D[i][1]);
        }

        fscanf(fp, "%d ", &cntN);
        fscanf(fp, "%s\n", N);

        char ans[100];
        int len = -1;
        for (int i = 0; i < cntN; i++)
        {
            bool cont = false;
            if (len >= 0)
            {
                for (int k = 0; k < cntC; k++)
                {
                    if ((ans[len] == C[k][0] && N[i] == C[k][1]) ||
                        (ans[len] == C[k][1] && N[i] == C[k][0]))
                    {
                        for (int l = 0; l < cntD; l++)
                        {
                            if (ans[len] == D[k][0])
                                bD[k][0]--;
                            if (ans[len] == D[k][1])
                                bD[k][1]--;
                        }
                        ans[len] = C[k][2];
                        cont = true;
                        break;
                    }
                }
            }

            if (!cont)
            {
                for (int k = 0; k < cntD; k++)
                {
                    if (N[i] == D[k][0])
                    {
                        if (bD[k][1] > 0)
                        {
                            len = -1;
                            ClearBD();
                            cont = true;
                            break;
                        }
                        bD[k][0]++;
                    }
                    else if (N[i] == D[k][1])
                    {
                        if (bD[k][0] > 0)
                        {
                            len = -1;
                            ClearBD();
                            cont = true;
                            break;
                        }
                        bD[k][1]++;
                    }
                }
            }

            if (!cont)
            {
                ans[++len] = N[i];
            }
        }

        printf("Case #%ld: [", j + 1);
        for (int i = 0; i < len; i++)
        {
            printf("%c, ", ans[i]);
        }
        if (len > -1)
            printf("%c", ans[len]);
        printf("]\n");
        ClearBD();
    }
    return 0;
}
