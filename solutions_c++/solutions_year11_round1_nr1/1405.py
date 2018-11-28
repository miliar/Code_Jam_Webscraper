#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;

const double eps = 1e-6;

int main(void)
{
    freopen("D:/A-small-attempt2.in", "r", stdin);
    freopen("D:/Asmall.out", "w", stdout);
    int t, n, pd, pg;
    scanf("%d", &t);
    int ca = 0;
    while(t--)
    {
        scanf("%d %d %d", &n, &pd, &pg);
        int flag = 0;
        for(int i = 1; i <= n; ++i)
        {
            double now = i * (pd / 100.0);
        //    printf("%lf||",now);
            if(fabs(now - int(now)) <= eps)
            {
                flag = 1;
                break;
            }
        }
        printf("Case #%d: ", ++ca);
        if(pg == 0 && pd == 0)
        {
            printf("Possible\n");
            continue;
        }
        if(!flag || (pd != 100 && pg == 100) || (flag == 1 && pg == 0))
            printf("Broken\n");
        else
            printf("Possible\n");
    }
}