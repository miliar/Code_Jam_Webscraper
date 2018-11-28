/**********************************************************************
Author: Sherlock
Created Time:  2010/5/23 19:15:09
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

const int   maxint  =   0x7FFFFFFF;

long long         l, p, c;

void            init()
{
    cin >> l >> p >> c;
}

void            solve()
{
    int cnt = 1;
    while (l < p)
    {
        l *= c;
        cnt ++;
    }
    int ans = 0;
    while (cnt > 2)
    {
        cnt = (cnt / 2) + 1;
        ans ++;
    }
    printf("%d\n", ans);
}

int             main()
{
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        printf("Case #%d: ", i);
        init();
        solve();
    }
    return 0;
}

