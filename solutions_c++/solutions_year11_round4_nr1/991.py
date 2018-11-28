#include <cstdio>
#include <cmath>
#include <algorithm>

#include <vector>

using namespace std;

struct TInterval {
    double Begin;
    double End;
    double DeltaSpeed;
    bool IsWalkaway;

    bool operator<(const TInterval& i) const {
        return DeltaSpeed < i.DeltaSpeed;
    }
};

typedef vector<TInterval> TIntervals;

int main() {
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int iTest = 0; iTest < t; ++iTest) {
        double x, s, r, t;
        int n;
        scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
        double now = 0.0;
        TIntervals intervals;
        for (int i = 0; i < n; ++i) {
            double b, e, si;
            scanf("%lf%lf%lf", &b, &e, &si);
            {
                intervals.push_back(TInterval());
                TInterval& nowi = intervals.back();
                nowi.Begin = now;
                nowi.End = b;
                nowi.DeltaSpeed = 0.0;
                nowi.IsWalkaway = false;
            }
            
            {
                intervals.push_back(TInterval());
                TInterval& nowi = intervals.back();
                nowi.Begin = b;
                nowi.End = e;
                nowi.DeltaSpeed = si;
                nowi.IsWalkaway = true;
            }
            
            now = e;
        }

        {
            intervals.push_back(TInterval());
            TInterval& nowi = intervals.back();
            nowi.Begin = now;
            nowi.End = x;
            nowi.DeltaSpeed = 0.0;
            nowi.IsWalkaway = false;
        }
        sort(intervals.begin(), intervals.end());

        double time = 0.0;
        double iLen = 0.0;
        for (size_t i = 0; i < intervals.size(); ++i) {
            const TInterval& nowi = intervals[i];
            double len = nowi.End - nowi.Begin;
            iLen += len;
            double tNeedRun = len / (r + nowi.DeltaSpeed);
            double tRun = min(t, tNeedRun);
            double tNotRun = (len - tRun*(r + nowi.DeltaSpeed))/(s + nowi.DeltaSpeed);
            t -= tRun;
            time += tRun + tNotRun;
        }
        if ( fabs(iLen - x) > 1e-9 )
            fprintf(stderr, "bad len\n");

        printf("Case #%d: %.10lf\n", iTest + 1, time);
    }

    return 0;
}
