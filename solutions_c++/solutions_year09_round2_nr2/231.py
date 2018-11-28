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

string solve(string input) {
    if (next_permutation(input.begin(), input.end()))
        return input;
    else {
        sort(input.begin(), input.end());
        input.insert(input.begin(), '0');
        int i = 0;
        while(input[0] == '0') {
            input.erase(input.begin());
            ++i;
        }
        REP(j, i)
            input.insert(input.begin()+1, '0');
    }
    return input;
}

int main(void)
{
    int N;
    cin >> N;
    REP(caseID, N) {
        string input;
        cin >> input;
        cout << "Case #" << caseID+1 << ": " << solve(input) << endl;
    }

    return 0;
}
