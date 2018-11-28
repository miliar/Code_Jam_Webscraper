#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>

#include <gmp.h>
#include <gmpxx.h>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

typedef complex<long long int> P;

vector<P> read_points() {
    int n;
    long long int A, B, C, D, x, y, M;
    cin >> n >> A >> B >> C >> D >> x >> y >> M;

    vector<P> res(n);
    REP(i, n) {
        res[i] = P(x, y);
        x = (A * x + B) % M;
        y = (C * y + D) % M;
    }

    return res;
}

void solve_case() {
    vector<P> v = read_points();
    int n = v.size();

    int res = 0;
    REP(i, n) REP(j, i) REP(k, j) {
        P a = v[i], b = v[j], c = v[k];
        P g = a+b+c;
        if (g.real() % 3 == 0 && g.imag() % 3 == 0)
            res++;
    }
    cout << res << endl;
}


int main() {

    int nCases;
    cin >> nCases;

    REP(iCase, nCases) {
        cout << "Case #" << iCase+1 << ": ";
        solve_case();
    }

    return 0;
}
