#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

const int INF = 1000000000;
int kases, kase, n;
double x1_, y1_, x2_, y2_, x3_, y3_, r1, r2, r3, t, res;

double sqr(double x) { return x * x; }

double dist(double x1_, double y1_, double x2_, double y2_)
{
    return sqrt(sqr(x1_ - x2_) + sqr(y1_ - y2_));
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    cin >> kases;
    for (kase = 1; kase <= kases; ++kase)
    {
        cin >> n;
        cout << setiosflags(ios::fixed) << setprecision(10);
        cout << "Case #" << kase << ": ";
        if (n == 1)
        {
            cin >> x1_ >> y1_ >> r1;
            cout << r1;
        }
        else if (n == 2)
        {
            cin >> x1_ >> y1_ >> r1;
            cin >> x2_ >> y2_ >> r2;
            cout << max(r1, r2);
        }
        else
        {
            cin >> x1_ >> y1_ >> r1;
            cin >> x2_ >> y2_ >> r2;
            cin >> x3_ >> y3_ >> r3;
            res = INF;
            t = max((dist(x1_, y1_, x2_, y2_) + r1 + r2) / 2, r3);
            if (t < res) res = t;
            t = max((dist(x1_, y1_, x3_, y3_) + r1 + r3) / 2, r2);
            if (t < res) res = t;
            t = max((dist(x2_, y2_, x3_, y3_) + r2 + r3) / 2, r1);
            if (t < res) res = t;
            cout << res;
        }
        cout << endl;
    }

    return 0;
}
