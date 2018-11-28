using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>

struct duo
{
    double l, w;
    duo() {}
    duo(double _l, double _w) : l(_l), w(_w) {}
};

bool operator<(const duo& a, const duo& b)
{
    if (a.w==b.w)
    {
        return a.l>b.l;
    }
    return a.w<b.w;
}

duo ww[1003];

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T;
    double X, S, R, t, b, e, x;
    int N;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        cin>>X>>S>>R>>t>>N;
        x = X;
        for (int i=0; i<N; ++i)
        {
            cin>>b>>e>>ww[i].w;
            ww[i].l = e-b;
            ww[i].w += S;
            x -= ww[i].l;
        }
        ww[N].l = x;
        ww[N].w = S;
        ++N;
        sort(ww, ww+N);
        R -= S;
        double timing = 0;
        //printf("---------\n");
        for (int i=0; i<N; ++i)
        {
            //printf("=> %d %lf %lf\n", i, ww[i].l, ww[i].w);
            double _t = ww[i].l/ww[i].w;
            double __t = ww[i].l/(ww[i].w+R);
            if (t>=__t)
            {
                //printf("all run: %lf\n", __t);
                timing += __t;
                t -= __t;
            }
            else if (t>0)
            {
                ww[i].l -= t*(ww[i].w+R);
                _t = ww[i].l/ww[i].w;
                //printf("run + walk: %lf %lf\n", t, _t);
                timing += t;
                t = 0;
                timing += _t;
                t -= _t;
            }
            else
            {
                //printf("all walk: %lf\n", _t);
                timing += _t;
                t -= _t;
            }
        }
        printf("Case #%d: %.7lf\n", cas, timing);
    }
    return 0;
}

