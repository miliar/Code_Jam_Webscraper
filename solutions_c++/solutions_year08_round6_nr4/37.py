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
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

typedef vector< vector<bool> > Graph;

Graph readTree() {
    int n;
    cin >> n;
    Graph tree(n, vector<bool>(n, false));
    REP(i, n-1) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        tree[a][b] = tree[b][a] = true;
    }
    return tree;
}

bool match(const Graph& large, const Graph& small, const vector<int>& perm) {
    int n = large.size(), m = small.size();

    REP(i, m) REP(j, m) {
        if (small[i][j] != large[perm[i]][perm[j]])
            return false;
    }
    return true;
}

void solve() {

    Graph large = readTree();
    Graph small = readTree();

    int n = large.size(), m = small.size();

    vector<int> perm(n);
    REP(i, n)
        perm[i] = i;

    bool ok = false;
    do {
        if (match(large, small, perm)) {
            ok = true;
            break;
        }
    } while(next_permutation(ALLOF(perm)));

    cout << (ok ? "YES" : "NO") << endl;

}


int main() {


    int nCases;
    cin >> nCases >> ws;

    REP(iCase, nCases) {

        cout << "Case #" << iCase+1 << ": ";
        solve();

    }

    return 0;
}

