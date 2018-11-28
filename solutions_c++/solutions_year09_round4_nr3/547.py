#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i)
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i)
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i)
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std;
static const double EPS = 1e-9;
typedef long long ll;

bool can(vector<int> a, vector<int> b) {
    if (a[0] < b[0]) {
        REPV(a, i) if (!(a[i] < b[i]))
            return false;
        return true;
    }
    if (a[0] > b[0]) {
        REPV(a, i) if (!(a[i] > b[i]))
            return false;
        return true;
    }
    return false;
}

bool can(vector<vector<int> > &A, int mask) {
    vector<int> t;
    int size = A.size();
    REP(i, size) if (mask & (1<<i)) t.push_back(i);
    REPV(t, i) REPV(t, j) if (i != j && !can(A[t[i]], A[t[j]]))
        return false;
    return true;
}

int solve(vector<vector<int> > &A) {
    int size = A.size();
    vector<bool> tv(1<<size);

    REP(i, (1<<size)) {
        tv[i] = can(A, i);
    }

    vector<int> can2;
    REP(i, (1<<size)) if (tv[i]) {
        bool ok = true;
        REP(j, size) if ((i & (1<<j)) == 0) {
            if (tv[i | (1<<j)]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            can2.push_back(i);
        }
    }

    cerr << size << "," << can2.size() << endl;
    vector<int> w(1<<size, INT_MAX);
    w[0] = 0;
    REP(i, (1<<size)) if (w[i] != INT_MAX) {
        REPV(can2, j) {
            w[i|can2[j]] <?= w[i]+1;
        }
    }

    return w[(1<<size)-1];
}

int main(void)
{
    int T;
    cin >> T;
    REP(caseID, T) {
        int n, k;
        cin >> n >> k;
        vector<vector<int> > A(n, vector<int>(k, 0));
        REP(i, n) REP(j, k)
            cin >> A[i][j];
        cout << "Case #" << caseID+1 << ": " << solve(A) << endl;
    }
    return 0;
}
