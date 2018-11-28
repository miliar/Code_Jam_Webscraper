#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

#define EPS 1e-7

int P[203], V[203];

int main()
{
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T, C;
    double D;
    cin >> T;
    for (int cas=1; cas<=T; ++cas)
    {
        cin >> C >> D;
        int vsum = 1;
        for (int i=0; i<C; ++i)
        {
            cin >> P[i] >> V[i];
            vsum += V[i];
        }
        double lo = 0.0, hi = D*vsum, mid;
        double lp, rp;
        do
        {
            bool pos = 1;
            mid = (hi+lo)/2.0;
            rp = P[0]-mid;
            for (int i=0; i<C; ++i)
            {
                lp = max(rp, P[i]-mid);
                rp = lp + (V[i]-1)*D;
                if (rp>(P[i]+mid))
                {
                    pos = 0;
                    break;
                }
                rp += D;
                //cout << lp << ' ' << rp << '\n';
            }
            //cout << '\n';
            if (pos) hi = mid;
            else lo = mid;
        }
        while (fabs(hi-lo)>EPS);
        printf("Case #%d: %.7lf\n", cas, mid+EPS);
    }
    return 0;
}
