/*
    Title:
    Author: RudySnow
    Algorithm:
    Date:
    License:
    Quote: Night Gathers, and My Watch Begins, it shall Never End until My Death
*/

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int t[105];

int check(int n, int m)
{
    int i = n - m * 3;
    if(i >= -2) return 1;
    if(i >= -4)
    {
        if(m <= 1) return 0;
        return 2;
    }
    return 0;
}

void Solve()
{
    int test, cas, i, j, n, s, p, r;
    cas = 1;
    scanf("%d", &test);
    while(test--)
    {
        scanf("%d%d%d", &n, &s, &p);
        r = 0;
        for(i = 0; i < n; ++i)
        {
            scanf("%d", &t[i]);
        }
        for(i = 0; i < n; ++i)
        {
            j = check(t[i], p);
            if(j == 0) continue;
            if(j == 1) ++r;
            else
            {
                if(s > 0) --s, ++r;
            }
        }
        printf("Case #%d: %d\n", cas, r);
        ++cas;
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    Solve();
    return 0;
}
