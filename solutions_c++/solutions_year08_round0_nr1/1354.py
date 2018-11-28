#include <cstdio>
#include <cstdlib>
#include <cstring>

int id[1002];
int ok[1002][102];

int solve(int s, int q)
{
    for (int i = 0; i < s; i++)
        ok[q][i] = 0;

    for (int i = q - 1; i >= 0; i--)
    {
        for (int j = 0; j < s; j++)
        {
            if (id[i] == j)
            {
                ok[i][j] = 9999;
                continue;
            }
            int min = 9999;
            for (int k = 0; k < s; k++)
            {
                int m;
                if (k == j)
                    m = ok[i + 1][k];
                else
                    m = ok[i + 1][k] + 1;
                if (m < min)
                    min = m;
            }
            ok[i][j] = min;
        }
    }

    int min = 9999;
    for (int i = 0; i < s; i++)
    {
        int m = ok[0][i];
        if (m < min)
            min = m;
    }
    return min;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        int s;
        scanf("%d", &s);
        char name[102][102] = {0};
        getchar();
        for (int j = 0; j < s; j++)
            gets(name[j]);

        int q;
        scanf("%d", &q);
        char query[1002][102] = {0};
        getchar();
        for (int j = 0; j < q; j++)
        {
            gets(query[j]);
            for (int k = 0; k < s; k++)
                if (!strcmp(query[j], name[k]))
                {
                    id[j] = k;
                    break;
                }
        }

        printf("Case #%d: %d\n", i + 1, solve(s, q));
    }
 
    return 0;
}