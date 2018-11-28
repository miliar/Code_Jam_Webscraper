#include <iostream>
#include <climits>
using namespace std;
const int maxc = 200 + 10, maxd = 1000000 + 10;
const long double maxans = 1e13, delta = 1e-7;

int c;
long double d;
long double p[maxc];
int v[maxc];

int zero(long double e)
{
    if (e < -delta)
        return -1;
    return e > delta;
}

bool solve(long double s)
{
    long double last = -1e100;
    for (int i = 0; i < c; i++)
        for (int j = 0; j < v[i]; j++) {
            long double pos = last + d;
            if (zero(pos - p[i]) < 0) {
                last = max(pos, p[i] - s);
            } else {
                if (zero(pos - p[i] - s) > 0)
                    return false;
                last = pos;
            }
        }
    return true;
}

int main(void)
{
    int T;
    cin >> T;
    for (int loop = 1; loop <= T; loop++) {
        cin >> c >> d;
        for (int i = 0; i < c; i++)
            cin >> p[i] >> v[i];

        long double l, r;
        l = 0;
        r = maxans;
        while (l + delta < r) {
            long double mid = (l + r) / 2.0;
            if (solve(mid))
                r = mid;
            else
                l = mid;
        }
        //cout << "Case #" << loop << ' ' << r << endl;
        printf("Case #%d: %.10Lf\n", loop, r);
    }
    return 0;
}
