#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int N = 501;

char pat[20], a[N];
int f[20][N];

int main()
{
    int ncase, i, j, k, n, m, testcase;
    
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    strcpy(pat, "welcome to code jam");
    
    scanf("%d\n", &ncase);
    for (testcase = 1; testcase <= ncase; testcase++)
    {
        gets(a);
        n = strlen(pat);
        m = strlen(a);
        memset(f, 0, sizeof(f));
        for (i = 0; i < m; i++)
        if (a[i] == pat[0])
            f[0][i] = 1;
        for (i = 1; i < n; i++)
        {
            for (j = 1; j < m; j++)
            if (a[j] == pat[i])
            {
                for (k = 0; k < j; k++)
                f[i][j] = (f[i][j] + f[i-1][k])%10000;
//                printf("f[%d][%d]=%d\n", i, j, f[i][j]);
            }
        }
        int ans = 0;
        for (i = 0; i < m; i++)
            ans = (ans + f[n-1][i])%10000;
        printf("Case #%d: ", testcase);
        if (ans < 10)
            printf("000%d\n", ans);
        else if (ans < 100)
            printf("00%d\n", ans);
        else if (ans < 1000)
            printf("0%d\n", ans);
        else printf("%d\n", ans);
    }
    return 0;
}
