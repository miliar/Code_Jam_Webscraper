#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxN = 10240;

struct MM
{
    double b, e, s;
};

int nm;
MM ms[maxN];

double xl, sp, rp, tl;

bool cmp(const MM & a, const MM & b)
{
    return a.b < b.b;
}

bool cmp2(const MM & a, const MM & b)
{
    return a.s < b.s;
}

int main()
{
    //freopen("A2.in", "r", stdin);
    //freopen("A2.out", "w", stdout);
    int cas;

    scanf("%d", &cas);
    for(int cc = 0; cc < cas; cc++)
    {
        scanf("%lf %lf %lf %lf %d", &xl, &sp, &rp, &tl, &nm);
        for(int i = 0; i < nm; i++)
            scanf("%lf %lf %lf", &ms[i].b, &ms[i].e, &ms[i].s);

        sort(ms, ms + nm, cmp);

        int nn = nm;

        if(ms[0].b != 0)
        {
            ms[nm].b = 0;
            ms[nm].e = ms[0].b;
            ms[nm++].s = 0;
        }

        if(ms[nn - 1].e != xl)
        {
            ms[nm].b = ms[nn - 1].e;
            ms[nm].e = xl;
            ms[nm++].s = 0;
        }

        for(int i = 1; i < nn; i++)
            if(ms[i].b != ms[i - 1].e)
            {
                ms[nm].b = ms[i - 1].e;
                ms[nm].e = ms[i].b;
                ms[nm++].s = 0;
            }

        sort(ms, ms + nm, cmp2);

        double ans = 0;
        for(int i = 0; i < nm; i++)
        {
            double t = (ms[i].e - ms[i].b) / (rp + ms[i].s);
            if(tl >= t)
            {
                tl -= t;
                ans += t;
                xl -= (ms[i].e - ms[i].b);
            }
            else
            {
                double len = tl * (rp + ms[i].s);
                ans += tl + (ms[i].e - ms[i].b - len) / (sp + ms[i].s);
                tl = 0;
                xl -= (ms[i].e - ms[i].b);
            }
        }

        printf("Case #%d: %lf\n", cc + 1, ans);
    }
    return 0;
}
