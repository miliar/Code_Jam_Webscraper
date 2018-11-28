#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;
 
#define DEBUG(x) //x
#define REP(i,a) for(int i=0;i<int(a);i++)
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define VI vector<int>
#define size(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define MK(x, y) make_pair(x, y)
#define PB push_back
 
#define eps 1e-7

typedef pair<int, int> pii;

int main()
{
    int T; scanf("%d", &T);

    FOR(t, 1, T+1)
    {
        int n;
        double x, ti, s, r;
        scanf("%lf %lf %lf %lf %d\n", &x, &s, &r, &ti, &n);
        r -= s;
        if (r == 0)
            ti = 0;
        double lastpos = 0;
        vector< pair <double, double> > v;
        REP(i, n)
        {
            double b, e, w;
            scanf("%lf %lf %lf\n", &b, &e, &w);
            if (b > lastpos)
                v.push_back(MK(s, b-lastpos));
            v.push_back(MK(s + w, e - b));
            lastpos = e;
        }

        if (lastpos < x)
            v.push_back(MK(s, x - lastpos));

        double res = 0;
        sort(all(v));
        REP(i, size(v))
        {
            double tt;
            if (ti > eps)
            {
                double run = v[i].second / (v[i].first + r);
                if (run > ti)
                {
                    double distRun = (v[i].first + r) * ti;
                    double remain = (v[i].second - distRun) / (v[i].first);
                    //cout << "Parte : " << v[i].first - distRun << " ( " << distRun << " ) ___" << ti << "+" << remain << endl;
                    res += ti;
                    res += remain;
                    ti = 0;
                    tt = ti + remain;
                }
                else
                {
                    ti -= run;
                    res += run;
                    tt = run;
                }
            }
            else
            {
                double remain = v[i].second / (v[i].first);
                res += remain;
                tt = remain;
            }
//            cout << " dist:" << v[i].first << " s:" << v[i].second << " "<<tt << " -> " << res << endl;
        }
        printf("Case #%d: %.10lf\n", t, res);

    }
    return 0;
}

