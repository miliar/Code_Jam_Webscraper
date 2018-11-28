/**********************************************************************
Author: Sherlock
Created Time:  2009-9-3 15:23:54
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
const int   maxSize =   1000 + 10;
const char  P[]   =   {"welcome to code jam"};

int         f[maxSize][30];
char        s[maxSize];

void            solve()
{
    int n = strlen(s);
    memset(f, 0, sizeof(f));
    f[0][0] = 1;
    for (int i = 0; i <= n; i ++)
    {
        for (int j = 0; j <= 19; j ++)
            if (f[i][j] > 0)
            {
                if (j < 19 && s[i] == P[j])
                    f[i + 1][j + 1] = (f[i + 1][j + 1] + f[i][j]) % 10000;
                f[i + 1][j] = (f[i + 1][j] + f[i][j]) % 10000;
            }
    }
    printf("%04d\n", f[n][19]);
}

int             main()
{
    freopen("C_large.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    gets(s);
    while (T > 0)
    {
        T --;
        printf("Case #%d: ", ++ cnt);
        gets(s);
        solve();
    }
    return 0;
}

