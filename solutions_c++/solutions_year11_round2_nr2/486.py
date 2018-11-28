#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <set>
#include <stdio.h>
#include <map>
#include <vector>

using namespace std;

struct data
{
    int a, b;
}point[200+10];
int allpoint[200000000+10];

int main(void)
{
    freopen("D:/B-small-attempt4.in", "r", stdin);
    freopen("D:/Bsmall.out", "w", stdout);
    int t, c, d;
    scanf("%d", &t);
    int ca = 0;
    while(t--)
    {
        scanf("%d %d", &c, &d);
        for(int i = 0; i < c; ++i)
        {
            int a, b;
            scanf("%d %d", &a, &b);
            point[i].a = a; point[i].b = b;
        }
        double ans = 0;
        int cnt = 0;
        for(int i = 0 ; i < c; ++i)
        {
            int now = point[i].b;
            while(now--)
            {
                allpoint[cnt++] = point[i].a;
        //        if(a == -1000000)
        //        {
        //            a = point[i].a;
        //            continue;
        //        }
        //        b = point[i].a;
        ////        printf("%d %d>>", a, b);
        //        if((b - a) < d)
        //        {
        //            ans += ((d - (b - a)) / (d * 1.0));
        //        }
        //        a = b;
            }
        }
        double res = 0;
        for(int i = 1; i < cnt; ++i)
        {
         //   printf("%d||", allpoint[i]);
            /*if(allpoint[i] - allpoint[i - 1] < d)
            {*/
                res += ((d - (allpoint[i] - allpoint[i - 1]))/ (2 * 1.0));
                if(ans < res)
                {
                    ans = res;
                }
                if(res < 0)
                    res = 0;
        //        printf("%lf>>", res);
            /*}*/
            /*else
            {
                if(ans < res)
                {
                    if(allpoint[i] - allpoint[i - 1])
                    ans = res;
                    res = 0;
                }
            }*/
        }
        if(ans < res)
        {
            ans = res;
        }
        printf("Case #%d: %.6lf\n", ++ca, ans);
    }
    return 0;
}