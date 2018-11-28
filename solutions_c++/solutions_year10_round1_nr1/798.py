#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iterator>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cstddef>
#include <cmath>
#include <cctype>
#include <ctime>

using namespace std;

int main(int argc, char *argv[])
{
    int ncase;
    char buf[1024];
    fgets(buf, 1024, stdin);
    sscanf(buf, "%d", &ncase);
    for (int icase = 1; icase <= ncase; icase++)
    {
        int k, n;
        fgets(buf, 1024, stdin);
        sscanf(buf, "%d%d", &n, &k);
        char bd[100][100];
        for(int i = 0; i < n; i++)
        {
            fgets(bd[i], 100, stdin);
            int z = n - 1;
            for (int j = n - 1; j >= 0; j--)
            {
                if (bd[i][j] != '.')
                    bd[i][z--] = bd[i][j];
            }
            for (; z >= 0;  z--)
                bd[i][z] = '.';
        }
        /*
        printf("%d\n", k);
        for (int i = 0; i < n; i++)
            printf("%s", bd[i]);
            */

        int r = 0;
        int b = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                char c = bd[i][j];
                if (c == 'R' && r || c == 'B' && b)
                    continue;
                int can;
                can = 1;
                if (j+k <= n)
                {
                    for (int d = j; d < j+k; d++)
                    {
                        if (bd[i][d] != c)
                        {
                            can = 0;
                            break;
                        }
                    }
                }
                else
                    can = 0;
                if (can)
                    goto CAN;
                can = 1;
                if (i + k <= n)
                {
                    for (int d = i; d < i+k; d++)
                    {
                        if (bd[d][j] != c)
                        {
                            can = 0;
                            break;
                        }
                    }
                }
                else
                    can = 0;
                if (can)
                    goto CAN;
                can = 1;
                if (i+k<=n && j+k <= n)
                {
                    for (int z = 0; z < k; z++)
                    {
                        if (bd[i+z][j+z] != c)
                        {
                            can = 0;
                            break;
                        }
                    }
                }
                else
                    can = 0;
                if (can)
                    goto CAN;

                can = 1;
                if (i-k >= -1 && j+k <= n)
                {
                    for (int z = 0; z < k; z++)
                    {
                        if (bd[i-z][j+z] != c)
                        {
                            can = 0;
                            break;
                        }
                    }
                }
                else
                    can = 0;
                if (can)
                    goto CAN;

                continue;

CAN:
                if (c == 'R')
                    r = 1;
                if (c == 'B')
                    b = 1;
            }
        if (r && b)
            printf("Case #%d: Both\n", icase);
        else if (r)
            printf("Case #%d: Red\n", icase);
        else if (b)
            printf("Case #%d: Blue\n", icase);
        else
            printf("Case #%d: Neither\n", icase);
    }
    return 0;
}
