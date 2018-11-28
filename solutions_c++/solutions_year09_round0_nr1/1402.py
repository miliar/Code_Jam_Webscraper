#include <stdio.h>

int a[1<<13][16];

int main()
{
    int n, m, k;

    scanf("%d%d%d", &k, &n, &m);

    for (int i=0; i<n+m; i++)
    {
        char s[512];
        scanf("%s", s);

        for (int j=0, x=0; x < k; x++)
        {
            int t = 1;
            if (s[j] == '(')
            {
                j++;
                t = 512;
            }

            for (; t; t--, j++)
            {
                if (s[j] == ')')
                {
                    j++;
                    break;
                }
                a[i][x] |= 1 << s[j]-'a';
            }
        }
    }

    for (int i=n; i<n+m; i++)
    {
        int ans = 0;
        for (int j=0, t; j<n; j++)
        {
            for (t=0; t<k; t++)
                if ((a[i][t] & a[j][t]) != a[j][t])
                    break;
            ans += t == k;
        }
        printf("Case #%d: %d\n", i+1-n, ans);
    }

    return 0;
}
