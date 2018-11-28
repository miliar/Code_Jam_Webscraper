#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
using namespace std;

typedef pair<int, int> pii;

int C, D;

inline bool check(vector<pii> &v, long double d) {
    long double l = -1e12;

    for (int i = 0; i < C; ++i) {
        int pos = v[i].first;
        int cnt = v[i].second;

        l = max(l+D, pos-d);
        long double r = l + (cnt-1)*D;

        if (l > pos + d || fabs(pos-r) > d)
            return false;

        l = r;
    }

    return true;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        scanf("%d%d", &C, &D);
        
        vector<pii> v;
        for (int j = 0; j < C; ++j) {
            int a, b;

            scanf("%d%d", &a, &b);
            v.push_back(make_pair(a,b));
        }

        long double l = 0.0, r = 1e12;
        while (r-l > 1e-8) {
            long double mid = l/2.0 + r/2.0;

            if (check(v, mid)) {
                r = mid;
            } else {
                l = mid;
            }
        }

        printf("Case #%d: %.8Lf\n", i+1, l);
    }

    return 0;
}
