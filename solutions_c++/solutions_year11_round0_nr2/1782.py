#include <iostream>

using namespace std;

int     combine[30][30];
int     que[1100], ans[1100];
bool    re[30][30];

void    solve()
{
    int c;
    scanf("%d", &c);
    memset(combine, -1, sizeof(combine));
    for (int i = 0; i < c; i ++)
    {
        char s[10];
        scanf("%s", s);
        combine[s[0] - 'A'][s[1] - 'A'] = combine[s[1] - 'A'][s[0] - 'A'] = s[2]
        - 'A';
    }
    int r;
    scanf("%d", &r);
    memset(re, false, sizeof(re));
    for (int i = 0; i < r; i ++)
    {
        char s[10];
        scanf("%s", s);
        re[s[0] - 'A'][s[1] - 'A'] = true;
        re[s[1] - 'A'][s[0] - 'A'] = true;
    }
    int n;
    scanf("%d", &n);
    char s[110];
    scanf("%s", s);
    int len = strlen(s);
    for (int i = 0; i < len; i ++)
        que[i] = s[i] - 'A';

    int j = 0;
    ans[0] = que[0];
    for (int i = 1; i < len; i ++)
    {
        if (j < 0)
        {
            ans[++j] = que[i];
            continue;
        }
        if (combine[ans[j]][que[i]] != -1)
            ans[j] = combine[ans[j]][que[i]];
        else
        {
            bool flag = false;
            for (int k = 0; k <= j; k ++)
            {
                if (re[ans[k]][que[i]])
                {
                    flag = true;
                    j = -1;
                    break;
                }
            }
            if (! flag)
                ans[++j] = que[i];
        }
    }
    printf("[");
    for (int i = 0; i <= j; i ++)
    {
        printf("%c", 'A' + ans[i]);
        if (i < j)
            printf(", ");
    }
    printf("]\n");
}

int     main()
{
    freopen("B.in", "r", stdin);
    freopen("B.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        printf("Case #%d: ", i);
        solve();
    }
}
