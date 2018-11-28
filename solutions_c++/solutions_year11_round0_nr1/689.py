#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int a[200];
int B[200];
int O[200];
char c[200][10];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases, n, i, step, ans, o, b, oi, bi, on, bn, u;
    scanf("%d", &cases);
    for(u = 1; u <= cases; u++)
    {
        scanf("%d", &n);
        oi = bi = on = bn = 0;
        for(i = 0; i < n; i++)
        {
            scanf("%s%d", c[i], &a[i]);
            if(strcmp(c[i], "O") == 0)
                O[on++] = a[i];
            else
                B[bn++] = a[i];
        }
        o = 1;
        b = 1;
        ans = 0;
        for(i = 0; i < n; i++)
        {
            if(strcmp(c[i], "O") == 0)
            {
                step = abs(a[i] - o) + 1;
                ans += step;
                o = a[i];
                if(step < abs(B[bi] - b))
                {
                    if(B[bi] > b)
                        b += step;
                    else
                        b -= step;
                }
                else
                    b = B[bi];
                oi++;
            }
            else
            {
                step = abs(a[i] - b) + 1;
                ans += step;
                b = a[i];
                if(step < abs(O[oi] - o))
                {
                    if(O[oi] > o)
                        o += step;
                    else
                        o -= step;
                }
                else
                    o = O[oi];
                bi++;
            }
        }
        printf("Case #%d: %d\n", u, ans);
    }
    return 0;
}
