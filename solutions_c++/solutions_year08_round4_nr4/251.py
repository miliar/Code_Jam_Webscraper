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

string apply(string s, vector<int> perm) {
    int n = s.size(), k = perm.size();
    string t(n, '.');
    for(int p = 0; p < n; p += k) {
        REP(i, k)
            t[p+i] = s[p+perm[i]];
    }
    return t;
}

int eval(string s) {
    int n = s.size();
    int res = 1;
    for(int i = 0; i < n-1; i++)
        if (s[i] != s[i+1])
            res++;
    return res;
}

void solve_case() {

    int k;
    string s;
    cin >> k >> s;
    int n = s.size();

    vector<int> perm(k);
    REP(i, k)
        perm[i] = i;

    int res = n;
    do {
        res <?= eval(apply(s, perm));
    } while(next_permutation(ALLOF(perm)));

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
