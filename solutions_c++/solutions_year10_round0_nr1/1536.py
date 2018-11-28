/**********************************************************************
Author: Sherlock
Created Time:  2010/5/8 10:35:12
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int   maxint  =   0x7FFFFFFF;

int         que[100];

void            solve()
{
    int n, k;
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i ++)
    {
        int f = 1 << (i + 1);
        if (k % f < f / 2)
            que[i] = 0;
        else
            que[i] = 1;
    }
    bool flag = true;
    for (int i = 0; i < n; i ++)
        if (que[i] == 0)
        {
            flag = false;
            break;
        }
    if (flag)
        printf("ON\n");
    else
        printf("OFF\n");
}

int             main()
{
//    freopen("A-small.in", "r", stdin);
//    freopen("A-small.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

