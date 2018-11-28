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



int main(int argc, char *argv[])
{
    u64 caseNum;
    FILE *fp = fopen(INPUT_FILE_NAME, "r");
    fscanf(fp, "%lld\n", &caseNum);

    for (u32 j = 0; j < caseNum; j++)
    {
        u64 numNum;
        fscanf(fp, "%lld\n", &numNum);

        u32 min = ~0;
        u64 sum = 0;
        u32 q = 0;
        for (u32 i = 0; i < numNum; i++)
        {
            u32 tmp;
            fscanf(fp, "%ld ", &tmp);
            if (min > tmp)
                min = tmp;
            sum += tmp;
            q ^= tmp;
        }

        if (q)
            printf("Case #%ld: NO\n", j + 1);
        else
            printf("Case #%ld: %lld\n", j + 1, sum - min);
    }
    return 0;
}
