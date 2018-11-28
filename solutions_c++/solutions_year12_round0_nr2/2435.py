#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <memory>
#include <cassert>
using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(), (a).end()
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define MP make_pair
#define DBG(x) cout << #x << " = " << x << endl

int solve(int N, int S, int p, const vector<int>& t) {
    assert(SIZE(t) == N);
    int ok_scores = 0;
    int half_scores = 0;
    if (p == 0) return N;
    if (p == 1) {
        REP(i, N) if (t[i] >= 1) ok_scores++;
        return ok_scores;
    }
    REP(i, N) {
        if (t[i] >= 3 * p - 2) {
            ok_scores++;
        } else if (t[i] >= 3 * p - 4) {
            half_scores++;
        }
    }
    return ok_scores + min(half_scores, S);
}

int main() {
    int T;
    cin >> T;
    REP(zzz, T) {
        int N; cin >> N;
        int S; cin >> S;
        int p; cin >> p;
        vector<int> t(N);
        REP(i, N) cin >> t[i];
        cout << "Case #" << zzz + 1 << ": " << solve(N, S, p, t) << endl;
    }
}
