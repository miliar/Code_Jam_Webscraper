/**********************************************************************
Author: Sherlock
Created Time:  2009/9/26 23:29:50
File Name: A.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int   maxint  =   0x7FFFFFFF;

int         n;
int         que[100];
char        buf[100];

void            init()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
    {
        scanf("%s", buf);
        que[i] = 0;
        for (int j = n - 1; j >= 0; j --)
            if (buf[j] == '1')
            {
                que[i] = j;
                break;
            }
    }
}

void            solve()
{
    int total = 0;
    for (int i = 0; i < n; i ++)
    {
        for (int j = i; j < n; j ++)
            if (que[j] <= i)
            {
                for (int k = j; k > i; k --)
                {
                    swap(que[k], que[k - 1]);
                    total ++;
                }
                break;
            }
    }
    printf("%d\n", total);
}

int             main()
{
    freopen("A.out", "w", stdout);
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

