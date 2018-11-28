#include <iostream>

using namespace std;

void solve(int test)
{
    int r, k, n;
    int g[2000], fs[2000];
    long long res[2000];

    scanf("%d%d%d", &r, &k, &n);
    for (int i = 0; i < n; i ++)
        scanf("%d", &g[i]), fs[i] = -1;
    for (int i = 0; i <= 1500; i ++)
        res[i] = 0;

    int s = 0;
    int start = -1, period = -1;
    for (int i = 1; i <= r; i ++)
    {
        int cur = 0, b = s;
        for (int j = s; j < s + n; j ++)
            if (cur + g[j % n] <= k) cur += g[j % n]; else 
            {
                if (cur != 0) b = j;
                break;
            }

        res[i] = res[i - 1] + (long long)(cur);
        s = b % n;
        if (fs[s] != -1)
        {
            start = fs[s], period = i - fs[s];
            break;
        } else fs[s] = i;
    }

    long long ans = 0;
    if (start == -1)
    {
        ans = res[r];
    } else
    {
        ans += res[start];
        int moves = r - start;
        int mx = moves / period, lt = moves % period;
        ans += (long long)(mx) * (res[start + period] - res[start]);
        ans += (res[start + lt] - res[start]);
    }

    printf("Case #%d: %lld\n", test, ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int test;
    scanf("%d", &test);
    for (int i = 1; i <= test; i ++)
        solve(i);
    return 0;
}