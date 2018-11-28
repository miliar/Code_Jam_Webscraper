// vim:set ts=8 sw=4 et smarttab:
// Round 2 2011

#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
#include <utility>

typedef std::pair<int, int> pi;
typedef std::pair<int, pi> ppi;

struct Mw
{
    int b, e, w;
    bool operator< (const Mw &rhs) const
    {
        return b < rhs.b;
    }
};

int x, s, r, t, n;
Mw mw[1000];

double solve()
{
    std::sort(mw, mw + n);
    int cur = 0;
    std::vector<ppi> interval;
    for (int i = 0; i < n; ++i)
    {
        if (mw[i].b > cur)
            interval.push_back(ppi(s, pi(cur, mw[i].b)));
        interval.push_back(ppi(s + mw[i].w, pi(mw[i].b, mw[i].e)));
        cur = mw[i].e;
    }
    if (cur < x)
        interval.push_back(ppi(s, pi(cur, x)));
    std::sort(interval.begin(), interval.end());
    double ret = 0;
    double t = ::t;
    for (std::vector<ppi>::const_iterator it = interval.begin(); it != interval.end(); ++it)
    {
        double dist = it->second.second - it->second.first;
        double speed;
        if (it->first == s)
            speed = r;
        else
            speed = r + it->first - s;
        double time = dist / speed;
        if (time >= t)
        {
            ret += t;
            ret += (dist - t * speed) / it->first;
            t = 0;
        }
        else
        {
            ret += time;
            t -= time;
        }
    }
    return ret;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
        for (int i = 0; i < n; ++i)
            scanf("%d%d%d", &mw[i].b, &mw[i].e, &mw[i].w);
        double ans = solve();
        printf("Case #%d: %.6lf\n", tc, ans);
    }
}
