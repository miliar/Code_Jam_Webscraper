#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>

using namespace std;

long double maxrun, run, ans, walk;

void add(long double dist, long double w) {
    if ( dist/(w+run) <= maxrun) {
        maxrun -= (dist)/(w+run);
        ans += (dist)/(w+run);
    } else {
        ans += maxrun;
        ans += (dist - (w+run)*maxrun) / (w + walk);
        maxrun = 0.0;
    }
}

int main() {

    int T;
    scanf("%d", &T);


    for (int t = 1; t <= T; t++) {
        
        int len,  n;
        
        ans = 0.0;
        scanf("%d %Lf %Lf %Lf %d", &len, &walk, &run, &maxrun, &n);
        long double b,e,w, prev = 0.0;
        vector<pair<long double, long double> > v;

        for (int i = 0; i < n; i++) {
            scanf("%Lf %Lf %Lf", &b, &e, &w);
            if (b > prev) {
                v.push_back(make_pair(0, b-prev));
            }
            v.push_back(make_pair(w, e-b));
            prev = e;
        }
        if (len > prev) v.push_back(make_pair(0, len-prev));
        sort(v.begin(), v.end());
        for (int i = 0; i < v.size(); i++) {
            add(v[i].second, v[i].first);
        }


        printf("Case #%d: %.10Lf\n", t, ans);

    }
    return 0;
}



