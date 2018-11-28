/**********************************************************************
Author: Sherlock
Created Time:  2009-9-12 8:50:03
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

using namespace std;

const int   maxint =   0x7FFFFFFF;

int         b[11];
char        buf[1000];

set <int>   hash;

void            solve()
{
    for (int j = 2; ; j ++)
    {
        bool find = true;
        for (int i = 2; i <= 10; i ++)
        {
            if (b[i] == 0)
                continue;
            hash.clear();
            int x = j;
            hash.insert(x);
            bool flag = false;
            while (true)
            {
                int t = x;
                x = 0;
                while (t > 0)
                {
                    x += (t % i) * (t % i);
                    t /= i;
                }
                if (x == 1)
                {
                    flag = true;
                    break;
                }
                if (hash.count(x) != 0)
                    break;
                hash.insert(x);
            }
            if (! flag)
            {
                find = false;
                break;
            }
        }
        if (find)
        {
            printf("%d\n", j);
            break;
        }
    }
}

int             main()
{
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    gets(buf);
    int cnt = 0;
    while (T > 0)
    {
        T --;
        printf("Case #%d: ", ++ cnt);
        gets(buf);
        memset(b, 0, sizeof(b));
        int len = strlen(buf);
        int i = 0;
        while (i < len)
        {
            while (i < len && buf[i] == ' ')
                i ++;
            if (i >= len)
                break;
            int x = 0;
            while (i < len && buf[i] >= '0' && buf[i] <= '9')
            {
                x = x * 10 + buf[i] - '0';
                i ++;
            }
            b[x] = 1;
        }
        solve();
    }
    return 0;
}

