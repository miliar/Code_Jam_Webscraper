#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <cmath>
#include <cassert>

using namespace std;
typedef complex<double> P;

int solve(const vector<string>& words, const vector<vector<bool> >& acs)
{
    int cnt = 0;
    for (int i = 0; i < words.size(); ++i) {
        const string& w = words[i];
        bool ok = true;
        for (int k = 0; k < w.length(); ++k) {
            if (!acs[k][w[k] - 'a']) { ok = false; break; }
        }
        if (ok) { ++cnt; }
    }

    return cnt;
}

int main(void)
{
    int L, D, N;
    cin >> L >> D >> N;

    vector<string> words(D);
    for (int i = 0; i < D; ++i) {
        cin >> words[i];
    }

    for (int i = 0; i < N; ++i) {
        string s; cin >> s;
        vector<vector<bool> > acs(D, vector<bool>(26));

        int p = 0;
        int k = 0;
        while (p < s.length()) {
            if (s[p] == '(') {
                ++p;
                while (s[p] != ')') {
                    acs[k][s[p] - 'a'] = true;
                    ++p;
                }
                ++k; ++p;
            } else {
                acs[k][s[p] - 'a'] = true;
                ++k; ++p;
            }
        }

        cout << "Case #" << (i + 1) << ": " << solve(words, acs) << endl;
    }

    return 0;
}

