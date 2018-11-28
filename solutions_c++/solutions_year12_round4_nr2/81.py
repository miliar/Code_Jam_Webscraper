#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int maxn = 1000 + 5;

int n;
double x[maxn], y[maxn];
pair<int, int> r[maxn];

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);
    
    cout << fixed;
    cout.precision(7);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);

        int n, W, L;
        cin >> n >> W >> L;
        for (int i = 1; i <= n; ++i) {
            cin >> r[i].first;
            r[i].second = i;
            x[i] = -123456;
            y[i] = -123456;
        }
        sort(r + 1, r + n + 1);
        for (int i = n; i; --i) {
            double lef = 0, rig = L;
            while (lef + 1e-9 < rig) {
                double mid = (lef + rig) / 2;
                vector< pair<double, double> > p;
                for (int j = i + 1; j <= n; ++j) {
                    double _x = x[r[j].second], _y = y[r[j].second], _r = r[j].first;
                    if (abs(_y - mid) <= _r + r[i].first) {
                        double t = sqrt((_r + r[i].first) * (_r + r[i].first) - (_y - mid) * (_y - mid)) + 1e-3;
                        p.push_back(make_pair(_x - t, _x + t));
                    }
                }
                sort(p.begin(), p.end());
                bool ok = false;
                double last = 0;
                for (int j = 0; j < p.size(); ++j)
                    if (p[j].first > last) {
                        ok = true;
                        x[r[i].second] = last;
                        y[r[i].second] = mid;
                        break;
                    }else 
                    if (p[j].second > last) {
                        last = p[j].second;
                        if (last > W)
                            break;
                    }
                if (last <= W) {
                    ok = true;
                    x[r[i].second] = last;
                    y[r[i].second] = mid;
                }
                if (ok)
                    rig = mid;
                else
                    lef = mid;
            }
        }
        for (int i = 1; i <= n; ++i)
            cout << x[i] << " " << y[i] << " ";
        
        printf("\n");
    }
    
    return 0;
}
