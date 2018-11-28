#include <iostream>
#include <algorithm>
using namespace std;

int x, s, r, n;
double runTime;

struct Seg
{
    int b, e, w;
}segs[1000];

struct Less1
{
    bool operator()(const Seg&a, const Seg&b)
    {
        return a.b < b.b;
    }
};

struct Less2
{
    bool operator()(const Seg& a, const Seg &b)
    {
        return a.w < b.w;
    }
};

void createSegs()
{
    sort(segs, segs + n, Less1());
    int start = 0;
    int i = 0;
    int j = n;
    while (i < n)
    {
        if (start < segs[i].b)
        {
            segs[j].b = start; segs[j].e = segs[i].b;
            segs[j].w = s; ++j;            
        }
        start = segs[i++].e;
    }
    if (start < x)
    {
        segs[j].b = start; segs[j].e = x; segs[j].w = s;
        ++j;
    }

    n = j;
    sort (segs, segs + n, Less2());
}

int main()
{
    freopen("data.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, t;

    scanf("%d", &T);
    for (t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        scanf("%d %d %d %lf %d", &x, &s, &r, &runTime, &n);
        for (int i = 0;i<n; ++i)
        {
            scanf("%d %d %d", &segs[i].b, &segs[i].e, &segs[i].w);
            segs[i].w += s;
        }
        r -= s;
        createSegs();
        double time = 0;
        for (int i = 0; i < n; ++i)
        {
            double tm = (segs[i].e - segs[i].b) / (double)(segs[i].w + r);
            if (runTime >= tm)
            {
                runTime -= tm;
                time += tm;
            } else
            {
                double remain_dis = (double) (segs[i].e - segs[i].b) - runTime * (segs[i].w + r);
                time += remain_dis / segs[i].w + runTime;
                runTime = 0;
            }
        }
        printf("%.8lf\n", time);
    }
    return 0;
}