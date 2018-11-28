#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int X, S, R, t, N;

struct interval {
    interval(int p, int q, int v) : p(p), q(q), v(v) {}
    int p, q, v;
};

bool cmp_il(interval const& a, interval const& b) {
    if (a.p != b.p) return a.p < b.p;
    return a.q < b.q;
}

bool cmp_i(interval const& a, interval const& b) {
    int l_a = a.q - a.p, l_b = b.q - b.p;

    double r_a = static_cast<double>(a.v + R) / (a.v + S);
    double r_b = static_cast<double>(b.v + R) / (b.v + S);

    if (fabs(r_a-r_b) > 1e-6) return r_a > r_b;
    return a.v < b.v;
}

long double solve(vector<interval> const& v) {
    long double T = 0.0;
    int L = v.size();

    long double t_ = t;

    for (int i = 0; i < L; ++i) {
        int s = v[i].q-v[i].p;

        int v_r = R + v[i].v;
        int v_s = S + v[i].v;

        long double t_r = static_cast<long double>(s) / v_r;
        t_r = min(t_r, t_);

        long double s_r = t_r * v_r;
        long double s_s = s - s_r;

        T += t_r + s_s/v_s;
        t_ -= t_r;
    }

    return T;
}

int main() {
    int T; scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        
        vector<interval> vi;
        for (int i = 0; i < N; ++i) {
            int B, E, w;
            scanf("%d%d%d", &B, &E, &w);
            
            vi.push_back(interval(B, E, w));
        }

        sort(vi.begin(), vi.end(), cmp_il);
        
        vector<interval> v;
        int last = 0;

        for (int i = 0; i < N; ++i) {
            if (vi[i].p > last)
                v.push_back(interval(last, vi[i].p, 0));

            v.push_back(vi[i]);
            last = vi[i].q;
        }
        if (last < X)
            v.push_back(interval(last, X, 0));

        sort(v.begin(), v.end(), cmp_i);

        printf("Case #%d: %.8Lf\n", tc, solve(v));
    }

    return 0;
}
