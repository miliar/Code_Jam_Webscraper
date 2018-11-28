#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <numeric>

using namespace std;

typedef signed long long i64;  
typedef unsigned long long u64;
typedef long double real;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;

#define forr(i,n0,n1) for(int i=(n0); i<(n1); i++)
#define forn(i,n) for(int i=0; i<(n); i++)
#define fors(i,s) forn(i, (int)s.length())
#define forv(i,v) forn(i, (int)v.size())
#define fore(t, it, obj) for (t :: iterator it = obj.begin(); it != obj.end(); it++)

#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(i)) != 0)

#define pb push_back
#define all(v) v.begin(), v.end()
#define mp make_pair

int n;
vector<double> x, y, z, p;

const double INF = 10E10;
const int ITER = 100;

double t[10000][4];

bool exist(double c, double za)
{
    forn(i, n)
    {
        double rg = c * p[i];

        rg -= fabsl(z[i] - za);

        if (rg < 0)
            return false;

        t[i][0] = x[i] - y[i] - rg;
        t[i][1] = x[i] + y[i] - rg;

        t[i][2] = x[i] - y[i] + rg;
        t[i][3] = x[i] + y[i] + rg;
    }

    double minx = -INF;
    double maxx = +INF;
    double miny = -INF;
    double maxy = +INF;

    forn(i, n)
    {
        minx = max(minx, t[i][0]);
        miny = max(miny, t[i][1]);
        maxx = min(maxx, t[i][2]);
        maxy = min(maxy, t[i][3]);
    }

    return minx <= maxx && miny <= maxy;
}

double f(double z)
{
    double lf = 0;
    double rg = INF;

    forn(tt, ITER)
    {
        double mid = (lf + rg) / 2;

        if (lf == rg || lf == mid || rg == mid)
            break;
            
        bool e = exist(mid, z);

        if (e)
            rg = mid;
        else
            lf = mid;
    }

    return (lf + rg) / 2.0;
}

double solve()
{
    double lz = -INF;
    double rz = +INF;

    forn(tt, ITER)
    {
        double lmid = lz + (rz - lz) / 3.0;
        double rmid = rz - (rz - lz) / 3.0;

        double lval = f(lmid);
        double rval = f(rmid);

        if (lval > rval)
            lz = lmid;
        else
            rz = rmid;
    }

    return f((lz + rz) / 2.0);
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;

    cin >> testCount;

    forn(ta, testCount)
    {
        cin >> n;

        //n = 1000;

        x = vector<double>(n);
        y = vector<double>(n);
        z = vector<double>(n);
        p = vector<double>(n);
        forn(i, n)
            cin >> x[i] >> y[i] >> z[i] >> p[i];

        /*
        forn(i, n)
        {
            x[i] = rand();
            y[i] = rand();
            z[i] = rand();
            p[i] = rand();
            //p[i] = 1;
        }
        */

        double pa = solve();

        cout << "Case #" << ta + 1 << ": ";

        printf("%.10lf", pa);

        cout << endl;
    }

    return 0;
}
