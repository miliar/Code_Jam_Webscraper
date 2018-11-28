#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << '\n')

#define forz(p)     for(int i = 0; i < p; ++i)
#define foriz(i, p) for(int i = 0; i < p; ++i)
#define tr(x)       for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define read(n)     (scanf("%d", &(n)) == 1)

const int INF = 0x3f3f3f3f;
const double EPS = 1e-9;

inline int cmpD(double x, double y, double tol = EPS)
{
    return (x <= y + tol) ? (x + tol < y) ?  -1 : 0 : 1;
}

struct walkway
{
    int B;
    int E;
    int w;
    bool operator<(const walkway & other) const
    {
        return (B < other.B) || (B == other.B and E < other.E);
    }
};

struct pp
{
    int B, E;
    int s;
    bool operator<(const pp & other) const
    {
        return s < other.s;
    }
    pp(int B, int E, int s): B(B), E(E), s(s)
    {}
};

double go()
{
    int X, S, R, t, N;
    read(X); read(S); read(R); read(t); read(N);
    vector<walkway> ww(N);
    forz(N)
    {
        read(ww[i].B);
        read(ww[i].E);
        read(ww[i].w);
    }
    walkway end;
    end.B = X;
    end.E = X;
    end.w = 0;
    ww.push_back(end);
    sort(ww.begin(), ww.end());

    int csp = 0;
    int cp = 0;
    int cs = S;
    bool in = false;
    vector<pp> parts;
    forz(N+1)
    {
#define PRINTPART(i) PRINT("part [%d, %d] speed = %d\n", parts[i].B, parts[i].E, parts[i].s)
        cp = ww[i].B;
        if (csp != cp)
        {
            parts.push_back(pp(csp, cp, cs));
            //PRINTPART(parts.size()-1);
        }
        if (ww[i].B != ww[i].E)
        {
            parts.push_back(pp(ww[i].B, ww[i].E, ww[i].w+S));
            //PRINTPART(parts.size()-1);
        }
        csp = ww[i].E;
    }
    sort(parts.begin(), parts.end());
    //reverse(parts.begin(), parts.end());

    int run_diff = R - S;
    double run_time = t;
    double ttime = 0.0;
    forz(parts.size())
    {
        pp p = parts[i];
        PRINTPART(i);
        //PRINT("part [%d, %d] speed = %d\n", p.B, p.E, p.s);
        int length = p.E - p.B;
        double time_spent_running = min(length*1.0/(p.s+run_diff), run_time);
        run_time -= time_spent_running;
        double time_spend_walking = (length - time_spent_running*(p.s+run_diff))*1.0/p.s;
        ttime += time_spent_running + time_spend_walking;

    }
    return ttime;
}

int main()
{
    int T;
    read(T);
    forz(T)
    {
        printf("Case #%d: %.16lf\n", 1+i, go());
    }
    return 0;
}
