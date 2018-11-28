#include <cstdio>
#include <cstring>
#include <cmath>

char        buf [200];
char        ans [200];

void init()
{
    scanf("%s", buf);
}

void solve()
{
    int cc = 0;
    int n = strlen(buf);
    for (int i = 0; i < n; i ++)
        if (buf[i] == '?') cc ++;

    int top = 1 << cc;
    strcpy(ans, buf);
    for (int stat = 0; stat < top; stat ++)
    {
        int p = 0;     
        long long v = 0;
        for (int i = 0; i < n; i ++)
            if (buf[i] == '?')
            {
                if (stat & (1<<(p++)))
                {
                    v += 1LL << (n-1-i);
                    ans[i] = '1';
                }
                else
                {
                    ans[i] = '0';
                }
            }
            else if (buf[i] == '1')
            {
                v += 1LL << (n-1-i);
            }

        long long x = long long(sqrt(v + 0.0));
        if (x * x == v)
        {
            printf("%s\n", ans); 
            return;
        }
    }
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t ++)
    {
        printf("Case #%d: ", t);

        init();
        solve();
    }

    return 0;
}