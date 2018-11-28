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

int solve(vector<int> input) {
    int N = input.size();

//    REP(i, N)
//        cerr << input[i] << endl;
    int ret = 0;
    REP(i, N) {
        FOR(j, i, N) if (input[j] <= i+1) {
            for (int k = j; k > i; --k) {
                ++ret;
                swap(input[k], input[k-1]);
            }
            break;
        }
        assert(input[i] <= i+1);
    }

//    REP(i, N)
//        cerr << input[i] << endl;

    return ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(caseID, T) {
        int N;
        cin >> N;
        vector<int> input(N, 0);
        REP(i, N) {
            string s;
            cin >> s;
            REP(j, N) if (s[j] == '1') {
                input[i] = j+1;
            }
        }
        cout << "Case #" << caseID+1 << ": " << solve(input) << endl;
    }

    return 0;
}
