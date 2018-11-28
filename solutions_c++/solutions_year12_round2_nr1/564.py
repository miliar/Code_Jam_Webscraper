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
#define N 205
#define eps 1e-9
int s[N], n, tot;
double pro[N];
int check(int idx, double cp)
{
    int i;
    double tp = cp, np;
    for(i = 1; i <= n; i++)
    {
        if(i != idx)
        {
            np = (s[idx] - s[i]) * 1.0 / tot + cp;
            if(np > eps)
                tp += np;
        }
    }
    if(tp > 1.0 - eps)
        return 1;
    else
        return 0;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 1, i, j;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(i = 1, tot = 0; i <= n; i++)
        {
            scanf("%d", &s[i]);
            tot += s[i];
        }
        for(i = 1; i <= n; i++)
        {
            double l = 0.0, r = 1.0, mid;
            if(check(i, 0.0))
            {
                pro[i] = 0.0;
            }
            else
            {
                for(j = 1; j <= 100; j++)
                {
                    mid = (l + r) / 2.0;
                    if(check(i, mid))   r = mid;
                    else                l = mid;
                }
                pro[i] = r * 100.0;
            }
        }
        printf("Case #%d:", cas++);
        for(i = 1; i <= n; i++)
        {
            printf(" %.6f", pro[i]);
        }
        printf("\n");
    }
    return 0;
}
/*
1
4 25 25 25 25
*/
