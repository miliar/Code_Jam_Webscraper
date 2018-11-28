// headers
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std; // program namespace

int main(int argc, char *argv[]) // main function
{ 
    int a, cnt, i, j, n, _t;
    double aa, bb, cc, d, dd, spd, tt, x1, x2, xx, yy;
    vector <double> a1, t, x;
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    cin >> _t;
    for (cnt = 1; cnt <= _t; cnt++)
    {
        cin >> d; cin >> n; cin >> a;
        a1.resize(a); t.resize(n); x.resize(n);
        for (i = 0; i < n; i++)
        {
            cin >> t[i]; cin >> x[i];
        }
        for (i = 0; i < a; i++) cin >> a1[i];
        printf("Case #%d:\n", cnt);
        for (i = 0; i < a; i++)
        {
            if (n == 1)
            {
                tt = sqrt(2.0 * d / a1[i]);
            }
            if (n == 2)
            {
                tt = sqrt(2.0 * d / a1[i]);
                spd = (x[1] - x[0]) / (t[1] - t[0]);
                aa = a1[i] / 2.0;
                bb = -spd;
                cc = -x[0];
                dd = (bb * bb) - (4 * aa * cc);
                xx = -1.0;
                if (dd >= 0.0)
                {
                    x1 = (-bb + sqrt(dd)) / (2 * aa); if ((x1 > 0.0) && (x1 < tt)) xx = x1;
                    x2 = (-bb - sqrt(dd)) / (2 * aa); if ((x2 > 0.0) && (x2 < tt)) xx = x2;
                }
                if ((xx > 0.0) && (xx < tt))
                {
                    yy = 0.5 * a1[i] * xx * xx; // distance at xx
                    tt = xx + ((d - yy) / spd);
                }
            }
            printf("%.6f\n", tt);
        }
    }
    return 0;
}
