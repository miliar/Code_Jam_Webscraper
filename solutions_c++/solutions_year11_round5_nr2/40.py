#include <cstdio>
#include <cstring>

int     n;

int     mx;
int     cnt [10000 + 100];
int     tmp [10000 + 100];

void init()
{
    scanf("%d", &n);
    memset(cnt, 0, sizeof(cnt));
    int x;
    mx = 0;
    for (int i = 0; i < n; i ++)
    {
        scanf("%d", &x);
        cnt[x] ++;
        if (x > mx) mx = x;
    }
}

void solve()
{
    int ans = n;

    for (int i = mx; i >= 1; i --)
    {
        while (cnt[i])
        {
            int j;
            for (j = i; ; j --)
                if (cnt[j] > cnt[j - 1]) break;
            if (i - j + 1 < ans)
                ans = i - j + 1;
            for (; j <= i; j ++)
                cnt[j] --;
        }
    }
    printf("%d\n", ans);
}

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

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