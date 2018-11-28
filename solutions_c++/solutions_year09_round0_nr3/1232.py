#include <iostream>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

char s[1000];

char *tmp = "welcome to code jam";

int n, i, j, k, m;
int d[1000][30];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d\n", &n);
    for (i = 1; i <= n; i ++)
    {
        for (j = 0; j < 1000; j ++) s[j] = 0;
        gets(s);

        m = strlen(s);

        for (j = 0; j < m; j ++) d[j][0] = 1;

        for (j = 0; j < m; j ++)
        {
            for (k = 1; k <= 19; k ++)
                d[j + 1][k] = d[j][k];
            for (k = 1; k <= 19; k ++)
                if (s[j] == tmp[k - 1]) d[j + 1][k] += d[j][k - 1], d[j + 1][k] %= 10000;
        }

        if (d[m][19] < 10) printf("Case #%d: 000%d\n", i, d[m][19]); else
            if (d[m][19] < 100) printf("Case #%d: 00%d\n", i, d[m][19]); else
                if (d[m][19] < 1000) printf("Case #%d: 0%d\n", i, d[m][19]); else
                    printf("Case #%d: %d\n", i, d[m][19]);
    }
    return 0;
}