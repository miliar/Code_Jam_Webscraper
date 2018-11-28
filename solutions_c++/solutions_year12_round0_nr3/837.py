#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3fffffff
#define LL long long

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int ti, cas = 1, s, t;
    int cnt, i, j, tmp;
    long long res;
    scanf("%d", &ti);
    while(ti--)
    {
        res = 0;
        scanf("%d%d", &s, &t);
        for(i = 1, tmp = 1; i <= 7 && tmp <= t; i++)
        {
            tmp *= 10;
        }
        cnt = i - 1;
        tmp /= 10;
        for(i = s; i < t; i++)
        {
            int cur = cnt;
            int next = i;
            while(cur--)
            {
                next = (next % 10) * tmp + (next / 10);
                if(next > i && next <= t)
                    res++;
                if(next == i)   break;
            }
        }
        printf("Case #%d: %I64d\n", cas++, res);
    }
    return 0;
}
