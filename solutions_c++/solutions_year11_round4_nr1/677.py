#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
struct item
{
    int s,v;
    item(int _s, int _v){ s = _s; v = _v; }
    bool operator < (const item &r) const {
        if(v != r.v)return v < r.v;
        if(s != r.s)return s < r.s;
        return 0;
    }
};

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    vector<item> l;
    for(int ti = 1; ti <= tc; ti++)
    {
        int x,s,r,tx,n;
        scanf("%d%d%d%d%d", &x, &s, &r, &tx, &n);
        l.clear();
        for(int i = 0; i < n; i++)
        {
            int b, e, w;
            scanf("%d%d%d", &b, &e, &w);
            x -= e-b;
            l.push_back(item(e-b, s+w));

        }
        l.push_back(item(x, s));
        sort(l.begin(), l.end());
        double t2 = 0;
        double a = r-s;
        double t = tx;
        for(int i = 0; i <= n; i++)
        {
            double tt = ((double)l[i].s)/(l[i].v+a);
            if(tt < t)
            {
                t -= tt;
                t2 += tt;
            }
            else
            {
                double ss = (l[i].v+a)*t;
                t2 += t;
                t -= t;
                t2 += (l[i].s-ss)/(l[i].v);
            }
        }

    printf("Case #%d: %.9lf\n", ti, t2);
    }
    return 0;
}
