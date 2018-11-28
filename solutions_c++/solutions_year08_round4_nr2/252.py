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


pair<int,int> decompose(int a, int n, int m) {
    for(int i = 1; i <= n; i++) {
        int j = a / i;
        if (j <= m && i*j == a)
            return make_pair(i, j);
    }
    assert(false);
    return make_pair(-1, -1);
}

int huge[(10010)*(10010)];

void solve_case() {

    int n, m, a;
    cin >> n >> m >> a;

    int k = 0;
    for(int i = 0; i <= n; i++)
        for(int j = 0; j <= m; j++)
            huge[k++] = i*j;

    sort(huge, huge+k);
    k = unique(huge, huge+k) - huge;

    int i = 0, j = 0;
    int s = -1, t = -1;
    while(i < k && j < k) {
        while(huge[j]-huge[i] < a) {
            j++;
            if (j == k)
                break;
        }
        if (j == k)
            break;
        if (huge[j]-huge[i] == a) {
            s = i;
            t = j;
            break;
        }
        i++;
    }
    if (s < 0) {
        cout << "IMPOSSIBLE" << endl;
    }
    else {
        pair<int,int> p = decompose(huge[s], n, m);
        pair<int,int> q = decompose(huge[t], n, m);
        printf("0 0 %d %d %d %d\n",
               p.first, q.second, q.first, p.second);
    }

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
