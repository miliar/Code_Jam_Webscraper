/**********************************************************************
Author: Sherlock
Created Time:  2009-9-13 0:05:30
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int   maxint =   0x7FFFFFFF;

int         que[100];
char        buf[100];

void            print(int n)
{
    for (int i = 0; i < n; i ++)
        printf("%d", que[i]);
    printf("\n");
}

void            solve()
{
    int n = strlen(buf);
    for (int i = 0; i < n; i ++)
        que[i] = buf[i] - '0';
    for (int i = n - 2; i >= 0; i --)
    {
        int m = 10, k = -1;
        for (int j = i + 1; j < n; j ++)    
            if (que[j] > que[i] && que[j] < m)
            {
                m = que[j];
                k = j;
            }
        if (k != -1)
        {
            swap(que[i], que[k]);
            sort(que + i + 1, que + n);
            print(n);
            return ;
        }
    }
    n ++;
    que[n - 1] = 0;
    sort(que, que + n);
    for (int i = 0; i < n; i ++)
        if (que[i] > 0)
        {
            swap(que[0], que[i]);
            break;
        }
    print(n);
}

int             main()
{
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int cnt = 0;
    while (T > 0)
    {
        T --;
        scanf("%s", buf);
        printf("Case #%d: ", ++ cnt);
        solve();
    }
    return 0;
}

