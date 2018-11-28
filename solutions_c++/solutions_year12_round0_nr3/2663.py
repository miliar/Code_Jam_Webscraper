#include <cstdio>
int test, n, m, d[15], a[15], cnt, x, y;
int b[2000005], p;
int main()
{
    scanf("%d", &test);
    int ca = 0;
    while (test--)
    {
        printf("Case #%d: ", ++ca);
        scanf("%d%d", &n, &m);
        cnt = 0;
        for (int i = n; i <= m; i++)
        {
            ++p;
            x = i;
            d[0] = 0;
            while (x)
            {
                d[++d[0]] = x % 10;
                x =(int) x / 10;
            }
            for (int j = 1; j < d[0]; j++)
            {
                y = 0;
                for (int k = d[0]; k; k--) y = y * 10 + d[(k - j - 1 + d[0]) % d[0] + 1];
                if (y > i && y <= m && b[y] != p)
                {
                    ++cnt;
                    b[y] = p;
                }
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}