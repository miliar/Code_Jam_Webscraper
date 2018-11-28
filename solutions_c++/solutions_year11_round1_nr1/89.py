// vim:set ts=8 sw=4 et smarttab:
// Round 1A 2011

#include <cstdio>
#include <cstring>
#include <cassert>

bool solve(long long n, long long pd, long long pg)
{
    if (pd < 100 && pg == 100)
        return false;
    if (pd > 0 && pg == 0)
        return false;
    if (n >= 100)
        return true;
    for (int d = 1; d <= n; ++d)
        for (int wd = 0; wd <= d; ++wd)
            if (wd * 100 == pd * d)
                return true;
    return false;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        long long n, pd, pg;
        scanf("%lld%lld%lld", &n, &pd, &pg);
        if (solve(n, pd, pg))
            printf("Case #%d: Possible\n", tc);
        else
            printf("Case #%d: Broken\n", tc);
    }
}
