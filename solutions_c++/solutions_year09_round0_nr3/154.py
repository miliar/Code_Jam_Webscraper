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

int solve(const string &pattern, const string &text) {
    int ps = pattern.size();
    int ts = text.size();
    vector<int> work(ps+1, 0);
    work[0] = 1;
    REP(i, ts) {
        for (int j = ps-1; j >= 0; --j) {
            if (pattern[j] == text[i]) {
                work[j+1] += work[j];
                work[j+1] %= 10000;
            }
        }
    }
    return work[ps];
}

int main(void)
{
    int N;
    cin >> N;

    string input;
    getline(cin, input);
    REP(i, N) {
        getline(cin, input);
        printf("Case #%d: %04d\n", i+1, solve("welcome to code jam", input));
    }

    return 0;
}
