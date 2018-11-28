/**********************************************************************
Author: Jun
Created Time:  2009/9/3 15:55:04
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
const int maxn = 500 + 100;
const char t[19] = {'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm'};

char s[maxn];
int f[maxn][30];

void work()
{
    gets(s);
    int n = strlen(s), m = 19;
    memset(f, 0, sizeof(f));
    for (int i = 1; i <= n; i ++)
        for (int j = 1; j <= m; j ++)
        {
            if (s[i - 1] != t[j - 1])
                f[i][j] = f[i - 1][j] % 10000;
            else
            {
                if (j == 1 && f[i][j] == 0)
                    f[i][j] = f[i - 1][j] + 1;
                else f[i][j] = (f[i - 1][j] + f[i - 1][j - 1]) % 10000;
            }
        }
    printf("%04d\n", f[n][m]);
}

int main()
{
    freopen("c.out", "w", stdout);
    int case_num;
    scanf("%d", &case_num);
    gets(s);
    for (int i = 0;  i < case_num; i ++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}

