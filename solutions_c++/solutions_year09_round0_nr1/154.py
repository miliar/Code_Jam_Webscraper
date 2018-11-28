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

bool isOK(const string &word, const vector<string> &input) {
    assert(word.size() == input.size());
    int L = word.size();
    REP(i, L) {
        bool ok = false;
        REPV(input[i], j) if (word[i] == input[i][j]) {
            ok = true;
            break;
        }
        if (!ok)
            return false;
    }
    return true;
}

// ex.
// input:  "(abc)bc(a(bc))"
// output: {"abc", "b", "c", "abc"}
vector<string> decompose(const string &input) {
    vector<string> ret;
    REPV(input, i) {
        if (input[i] == '(') {
            int d = 1;
            string s;
            while(i != (int)input.size() && d) {
                ++i;
                if (input[i] == ')')
                    --d;
                else if (input[i] == '(')
                    ++d;
                else
                    s += input[i];
            }
            assert(d == 0);
            ret.push_back(s);
        } else {
            ret.push_back(string(1, input[i]));
        }
    }
    return ret;
}

int solve(const vector<string> &words, const string &input) {
    int ret = 0;

    vector<string> work = decompose(input);

    REPV(words, i) if (isOK(words[i], work))
        ++ret;

    return ret;
}

int main(void)
{
    int L, D, N;
    cin >> L >> D >> N;
    vector<string> words(D);
    REP(i, D) cin >> words[i];

    REP(i, N) {
        string input;
        cin >> input;
        cout << "Case #" << i+1 << ": " << solve(words, input) << endl;
    }
    return 0;
}
