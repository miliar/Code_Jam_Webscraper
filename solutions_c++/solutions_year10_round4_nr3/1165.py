/**********************************************************************
Author: Jun
Created Time:  2010/6/5 23:00:47
File Name: 
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxn = 100 + 10;

bool g[maxn][maxn];
int n, m, x1, y1, x2, y2, r; 

void work()
{
    scanf("%d", &r);
    memset(g, 0, sizeof(g));
    int n = 0, m = 0;
    for (int k = 0; k < r; k ++)
    {
        scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
        n = max(n, x1);
        n = max(n, x2);
        m = max(m, y1);
        m = max(m, y2);
        y1 --, x1 --, y2 --, x2 --;
        for (int i = x1; i <= x2; i ++)
            for (int j = y1; j <= y2; j ++)
                g[i][j] = true;
    }
    int ans = 0;
    while (1)
    {
        bool ok = true;
        ans ++;
        for (int i = n - 1; i >= 0; i --)
            for (int j = m - 1; j >= 0; j --)
                if (g[i][j])
                {
                    ok = false;
                    if (!((i > 0 && g[i - 1][j]) || (j > 0 && g[i][j - 1])))
                        g[i][j] = false;   
                }        
                else {
                    if ((i > 0 && g[i - 1][j]) && (j > 0 && g[i][j - 1]))
                        g[i][j] = true;
                }
        if (ok) break;    
    }
    printf("%d\n", ans - 1);
}

int main()
{
    freopen("c.small.out", "w", stdout);
    int case_num;
    scanf("%d", &case_num);
    for (int i = 0; i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}

