#include <iostream>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

int l, d, n;
char c[6000][20];
char s[1000];

int i, j;
int ans = 0;

bool used[6000];

void solve(char s[1000], int qq)
{
    int i, j, q;
    for (i = 1; i <= d; i ++) used[i] = false;

    char buf[30];

    int n = strlen(s);
    int m = -1, k = -1;

    bool p = false;

    for (i = 0; i < n; i ++)
        if (s[i] != '(' && s[i] != ')')
        {
            if (p) k ++, buf[k] = s[i]; else 
            {
                m ++;
                if (m == 0)
                {
                    for (j = 1; j <= d; j ++) if (c[j][0] == s[i]) used[j] = true;
                } else
                {
                    for (j = 1; j <= d; j ++) if (c[j][m] == s[i] && used[j]) used[j] = true; else used[j] = false;
                }
            }
        } else
        if (s[i] == '(') p = true, k = -1; else
        if (s[i] == ')')
        {
            m ++;
            p = false;
            if (m == 0)
            {
                for (j = 1; j <= d; j ++)
                    for (q = 0; q <= k; q ++) if (c[j][0] == buf[q])
                    {
                        used[j] = true;
                        break;
                    }
            } else
            {
                bool get;
                for (j = 1; j <= d; j ++)
                {
                    get = false;
                    for (q = 0; q <= k; q ++) if (c[j][m] == buf[q] && used[j])
                    {
                        used[j] = true;
                        get = true;
                        break;
                    }

                    if (!get) used[j] = false;
                }
            }
        }

    ans = 0;
    for (i = 1; i <= d; i ++) if (used[i]) ans ++;
    printf("Case #%d: %d\n", qq, ans);
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d%d%d\n", &l, &d, &n);

    for (i = 1; i <= d; i ++)
        scanf("%s\n", c[i]);

    for (i = 1; i <= n; i ++)
    {
        for (j = 0; j < 1000; j ++) s[j] = 0;
        scanf("%s\n", s);
        solve(s, i);
    }
    return 0;
}