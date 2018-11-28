#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdio>
#include <cassert>
#include <utility>

using namespace std;

#define two(n) (1 << (n))
#define hold(mask, i) (((mask) & two(i)) != 0)
#define all(v) v.begin(), v.end()
#define forn(i, n) for (int i = 0; i < int(n); ++i)

struct pt
{
    double x, y;
};

vector<pt> a;
vector<pt> b;
vector<pt> c(3);

void read()
{
    a.resize(3);
    b.resize(3);

    forn(i, 3)
        cin >> a[i].x >> a[i].y;

    forn(i, 3)
        cin >> b[i].x >> b[i].y;
}

double scale;

bool matchT()
{
    vector<double> fa(3), fb(3);
    forn(i, 3)
        fa[i] = hypot(a[(i + 1) % 3].x - a[i].x, a[(i + 1) % 3].y - a[i].y);

    forn(i, 3)
        fb[i] = hypot(c[(i + 1) % 3].x - c[i].x, c[(i + 1) % 3].y - c[i].y);

    scale = -1;

    forn(i, 3)
        if (fa[i] > 0 && fb[i] > 0)
            scale = fa[i] / fb[i];

    if (scale < -0.5)
        return false;
    else
    {
        double result = 0.0;
        forn(i, 3)
            result += fabs(fa[i] - scale * fb[i]);
        return result < 1E-8;
    }
}

double f(double x, double y)
{
    vector<double> fa(3), fb(3);

    forn(i, 3)
        fa[i] = hypot(x - a[i].x, y - a[i].y);
    forn(i, 3)
        fb[i] = hypot(x - c[i].x, y - c[i].y);

    /*forn(i, 3)
        if (fa[i] > 0 && fb[i] > 0)
            scale = fa[i] / fb[i];
    */
    {
        double result = 0.0;

        forn(i, 3)
            result += fabs(fa[i] - scale * fb[i]) * 10;

        return result;
    }
}

double Y;

double f(double x)
{
    double lf = -1E5;
    double rg = +1E5;

    forn(tt, 100)
    {
        double lmid = lf + (rg - lf) / 3.0;
        double rmid = rg - (rg - lf) / 3.0;

        double lval = f(x, lmid);
        double rval = f(x, rmid);

        if (lval > rval)
            lf = lmid;
        else
            rg = rmid;
    }

    Y = (lf + rg) / 2.0;

    //cerr << f(x, (lf + rg) / 2.0) << endl;

    return f(x, (lf + rg) / 2.0);
}

bool solve2()
{
    double lf = -1E5;
    double rg = +1E5;

    forn(tt, 100)
    {
        double lmid = lf + (rg - lf) / 3.0;
        double rmid = rg - (rg - lf) / 3.0;

        double lval = f(lmid);
        double rval = f(rmid);

        if (lval > rval)
            lf = lmid;
        else
            rg = rmid;
    }

    double X = (lf + rg) / 2.0;

    double v = f(X);

    if (fabs(v) < 1E-7)
    {
        printf("%.10lf %.10lf\n", X, Y);
        return true;
    }

    return false;
}

void solve()
{
    vector<pair<double,double> > r;

    vector<int> p(3);
    forn(i, 3)
        p[i] = i;
    do
    {
        forn(i, 3)
            c[i] = b[p[i]];
        if (matchT())
        {
            if (solve2())
                return;
        }
    }
    while (next_permutation(all(p)));

    cout << "No Solution" << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);

    int minTest = 1;
    int maxTest = INT_MAX;

    int testCount;
    cin >> testCount;

    for (int test = 1; test <= testCount; test++)
    {
        read();

        if (minTest <= test && test <= maxTest)
        {
            cout << "Case #" << test << ": ";
            solve();
        }
    }

    return 0;
}
