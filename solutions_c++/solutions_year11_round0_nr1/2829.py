/*
 * Main.cpp
 *
 *  Created on: 2011/05/07
 *      Author: Philo
 */

#include "Main.h"

const char INPUT_FILE_NAME[]  = "D:/Temp/input.in";
const char OUTPUT_FILE_NAME[] = "D:/Temp/output.out";



int main(int argc, char *argv[])
{
    u64 caseNum;
    FILE *fp = fopen(INPUT_FILE_NAME, "r");
    FILE *fout = fopen(OUTPUT_FILE_NAME, "w");
    fscanf(fp, "%lld\n", &caseNum);

    for (u32 i = 0; i < caseNum; i++)
    {
        u64 numNum;
        fscanf(fp, "%lld\n", &numNum);
        int ans = 0;
        int total = 0;
        int p[2] = {1, 1};
        int now = -1;
        for (u32 j = 0; j < numNum; j++)
        {
            int pa;
            char a;
            fscanf(fp, "%c ", &a);
            fscanf(fp, "%ld ", &pa);
//            printf("%c, %d\n", a, pa);
            int t = (a == 'O') ? 0 : 1;
            if (t!=now)
            {
                ans += total;
                total = abs(p[t] - pa) - total;
                if (total <= 0)
                    total = 0;
                total++;
                now = t;
                p[now] = pa;
            }
            else
            {
                total += abs(p[now] - pa) + 1;
                p[now] = pa;
            }
        }
        ans += total;

        fprintf(fout, "Case #%ld: %ld\n", i + 1, ans);
        printf("Case #%ld: %d\n", i + 1, ans);
//        for (u32 j = 0; j < 2; j++)
//        {
//            for (u32 k = 0; k < cnt[j]; k++)
//            {
//                printf("%ld ", data[j][k]);
//            }
//            printf("\n");
//        }
    }
    return 0;
}
