// -*- encoding: utf-8-unix -*-
// USED ALGORITHM: 
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <complex>

using namespace std;
typedef complex<double> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
#define ALL(c) (c).begin(), (c).end()
//#define FOR(c, it) for (typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define REP(i, n) for (int i = 0; i < n; ++i)

#define INF (1.0 / 0.0)

inline
double costof(int a, int b, int M, int I)
{
    if (a == b) { return 0; }
    if (M == 0) { return INF; }
    return (abs(b - a) - 1) / M * I;
}

int main(void)
{
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        int D, I, M, N; cin >> D >> I >> M >> N;
        vi v(N); REP(i, N) { cin >> v[i]; }

        vvd cost(N, vd(256));
        REP (k, 256) {
            cost[0][k] = D + I;
            cost[0][k] = min(cost[0][k], (double)abs(v[0]-k));
            cost[0][k] = min(cost[0][k], I + costof(v[0], k, M, I));
        }

        for (int i = 1; i < N; ++i) {
            for (int k1 = 0; k1 < 256; ++k1) {
                cost[i][k1] = INF;
                for (int k2 = 0; k2 < 256; ++k2) {
                    // remove v[i] + insert
                    {
                        double c = D + costof(k2, k1, M, I);
                        if (k1 != k2) { c += I; }
                        cost[i][k1] = min(cost[i][k1], cost[i-1][k2] + c);
                    }
                    // convert v[i] -> k3.   k2 .. k3 .. k1
                    {
                        for (int k3 = min(k1, k2); k3 <= max(k1, k2); ++k3) {
                            double c = costof(k2, k3, M, I) + costof(k3, k1, M, I) + abs(v[i] - k3);
                            if (k3 != k1) { c += I; }
                            cost[i][k1] = min(cost[i][k1], cost[i-1][k2] + c);
                        }
                    }
                }
            }
        }
        
        cout << "Case #" << t << ": " << *min_element(cost[N-1].begin(), cost[N-1].end()) << endl;
    }
    return 0;
}

