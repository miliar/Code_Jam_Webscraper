#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

const double eps = 1e-8;

int dcmp(double x) {
    return (x > +eps) - (x < -eps);
}

int main() {
    freopen("B.out", "w", stdout);
    int l, p, c;
    int t;
    scanf("%d", &t);
    for (int ca = 0; ca < t; ++ca) {
        scanf("%d %d %d", &l, &p, &c);
        int ans = 0;
        double R = 1.0 * p / l;
        while (dcmp(R - c) > 0) {
            R = sqrt(R);
            ans++;
        }
        printf("Case #%d: %d\n", ca + 1, ans);
    }
    return 0;
}
