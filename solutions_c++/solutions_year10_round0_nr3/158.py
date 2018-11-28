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
typedef vector<string> vs;
#define ALL(c) (c).begin(), (c).end()
//#define FOR(c, it) for (typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define REP(i, n) for (int i = 0; i < n; ++i)


int main(void)
{
    int T; cin >> T;
    for (int caseNo = 1; caseNo <= T; ++caseNo) {
        int R, k, N; cin >> R >> k >> N;
        vi v(N); REP(i, N) { cin >> v[i]; }
        
        vi sum(N), next(N);
        for (int i = 0; i < N; ++i) {
            int s = 0;
            for (int j = 0; j < N; ++j) {
                if (sum[i] + v[(i + j) % N] <= k) {
                    sum[i] += v[(i + j) % N];
                } else {
                    next[i] = (i + j) % N;
                    break;
                }
            }
        }

        int cur = 0;
        long long ans = 0;
        for (int i = 0; i < R; ++i) {
            ans += sum[cur];
            cur = next[cur];
        }

        cout << "Case #" << caseNo << ": " << ans << endl;
    }

    return 0;
}

