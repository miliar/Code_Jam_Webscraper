#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int n1, n2, m;
double w;

struct point {
    long double x, y;
    void read()
    {
        cin >> x >> y;
    }
} p[105], q[105];

long double area(double w)
{
    double ret = 0;
    for (int i = 2; i <= n1; ++i) {
        double x1 = p[i].x, y1 = p[i].y, x2 = p[i - 1].x, y2 = p[i - 1].y;
        bool ok = false;
        if (x1 >= w) {
            y1 = y2 + (y1 - y2) * (w - x2) / (x1 - x2);
            x1 = w;
            ok = true;
        }
        ret -= (y1 + y2) * (x1 - x2);
        if (ok) break;
    }
    for (int i = 2; i <= n2; ++i) {
        double x1 = q[i].x, y1 = q[i].y, x2 = q[i - 1].x, y2 = q[i - 1].y;
        bool ok = false;
        if (x1 >= w) {
            y1 = y2 + (y1 - y2) * (w - x2) / (x1 - x2);
            x1 = w;
            ok = true;
        }
        ret += (y1 + y2) * (x1 - x2);
        if (ok) break;
    }
    return ret;
}

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    
    cout << fixed;
    cout.precision(7);
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        cin >> w >> n1 >> n2 >> m;
        for (int i = 1; i <= n1; ++i)
            p[i].read();
        for (int i = 1; i <= n2; ++i)
            q[i].read();
        long double s = area(w);
        cout << "Case #" << t2 << ":" << endl;
        for (int i = 1; i < m; ++i) {
            long double l = 0, r = w;
            while (l + 1e-7 < r) {
                long double mid = (l + r) / 2;
                if (area(mid) < s / m * i) l = mid;
                else r = mid;
            }
            cout << (l + r) / 2 << endl;
        }
    }
    
    return 0;
}
