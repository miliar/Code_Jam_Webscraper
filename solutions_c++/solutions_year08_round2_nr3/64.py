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
    if (ra != rb)
        uf[rb] = ra;
    return (ra != rb);
}

void solve_case() {

    int k;
    cin >> k;

    vector<int> deck(k, 0);
    vector<int*> ptr(k);
    REP(i, k)
        ptr[i] = &deck[i];

    REP(i, k) {
        rotate(ptr.begin(), ptr.begin()+i%ptr.size(), ptr.end());
        int* p = ptr[0];
        ptr.erase(ptr.begin());
        *p = i+1;
    }

    int n;
    cin >> n;
    REP(i, n) {
        int x;
        cin >> x;
        x--;
        if (i > 0)
            cout << " ";
        cout << deck[x];
    }
    cout << endl;

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
