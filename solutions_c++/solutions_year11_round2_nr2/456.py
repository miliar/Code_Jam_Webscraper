#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#define MAXN (1 << 20)
#define EPS (1e-10)
#define x first
#define y second
using namespace std;
#warning use cin/cout or %I64d for long integers

int n, cnt;
double dist;
double a[MAXN];
/*
inline double calc(double from)
{
    double step = dist;
    double cur = from;
    double sol = 0., tmp;
    for (int i=0; i < cnt; ++i)
    {
        tmp = fabs(a[i] - cur);
        if (tmp > sol+EPS)
            sol = tmp;
        //cout << "   -> sol is " << sol << endl;
        cur += step;
    }
    //cout << "   returning " << sol << endl;
    return sol;
}

inline void solve()
{
    double l = -1e12, r = 1e12, mid1, mid2;
    double valLeft, valRight;

    for (int it=0; it < 500; ++it)
    {
        mid1 = l + (r-l)/3.;
        mid2 = r - (r-l)/3.;
        valLeft = calc(mid1);
        valRight = calc(mid2);

        //cout << mid1 << " -> " << valLeft << endl;
        //cout << mid2 << " -> " << valRight << endl;

        if (valLeft+EPS < valRight)
            r = mid2;
        else l = mid1;
    }

    cout << setprecision(10) << fixed << calc((l+r)/2.) << endl;
    cout << setprecision(10) << fixed << (l+r)/2. << endl;
}*/

inline int can(double x)
{
    double cur;
    double step = dist;
    double last=a[0]-x;

    for (int i=1; i < cnt; ++i)
    {
        cur = a[i]-x;
        //cout << last << endl;
        if (cur-last+EPS > dist)
        {
            last = cur;
        }
        else
        {
            cur = last+dist;
            if (fabs(cur-a[i])+EPS > x)
                return 0;
            last = cur;
        }
    }

    return 1;
}

inline void solve()
{
    double l = 0., r = 1e15, mid;

    for (int it=0; it < 100; ++it)
    {
        mid = (l+r) / 2.;
        //cout << l << ' ' << mid << ' ' << r << endl;
        //cout << can(mid) << endl;
        if (can(mid)) r = mid;
        else l = mid;
    }

    cout << setprecision(10) << fixed << (l+r)/2. << endl;
}

inline void read()
{
    cin >> n >> dist;
    for (int i=0; i < n; ++i)
    {
        double pos;
        int amount;
        cin >> pos >> amount;
        //cout << amount << endl;
        for (int j=0; j < amount; ++j)
            a[cnt ++] = pos;
    }
}

inline void clear()
{
    cnt = 0;
}
/*
inline void stupidSolve()
{
    double ans = 1e15;
    for (double pos = -101000.0; pos < 101000.0; pos += 0.5)
    {
        double cur = calc(pos);
        if (ans > cur + EPS)
            ans = cur;
    }

    cout << setprecision(10) << fixed << ans << endl;;
}*/

int main()
{
    int brt, testNo = 0;
    cin >> brt;

    while (brt--)
    {
        clear();
        read();
        cout << "Case #" << ++testNo << ": ";
        //cout << can(2.5) << endl;
        solve();
    }
    return 0;
}
