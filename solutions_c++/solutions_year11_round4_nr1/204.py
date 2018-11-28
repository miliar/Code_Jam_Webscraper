#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        long long X, S, R, N; double t;
        scanf("%lld %lld %lld %lf %lld", &X, &S, &R, &t, &N);
        R -= S;
        vector<pair<long long, double> > walk;

        for(int i = 0; i < N; i++) {
            long long B, E, W;
            scanf("%lld %lld %lld", &B, &E, &W);
            X -= E-B;
            walk.push_back(make_pair(W+S, E-B));
        }
        walk.push_back(make_pair(S, X));
        sort(walk.begin(), walk.end());

        double ans = 0;
        unsigned int i;
        for(i = 0; i < walk.size(); i++) {
            long long nspeed = walk[i].first + R;
            if(nspeed * t >= walk[i].second) {
                ans += walk[i].second/(double)nspeed;
                t -= walk[i].second/(double)nspeed;
            } else {
                ans += t;
                walk.push_back(make_pair(walk[i].first, walk[i].second - nspeed * t));
                i++;
                break;
            }
        }

        for(; i < walk.size(); i++)
            ans += walk[i].second/(double)walk[i].first;

        printf("Case #%d: %.9lf\n", z, ans);
    }
}
