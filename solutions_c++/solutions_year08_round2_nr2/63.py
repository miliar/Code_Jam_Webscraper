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


int find_root(vector<int>& uf, int a) {
    return (uf[a] < 0 ? a : uf[a] = find_root(uf, uf[a]));
}

int merge(vector<int>& uf, int a, int b) {
    int ra = find_root(uf, a);
    int rb = find_root(uf, b);
    if (ra != rb) {
        if (uf[rb] < uf[ra])
            swap(ra, rb);
        uf[ra] += uf[rb];
        uf[rb] = ra;
    }
    return (ra != rb);
}

void solve_case() {

    long long int from, to, plower;
    cin >> from >> to >> plower;

    int n = to-from+1;

    const int P = 1000000+100;
    vector<int> isprime(P+1, true);
    isprime[0] = isprime[1] = false;
    vector<int> primes;
    for(int i = 2; i <= P; i++) {
        if (isprime[i]) {
            if (i >= plower)
                primes.push_back(i);
            for(int j = i*2; j <= P; j+=i)
                isprime[j] = false;
        }
    }

    vector<int> uf(n, -1);
    FOR(it, primes) {
        int p = *it;
        long long int head = (from+p-1)/p*p;
        for(long long int i = head; i <= to; i += p) {
            merge(uf, (int)(i-from), (int)(head-from));
        }
    }

    int res = 0;
    REP(i, n)
        if (uf[i] < 0)
            res++;
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
