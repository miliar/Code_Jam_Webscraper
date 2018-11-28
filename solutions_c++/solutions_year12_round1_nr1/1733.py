#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<pair<int, int> > VII;
typedef vector<char> VC;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<int, int> MII;
typedef long long int LL;

#define FOR(i,a,b) for (int i=(int)(a); i<(int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define SORT(c) sort((c).begin(), (c).end());
#define RSORT(c) sort((c).rbegin(), (c).rend());
#define DUMP(x) cerr << #x << "=" << (x) << " ";
#define DUMPLN(x) cerr << #x << "=" << (x) << endl;

void solve(int problem, int types, int length, const vector<double>& corr) {
    vector<double> needBs(corr.size());

    double good = 1.0;
    REP (i, types) {
        needBs[i] = good * (1 - corr[i]);
        good *= corr[i];
    }

    double ans= numeric_limits<double>::max();
    int full = length + 1;
    int rest = length - types + 1;

    for (int bs = 1; bs <= types; bs++) {
        double ok = needBs[types - bs] + good;
        if (bs == types) ok = 1.0;
        double ng = 1 - ok;
        double temp = ((bs * 2) + rest) + (ng * full);
        if (temp < ans) ans = temp;
    }

    // keep typing
    double temp = (good * rest) + ((1-good) * (rest + full));
    if (temp < ans) ans = temp;

    // enter right away
    temp = 1 + full;
    if (temp < ans) ans = temp;

    printf("Case #%d: %.6f\n", problem, ans);
}

//----------------------------------------------------
int NUM_CASES = 0;

void solve() {
}

int main() {
    cin >> NUM_CASES;
    REP(i, NUM_CASES) {
        int types, length;
        cin >> types >> length;
        vector<double> correctness(types);
        REP (j, types) cin >> correctness[j];
        solve(i+1, types, length, correctness);
    }
}
