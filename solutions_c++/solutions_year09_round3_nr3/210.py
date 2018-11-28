#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int N = 128;
const int MAX = 1000000000;

int a[N], m, n, f[N][N], ncase, testcase;

int main()
{
    int i, j, k, l, s;
    
    freopen("C-small.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    
    scanf("%d", &ncase);
    for (testcase = 1; testcase <= ncase; testcase++)
    {
        scanf("%d%d", &m, &n);
        for (i = 1; i <= n; i++)
            scanf("%d", a+i);
        a[0] = 0;
        a[++n] = m + 1;
        memset(f, 0x7f, sizeof(f));
        for (i = 0; i < n - 1; i++)
            f[i][i + 2] = (a[i + 2] - a[i] -2);
        for (l = 3; l <= n; l++)
            for (i = 0; i + l <= n; i++)
            {
                j = i + l;
                for (k = i + 1; k < j; k++)
                {
                    s = a[j] - a[i] - 2;
                    if (k - i > 1)
                        s += f[i][k];
                    if (j - k > 1)
                        s += f[k][j];
                    if (s < f[i][j])
                        f[i][j] = s;
                }
//                printf("f[%d][%d] = %d\n", i, j, f[i][j]);
            }
        printf("Case #%d: %d\n", testcase, f[0][n]);
    }
    return 0;
}
