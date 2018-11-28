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
        int n, k; cin >> n >> k;
        int s = (1 << n) - 1;
        if ((k & s) == s) {
            cout << "Case #" << caseNo << ": ON" << endl;
        } else {
            cout << "Case #" << caseNo << ": OFF" << endl;            
        }
    }

    return 0;
}

