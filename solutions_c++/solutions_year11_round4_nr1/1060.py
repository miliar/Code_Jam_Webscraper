#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int i, j, k;
    double d;
    double ret;
    int tc, TC;
    int X, S, R, N, t;
    double tt;
    int B[1010];
    int E[1010];
    int w[1010];
    double P[3000];
    double v[3000];

    cin >> TC;

    for(tc=1;tc<=TC;tc++) {
        cin >> X >> S >> R >> t >> N;
        B[0] = E[0] = 0;
        w[0] = 0;
        for(i=1;i<=N;i++) {
            cin >> B[i] >> E[i] >> w[i];
        }
        B[N+1] = E[N+1] = X;
        w[N+1] = 0;
        N += 2;
        for(i=0;i<N;i++) {
            P[2*i+0] = B[i];
            v[2*i+0] = w[i];
            P[2*i+1] = E[i];
            v[2*i+1] = 0;
        }
        vector<pair<double, double> > vp;
        for(i=0;i<(2*N-1);i++) {
            vp.push_back(make_pair(v[i],P[i+1]-P[i]));
        }
        sort(vp.begin(), vp.end());

        ret = 0;
        tt = t;
        for(i=0;i<vp.size();i++) {
            if ((vp[i].first+R)*tt > vp[i].second) {
                ret += vp[i].second/(vp[i].first+R);
                tt  -= vp[i].second/(vp[i].first+R);
            } else {
                ret += (tt + (vp[i].second-(vp[i].first+R)*tt)/(vp[i].first+S));
                tt  = 0.0;
            }
        }

        printf("Case #%d: %.20f\n", tc, ret);
        //        cout << "Case #" << tc << ": " << ret << endl;
    }
    
    return 0;
}
